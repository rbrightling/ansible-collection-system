ANSIBLE_ACCOUNT
===============

Create an Ansible User account for Remote Management.

Requirements
------------

Supported OS's
  - Debian 12

Role Variables
--------------

```
# Name for the ansible account
ansible_account_name: "ansible"

# Path for the ansible sudoers file
ansible_account_sudoers_path: "/etc/sudoers.d/ansible"

# List of keys for adding as authorized access
ansible_account_authorized_keys: []

# Set a optional uid for the user
ansible_account_uid: null

ansible_account_sudoers_validate: "{{ sudo_visudo_path|default('/usr/sbin/visudo') }} -cf %s"
```

Dependencies
------------

- Sudo
  rbrightling.system.sudo


Example Playbook
----------------

```
- hosts: servers
  tasks:
    - name: "Include ansible_account"
      include_role:
        name: ansible_account
      vars:
        ansible_acciunt_authorized_keys:
          - "ssh-ed25519 <public_key> <user>"
```
License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
