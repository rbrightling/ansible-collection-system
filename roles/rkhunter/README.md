RkHunter
========

Install and configure Rootkit Hunter (rkhunter) on a host system and create the initial file properties database.

Requirements
------------

Supported OS's:
  - Debian 10
  - RedHat 8

Role Variables
--------------

```yaml
# Run rkhunter update
rkhunter_update: true

# Force propupd to be run
rkhunter_force_propupd: false

# Config options
# ==============

# Mirror options
# --------------

# Rotate the mirror list used else treat it as a priority list
rkhunter_rotate_mirrors: true

# Update the mirrors list on --update
rkhunter_update_mirrors: true
# true: update the mirrors file
# false: mirrors file has to be updated manually, useful for local mirrors.

# Which mirrors are to be used when running update
rkhunter_mirrors_mode: 0
# 0: use any mirror
# 1: only use local mirrors
# 2: only used remote mirrors

# Mail options
# ------------

# Addresses to email on warnings, multiple addresses can be given with a list
rkhunter_mail_on_warning: null

# Command to use to send mail for rkhunter_mail_on_warning
rkhunter_mail_cmd: 'mail -s "[rkhuner] Warnings found for ${HOST_NAME}"'

# Language options
# ----------------

# Language to use
rkhunter_language: en

# Specify the language files to update, null to update all.
rkhunter_update_lang: "{{ rkhunter_language }}"

# Test Options
# ------------

# Specify the test to run with rkhunter.
rkhunter_enable_tests: ALL
rkhunter_disable_tests:
  - suspscan 
  - hidden_ports 
  - hidden_procs 
  - deleted_files 
  - packet_cap_apps 
  - apps

# Specify the command to use for file property hash value checks.
rkhunter_hash_cmd: "SHA256"

# Field from the hash_cmd which contains the hash value.
rkhunter_hash_fld_idx: null

# Package manager to use to optain file property information if available, otherwise HASH_CMD is used.
rkhunter_pkgmgr: "{{ rkhunter__pkgmgr }}"
# Debian: null
# RedHat: RPM

# Given paths to ignore for changes from the package manager. Files will be checked with the normal method instead.
# Only used if rkhunter_pkgmgr is set
rkhunter_pkgmgr_no_vrfy: null

# Solaris option
rkhunter_use_sunsum: null

# Ignore any listed path prelink dependency errors; a warning will be given if any listed paths don't create the error.
rkhunter_ignore_prelink_dep_err: null

# Specify the commands, directories or file paths to include or exclude from the file property checks.
rkhunter_user_fileprop_files_dirs: null
rkhunter_exclude_user_fileprop_files_dirs: null
# Example:
#   - top
#   - /usr/local/sbin
#   - /etc/rkhunter.conf
#   - /etc/rkhunter.d/*
#   - /opts/ps*

# Allow the use of '**' to recursively checking directories.
# for example with fileprop_files_dirs: /etc/**/*.conf, would find all .conf files in /etc/ and any level of subdirectory.
rkhunter_globstar: false

# Perform a thorough check with Phalanx2 else just a basic check
rkhunter_phalanx2_dirtest: false

# Set rkkhunter to search for filenames in all directories
# NOTE: Shouldn't be enabled by default
rkhunter_scanrootkitmode: null #THOROUGH

# List of tests for the unhide command to use.
rkhunter_unhide_tests: sys

# Set options for the unhide-tcp command
rkhunter_unhidetcp_opts: null

# Used to check for empty or missing log files
rkhunter_empty_logfiles: null
rkhunter_missing_logfiles: null

# Log options
# -----------

# Option to append to the rkhunter log 
rkhunter_append_log: true

# Copy a timestamped log when finishes with errors or warnings
rkhunter_copy_log_on_error: 0

# Enable rkhunter to log start and finish times as well as warning messages with syslog.
rkhunter_use_syslog: "authpriv.warning"

# SSH options
# -----------

# Check for PermitRootLogin in sshd_config
rkhunter_allow_ssh_root_user: false
# true/yes: PermitRootLogin is allowed
# false/no: PermitRootLogin is not allowed
# unset: If not set in sshd_config and avoid warning message

# Check if version 1 of ssh is allowed in sshd_config
rkhunter_allow_ssh_prot_v1: 2
# 0: not allowed
# 1: allowed
# 2: Ignore if not set in sshd_config

# Directory for ssh config: rkhunter can normally work this out so doesn't need setting
rkhunter_ssh_config_dir: null

# Output options
# --------------

# Detect if x is available to use second colour set.
rkhunter_auto_x_detect: true

# Set to use the second colour set. 
rkhunter_color_set2: null

# Set whitelisted items in white instead of green.
rkhunter_whitelisted_is_white: null

# Show a summary of the number of warnings at the end of the run.
rkhunter_show_summary_warnings_number: null

# Set where the summary scan time is displayed
rkhunter_show_summary_time: 3
# 1: only on screen
# 2: only in logs
# 3: both screen and logs

# Whitelist options
# -----------------

# whitelist files and directories from existing or not existing.
rkhunter_existwhitelist: "{{ rkhunter__existswhitelist }}"
# Debian: null
# RedHat:
#   - "/bin/ad"
#   - "/var/log/pki-ca/system" 
#   - "/var/log/pki-pki-comat/ca/system"
#   - "/var/log/pki-pki-comat/kra/system"
#   - "/usr/bin/GET"
#   - "/usr/bin/whatis"

# Whitelists various attributes of the specified files.
rkhunter_attrwhitelist: null

# Allow the specified files to have 'other' write set permissions.
rkhunter_writewhitelist: null

# Whitelist the following files to allowed to be scripts
rkhunter_scriptwhitelist: "{{ rkhunter__scriptwhitelist }}"
# Debian:
#   - "/usr/bin/egrep"
#   - "/usr/bin/fgrep"
#   - "/usr/bin/which"
#   - "/usr/bin/ldd"
#   - "/usr/sbin/adduser"
# RedHat:
#   - "/usr/bin/whatis"
#   - "/usr/bin/ldd"
#   - "/usr/bin/groups"
#   - "/usr/bin/GET"

# Whitelist the following files to have the immutable attribute set.
rkhunter_immutwhitelist: null

# Set to reverse the immutable-bit test.
rkhunter_immutable_set: false

# Ignore changes to inodes value for file properties.
rkhunter_skip_inode_check: false

# Allow for hidden directories or files to be whitelisted
rkhunter_allowhiddendir: null
rkhunter_allowhiddenfile: "{{ rkhunter__allowhiddenfile }}"
# Debian: null
# RedHat:
#   - "/etc/.updated"
#   - "/usr/share/man/man5/.k5login.5.gz"
#   - "/usr/share/man/man5/.k5identity.5.gz"
#   - "/usr/share/man/man1/..1.gz"

# Allow the given process to use deleted files. Can be given as just the program or a colon list of specified files
rkhunter_allowprocdelfile: null
# Example:
#   - /sbin/cardmgr
#   - /usr/libexec/gconfd-2:/tmp/acb:/var/cmp/xyz
#   - /usr/sbin/mysqld:/tmp/ib*

# Allow the given processes to listen on any network interface
rkhunter_allowproclisten: null

# Allow specified network interfaces to be in promiscuous mode.
rkhunter_allowpromiscif: null
# Example:
#   - eth0

# Whitelist files and directories from rootkit scanners
rkhunter_rtkt_file_whitelist: null
rkhunter_rtkt_dir_whitelist: null
# Example:
#   - /etc/rc.local         
#   - /etc/rc.local:hdparm 
#   - /etc/rc.local: 

# Whitelist shared library files
rkhunter_shared_lib_whitelist: null

# How rkhunter should scan the /dev/ directory. 
rkhunter_scan_mode_dev: THOROUGH # THOROUGH or LAZY

# Whitelist specified files in the /dev directory
rkhunter_allowdevfile: null
# Example:
#   - /dev/sdm/pulse-shm-*

# Allow given process paths to use shared memory segments
rkhunter_allowipcproc: null

# Allow given PID's to used shared memory segments
rkhunter_allowipcpid: null

# Allow given user accounts to use shared memory segments
rkhunter_allowipcuser: null

# Maximum allowed shared memory segment size
rkhunter_ipc_seg_size: 1048576 # 1M

# Inetd options
# -------------

# Location of the inetd configuration file.
rkhunter_inetd_conf_path: null
# Example: /etc/inetd.conf

# Allowed inetd services
rkhunter_inetd_allowed_svc: null
# Example:
#   - echo

# XINETD
# ------

# The xinetc path for rkhunter to use
rkhunter_xinetd_conf_path: null # /etc/xinetd.conf

# List of allowed xinetd services by paths
rkhunter_xinetd_allowed_svc: null
# Example:
#   - /etc/xinetd.d/echo

# List of allowed applications
rkhunter_app_whitelist: null
# application names can also be specified with specific versions by separating it with a colon
# Example:
#   - openssl:0.9.7d
#   - gpg
#   - httpd:1.3.29

# Scan given directories for suspicious files.
# suspscan is not enabled by default due to likely false positives and resource usage.
rkhunter_suspscan_dirs:
  - "/tmp"
  - "/var/tmp"
# Add any directories webserver users have write access.

# Location of temporary files used by the suspscan test.
rkhunter_suspscan_temp: "/dev/shm"

# Maximum size of files to be scanned by suspscan in bytes
rkhunter_suspscan_maxsize: 1024000

# suspscan test score threshold to hit before reporting
rkhunter_suspscan_thresh: 200

# Whitelist files from the suspscan
rkhunter_suspscan_whitelist: null

# Whitelist ports to listen on
rkhunter_port_whitelist: null
# Example:
#   - TCP:2001
#   - UDP:32011

# Whitelist application paths for specific ports
rkhunter_port_path_whitelist: null
# Example:
#   - /usr/bin/squid
#   - /usr/bin/squid::TCP:3801

# OS Options
# ----------

# Location of the OS release file; if not set rkhunter will try to detect it self.
rkhunter_os_version_file: null

# Warn if OS information is changed:
rkhunter_warn_on_os_change: true

# Run a file property update on OS change detection
rkhunter_updt_on_os_change: false

# Specify the location of startup file, by default rkhunter can try to determine them.
rkhunter_startup_paths: null 
# Example:
#   - /etc/init.d
#   - /etc.rc.local

# Location of file containing user account passwords, by default rkhunter can try to determine it.
rkhunter_password_file: null # /etc/shadow

# List of accounts whitelisted for a UID value of 0 as root equivalents.
rkhunter_uid0_accounts: null
# Example:
#   - toor
#   - rooty

# Allowed list of account to have not password
rkhunter_pwdless_accounts: null

# Syslog configuration paths, by default rkhunter can try to determine it.
rkhunter_syslog_config_file: null

# Allow syslog remote logging
rkhunter_allow_syslog_remote_logging: false

# Directory containing Linux kernel modules, if not set rhhunter will try to determine it.
rkhunter_modules_dir: null

# Command Options
# ---------------

# Force rkhunter to use supplied scripts for the 'stat' and 'readline' commands.
rkhunter_stat_cmd: null
rkhunter_readlink_cmd: null

# rkhunter will try and change epoach seconds to datetime using date. 
rkhunter_epoch_date_cmd: null
# NONE: only epoch seconds will be shown
# PERL: force rhhunter to use the perl command if present

# Program to use for checking and getting updates
rkhunter_web_cmd: curl

# Lockfile options
# ----------------

# Use a locking file to avoid rkhunter running multiple simultaneous scans
rkhunter_use_locking: true

# Directory of the lock file, rkhunter will try to determine this if not set
rkhunter_lockdir: null

# Time to wait for the lock to be released before timing out
rkhunter_lock_timeout: 300

# Show messages when waiting to release lock
rkhunter_show_lock_msgs: true

# Location Paths
# --------------

# Directory to be used for temporary files used by rkhunter
rkhunter_tmpdir: "{{ rkhunter__tmpdir }}"
# debian: /var/lib/rkhunter/tmp
# redhat: /var/lib/rkhunter

# Location of the log file
rkhunter_logfile: "{{ rkhunter__logfile }}"
# debian: /var/log/rkhunter.log
# redhat: /var/log/rkhunter/rkhunter.log

# Where rkhunter stores it's database
rkhunter_dbdir: "{{ rkhunter__dbdir }}"
# debian: /var/lib/rkhunter/db
# redhat: /var/lib/rkhunter/db

# Location of the rkhunter scripts
rkhunter_scriptdir: "{{ rkhunter__scriptdir }}" 
# debian: /usr/share/rkhunter/scripts
# redhat: /usr/share/rkhunter/scripts

# List of binary directories. By default the root users PATH environment will be used. 
# Options with + prepended will be prepended to the list
rkhunter_bindir: null
# Example:
#   - /bin
#   - +/usr/local/bin

# rkhunter install directory
rkhunter_installdir: "/usr"
```

Dependencies
------------

- None

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - name: include rbrightling.system.rkhunter
       include_role:
         name: rbrightling.system.rkhunter
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
