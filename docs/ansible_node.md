Ansible Node
============

![Test Ansible Role](https://github.com/rbrightling/ansible-ansible_node/workflows/Test%20Ansible%20Role/badge.svg) [![Ansible Galaxy](http://img.shields.io/badge/galaxy-rbrightling.ansible_node-660198.svg?style=flat)](https://galaxy.ansible.com/rbrightling/ansible_node)

Install the basic requirements to manage a node with ansible using raw commands.
Sets the /usr/bin/python to python3 is not found using alternatives

CentOS/Redhat:
- Install python
- Checks for SELinux and installs python selinux supports

Debian:
- Installs minimal python with apt support

Requirements
------------

OS Support:
  - CentOS
  - Debian
  - RedHat

Role Variables
--------------

```yaml
# Python path to test for
ansible_node_python_path: "/usr/bin/python3"

# Base packages to install
ansible_node_python_packages: "{{ ansible_node__python_packages }}"
# CentOS/RedHat:
#   - python3
# Debian:
#   - python3-minimal
#   - python3-simplejson

# Python package to install to manage apt on Debian based distributions.
ansible_node_python_apt_package: "python3-apt"

# Python selinux package to install if detected (CentOS/RedHat)
ansible_node_python_selinux_package: "python3-libselinux"
```

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: Include Ansible Node role
      include_role:
        name: "ansible_node"
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
