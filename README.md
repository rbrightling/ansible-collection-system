Ansible Collection - rbrightling.system
=======================================

Base system collection of roles to manage and configure base system features and security.

Roles
-----

- ansible_node
- auditd
- fail2ban
- openssh_server
- shadow_utils
- sudo
- sysstat

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
