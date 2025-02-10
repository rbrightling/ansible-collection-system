import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ansible_user_created(host):
    ansible_account_name = "ansible"
    ansible_account = host.user(ansible_account_name)
    assert ansible_account.exists
