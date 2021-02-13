import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_aide_conf(host):
    aide_conf = host.file("/etc/hosts.example")
    assert aide_conf.mode == 0o644
    assert aide_conf.user == "root"
    assert aide_conf.group == "root"
