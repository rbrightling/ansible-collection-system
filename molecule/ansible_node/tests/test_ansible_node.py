import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_python_installed(host):
    python_package_name = _get_distro_python_package_name(
        host.system_info.distribution, host.system_info.release)
    python_package = host.package(python_package_name)
    assert python_package.is_installed


def test_python_command(host):
    host.exists("python")


def _get_distro_python_package_name(host_distro, release):

    if host_distro == "debian":
        if int(release) >= 10.0:
            return "python3-minimal"
        else:
            return "python-minimal"
    elif host_distro == "centos":
        if int(release) >= 8:
            return "python36"
        else:
            return "python"
    return "python"
