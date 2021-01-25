Ansible Collection - rbrightling.system
=======================================

[![Ansible Galaxy](http://img.shields.io/badge/galaxy-rbrightling.system-660198.svg?style=flat)](https://galaxy.ansible.com/rbrightling/system)

Base system collection of roles to manage and configure base system features and security.

Roles
-----

| Roles                                                                                                     | Build Status                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ansible_node](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/ansible_node)     | ![rbrightling.system.ansible_node](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.ansible_node/badge.svg?branch=main)     |
| [auditd](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/auditd)                 | ![rbrightling.system.auditd](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.auditd/badge.svg?branch=main)                 |
| [fail2ban](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/fail2ban)             | ![rbrightling.system.fail2ban](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.fail2ban/badge.svg?branch=main)             |
| [openssh_server](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/openssh_server) | ![rbrightling.system.openssh_server](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.openssh_server/badge.svg?branch=main) |
| [shadow_utils](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/shadow_utils)     | ![rbrightling.system.shadow_utils](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.shadow_utils/badge.svg?branch=main)     |
| [sudo](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/sudo)                     | ![rbrightling.system.sudo](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.sudo/badge.svg?branch=main)                     |
| [sysstat](https://github.com/rbrightling/ansible-collection-system/tree/main/roles/sysstat)               | ![rbrightling.system.sysstat](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.sysstat/badge.svg?branch=main)               |

Requirements
------------

Supported OS's:
  - Debian 10
  - RedHat 8

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
