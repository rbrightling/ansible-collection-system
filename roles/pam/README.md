PAM
===

Manage System PAM.

Requirements
------------

Supported OS's:
  - Debian 13


Role Variables
--------------

```yaml
pam_su_require_wheel: true
pam_su_wheel_group: sudo


# faillock specific configuration
pam_faillock_deny: 3
pam_faillock_unlock_time: 300
pam_faillock_fail_interval: 900
pam_faillock_audit: true
pam_faillock_even_deny_root: true

# pwhistory
pam_pwhistory_remember: 5
pam_pwhistory_enforce_for_root: true

# pwquality
pam_pwquality_minlen: 15
pam_pwquality_dcredit: -1
pam_pwquality_ucredit: -1
pam_pwquality_lcredit: -1
pam_pwquality_ocredit: -1
pam_pwquality_minclass: 4
pam_password_rounds: 11

# Limits
pam_limits_default_hard_core: 0
pam_limits_default_soft_nproc: 1024
pam_limits_default_hard_nproc: 2048
pam_limits_root_hard_nproc: 655336

pam_limits_default_soft_nofile: 8192
pam_limits_default_hard_nofile: 16384
pam_limits_root_hard_nofile: 65536

pam_limits_default_hard_nice: -19
pam_limits_root_hard_nice: -20
```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: include rbrightling.system.pam
      include_role:
        name: rbrightling.system.pam
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
