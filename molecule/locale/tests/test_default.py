import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_locale_installed(host):
    locale_package_name = "locales"
    locale_package = host.package(locale_package_name)
    assert locale_package.is_installed

