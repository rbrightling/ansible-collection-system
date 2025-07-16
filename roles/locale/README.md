Locale
======

Manage the system locale.

Requirements
------------

None

Role Variables
--------------

```
# defaults file for locale

# The locale LANG setting
locale_lang: "en_GB.UTF-8"

# The locale LANGUAGE setting
locale_language: "en_GB:en"

# List of locale to generate
locale_enable_locale:
  - "{{ locale_lang }}"
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: servers
  tasks:
    - name: include role rbrightling.system.locale
      include_role:
        name: rbrightling.system.locale
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
