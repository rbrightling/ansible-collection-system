Hosts
=====

Manage the system hosts file for static hostnames lookup.

Requirements
------------

None

Role Variables
--------------

```
# 127.0.1.1 is often used for the FQDN of the machine
hosts_hostname_address: 127.0.1.1
# ansible_default_ipv4.address
# null: to remove

# List of addresses with hostnames to resolve.
hosts_list: {}
# Example:
#   192.168.0.10: webserver webserver.local
#   192.168.0.11:
#     - dbserver
#     - dbserver.local
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: servers
  tasks:
    - name: include role rbrightling.system.hosts
      include_role:
        name: rbrightling.system.hosts
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
