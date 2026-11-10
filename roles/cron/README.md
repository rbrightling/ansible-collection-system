CRON
====

Install and Manage Cron

Requirements
------------

Supported OS's:
  - Debian 13

Role Variables
--------------

```yaml
cron_allow_users: []
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: include rbrightling.system.cron
      include_role:
        name: rbrightling.system.cron
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
