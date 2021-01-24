Ansible Collection - rbrightling.system
=======================================



Base system collection of roles to manage and configure base system features and security.

Roles
-----

| Roles                                                                                                       | Build Status                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ansible_node](https://github.com/rbrightling/ansible-collection-system/blob/main/docs/ansible_node.md)     | ![rbrightling.system.ansible_node](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.ansible_node/badge.svg?branch=main)     |
| [auditd](https://github.com/rbrightling/ansible-collection-system/blob/main/docs/auditd.md)                 | ![rbrightling.system.auditd](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.auditd/badge.svg?branch=main)                 |
| [fail2ban](https://github.com/rbrightling/ansible-collection-system/blob/main/docs/fail2ban.md)             | ![rbrightling.system.fail2ban](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.fail2ban/badge.svg?branch=main)             |
| [openssh_server](https://github.com/rbrightling/ansible-collection-system/blob/main/docs/openssh_server.md) | ![rbrightling.system.openssh_server](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.openssh_server/badge.svg?branch=main) |
| [shadow_utils](https://github.com/rbrightling/ansible-collection-system/blob/main/docs/shadow_utils.md)     | ![rbrightling.system.shadow_utils](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.shadow_utils/badge.svg?branch=main)     |
| [sudo](https://github.com/rbrightling/ansible-collection-system/blob/main/docs/sudo.md)                     | ![rbrightling.system.sudo](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.sudo/badge.svg?branch=main)                     |
| [sysstat](https://github.com/rbrightling/ansible-collection-system/blob/main/docs/sysstat.md)               | ![rbrightling.system.sysstat](https://github.com/rbrightling/ansible-collection-system/workflows/rbrightling.system.sysstat/badge.svg?branch=main)               |

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
