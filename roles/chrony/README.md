CHRONY
======

Install and configure Chrony.

Requirements
------------

Supported OS's:
  - Debian 13

Role Variables
--------------

```yaml
chrony_sources:
  - "pool 2.debian.pool.ntp.org iburst"
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: include rbrightling.system.chrony
      include_role:
        name: rbrightling.system.chrony
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)

