Ansible Collection - rbrightling.system
=======================================

[![Ansible Galaxy](http://img.shields.io/badge/galaxy-rbrightling.system-660198.svg?style=flat)](https://galaxy.ansible.com/rbrightling/system)

Base system collection of roles to manage and configure base system features and security.

Roles
-----

| Roles                                                                                                       | Build Status                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [aide](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/aide)                       | [![rbrightling.system.aide](https://github.com/rbrightling/ansible-collection-system/actions/workflows/aide.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/aide.yml)                                  |
| [ansible_account](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/ansible_account) | [![rbrightling.system.ansible_account](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_account.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_account.yml) |
| [ansible_node](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/ansible_node)       | [![rbrightling.system.ansible_node](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)          |
| [auditd](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/auditd)                   | [![rbrightling.system.auditd](https://github.com/rbrightling/ansible-collection-system/actions/workflows/auditd.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)                      |
| [fail2ban](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/fail2ban)               | [![rbrightling.system.fail2ban](https://github.com/rbrightling/ansible-collection-system/actions/workflows/fail2ban.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)                  |
| [hosts](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/hosts)                     | [![rbrightling.system.hosts](https://github.com/rbrightling/ansible-collection-system/actions/workflows/hosts.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)                        |
| [openssh_server](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/openssh_server)   | [![rbrightling.system.openssh_server](https://github.com/rbrightling/ansible-collection-system/actions/workflows/openssh_server.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)      |
| [shadow_utils](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/shadow_utils)       | [![rbrightling.system.shadow_utils](https://github.com/rbrightling/ansible-collection-system/actions/workflows/shadow_utils.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)          |
| [sudo](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/sudo)                       | [![rbrightling.system.sudo](https://github.com/rbrightling/ansible-collection-system/actions/workflows/sudo.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)                          |
| [sysstat](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/sysstat)                 | [![rbrightling.system.sysstat](https://github.com/rbrightling/ansible-collection-system/actions/workflows/sysstat.yml/badge.svg?branch=main)](https://github.com/rbrightling/ansible-collection-system/actions/workflows/ansible_node.yml)                    |

Requirements
------------

Supported OS's:
  - Debian 12

Usage
-----

Install this ansible collection:

```bash
ansible-galaxy collection install rbrightling.system
```

Example Playbook
----------------

```yaml
---
- hosts: localhost
  tasks:
    - include_role:
        name: rbrightling.system.{{ role_name }}
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
