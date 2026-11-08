""" NFTables Ansible Jinja2 Filters """
from typing import TypedDict, NotRequired
import ipaddress
from ansible.parsing.yaml.objects import AnsibleUnicode
from ansible.errors import AnsibleFilterError

class Rule(TypedDict):
    protocol: str
    port: int
    ip: NotRequired[str]

def _split_srcs(sources):
    ip_versions = {
      4: [],
      6: []
    }
    for ip_src in sources:
      ip_addr = ipaddress.ip_address(ip_src)
      ip_versions[ip_addr.version].append(ip_src)
    return ip_versions



def nftables_addr_set(set):
    name = set['name']
    ip_versions = _split_srcs(set['srcs'])
    output = []
    if ip_versions[4]:
        output.append(
            f"set @{name}_v4\n"
            f"  type ipv4_addr\n"
            f"  flags interval\n"
            f"  elements = {{ {", ".join(ip_versions[4])} }}\n"
        )
    if ip_versions[6]:
        output.append(
            f"set @{name}_v6\n"
            f"  type ipv6_addr\n"
            f"  flags interval\n"
            f"  elements = {{ {", ".join(ip_versions[6])} }}\n"
                )
    return "\n".join(output)

def _sets_to_versions():
    pass

def nftables_tcp_accept_rule(rule, ipaddr_sets=None, match_sets=None):

    ipaddr_sets_reg = {}
    for ipaddr_set in (ipaddr_sets or []):
        ipaddr_sets_reg[ipaddr_set['name']] = {
            "v6": any(":" in str(ip) for ip in ipaddr_set.get('srcs', [])),
            "v4": any("." in str(ip) for ip in ipaddr_set.get('srcs', []))
        }

    ip_family_map = { 4: "ip", 6: "ip6" }

    if isinstance(rule["ports"], list) and len(rule["ports"]) == 1:
        rule["ports"] = rule["ports"][0]

    nft_rules = []

    if "src" in rule and rule["src"] is not None:
        sources = [rule["src"]] if isinstance(rule["src"], str) else rule["src"]
        for ip_src in sources:
                    try:
                        ip_addr = ipaddress.ip_address(ip_src)
                        nft_rules.append({
                            'src': rule["src"],
                            'family': ip_addr.version
                        })
                    except ValueError:
                        if ip_src in ipaddr_sets_reg:
                            if ipaddr_sets_reg[ip_src]['v4']:
                                nft_rules.append({
                                    'src': f"@{ip_src}_v4",
                                    'family': 4
                                })
                            if ipaddr_sets_reg[ip_src]['v6']:
                                nft_rules.append({
                                    'src': f"@{ip_src}_v6",
                                    'family': 6
                                })
                        else:
                            raise AnsibleFilterError(f"Specified set not found: {rule['src']}")

    elif "meter" in rule and rule["meter"] is not None:
        nft_rules.append({**rule,**{'family': 4}})
        nft_rules.append({**rule,**{'family': 6}})
    else:
        nft_rules.append(rule)

    output_lines = []

    for ip_version in nft_rules:
        parts = []
        if "interface" in rule and rule["interface"] is not None:
            parts.append(f"iifname \"{rule['interface']}\"")
        if 'src' in ip_version and ip_version["src"] is not None:
            parts.append(f"{ip_family_map[ip_version['family']]} saddr {ip_version['src']}")
        parts.append('tcp')
        if isinstance(rule['ports'], list):
            ports = ", ".join(map(str, rule['ports']))
            parts.append(f"dport {{{ports}}}")
        else:
            parts.append(f"dport {rule['ports']}")

        if "rate_limit" in rule and rule["rate_limit"] is not None:
            if 'meter' in rule and rule["meter"] is not None:
                parts.append(f"ct state new add @{rule['meter']}_v{ip_version['family']} {{ {ip_family_map[ip_version['family']]} saddr limit rate {rule['rate_limit']} }}")
            else:
                parts.append(f"ct state new limit rate {rule['rate_limit']}")
        parts.append("accept")
        if "comment" in rule and rule["comment"] is not None:
            parts.append(f"comment \"{rule['comment']}\"")
        output_lines.append(" ".join(parts))

    return "\n".join(output_lines)
