AIDE
====

Install and manage AIDE (Advanced Intrusion Detection Environment) on a host system and creates a aide file database.

Seperate tasks can be used to backup and use the aide database to check for changes.

Configured with a default set of rules and the ability add addition rules and rule groups.

*DEBIAN:* Comes with a number of changes to the way it is run which are ignored by this role; while combatability is 
maintained. Files from aide.conf.d will be ignored and the daily cronjon is disabled by default. 

*NOTE:* `aide_force_update_db` and `aide_force_init_db` can be passed to ansible to run the relevant aide commend. 

Requirements
------------

Supported OS's:
  - Debian 10
  - RedHat 8

Role Variables
--------------

```
# Config options
# options for storing the aide database. 
aide_database: "file:/var/lib/aide/aide.db{{ '.gz' if aide_gzip_dbout else '' }}"
aide_database_out: "file:/var/lib/aide/aide.db.new{{ '.gz' if aide_gzip_dbout else '' }}"
aide_database_new: "{{ aide_database_out }}"

# Outputs to write to, can be given as a single string or list
aide_report_url:
  - "file:/var/log/aide/aide.log"
  - stdout

# gzip the output database
aide_gzip_dbout: true

# The level of messages that is output. This value can be 0-255 inclusive.
aide_verbose: 5

# Whether to base16 encode the checksums in the report or not. Default uses base644.
aide_report_base16: false

# Give a summary in the report.
aide_summarize_changes: true

# Attributes added to the final report in verbose 2 or higher. Disable with 'E' or false.
aide_database_attrs: "sha256+sha512+rmd160+crc32+tiger"

# Group files in the report by added, removed and changed or not.
aide_grouped: true

# Add  the AIDE version and the time of database generation as comments to the database file or not
aide_database_add_metadata: null

# Report added files (verbose level >= 2) and their details (verbose level >=7) in initialization mode
aide_report_detailed_init: null

# Suppress  report  output if no differences to the database have been found or not.
aide_report_quiet: null

# The prefix to strip from each file name in the file system before applying the rules and writing to database.
aide_root_prefix: null

# Whether to check ACLs for symlinks or not.
aide_acl_no_symlink_follow: null

# Whether to warn about dead symlinks or not.
aide_warn_dead_symlinks: null

# Special group definition that lists attributes whose addition is to be ignored in the final report.
report_ignore_added_attrs: null
report_ignore_remote_attrs: null
report_ignore_changed_attrs: null

# The value of config_version is printed in the report and also printed to the database.
aide_config_version: null

# Rules groups 
aide_rule_groups: {}
# Example:
#   GROUP1: "option1+option2"

# Rules
aide_rules: {}
# Example:
#   "/directory": RULE_GROUP
#   "/file/apt$": RULE_GROUP

# Update the aide database
aide_force_update_db: false
aide_force_init_db: false

# Enable the daily cronjob
# Debian only
aide_daily_cron: false # true/false, null to not manage
```

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: servers
  tasks:
    - name: include rbrightling.system.aide
      include_role:
        name: rbrightling.system.aide
```
License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
