import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_aide_installed(host):
    sudo_package_name = "aide"
    sudo_package = host.package(sudo_package_name)
    assert sudo_package.is_installed


def test_aide_db(host):
    aide_db = host.file("/var/lib/aide/aide.db.gz")
    assert aide_db.mode == 0o600
    assert aide_db.user == "root"
    assert aide_db.group == "root"


def test_aide_conf(host):
    aide_conf = host.file(_get_aide_conf_path(host.system_info.distribution))
    assert aide_conf.mode == 0o600
    assert aide_conf.user == "root"
    assert aide_conf.group == "root"


def _get_aide_conf_path(host_distro):
    return {
        "debian": "/etc/aide/aide.conf",
    }.get(host_distro, "/etc/aide.conf")
