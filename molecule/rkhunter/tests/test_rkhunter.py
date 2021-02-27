import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_rkhunter_installed(host):
    package_name = "rkhunter"
    package = host.package(package_name)
    assert package.is_installed


def test_rkhunter_conf(host):
    aide_conf = host.file("/etc/rkhunter.conf")
    assert aide_conf.mode == 0o640
    assert aide_conf.user == "root"
    assert aide_conf.group == "root"
