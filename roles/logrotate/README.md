LOGROTATE
=========

Install and Configure Logrotate.

Requirements
------------

Supported OS's:
  - Debian 13

Role Variables
--------------

```yaml
logrotate_frequency: "weekly"

logrotate_rotate: 13

logrotate_size: 100M


logrotate_create_permissions: '0640'
logrotate_create_user: 'root'
logrotate_create_group: 'adm'

logrotate_dateext: true

logrotate_compress: true
logrotate_delay_compress: true

logrotate_missing_ok: true
logrotate_if_empty: false
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: include rbrightling.system.logrotate
      include_role:
        name: rbrightling.system.logrotate
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
