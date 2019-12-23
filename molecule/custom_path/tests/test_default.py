import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_python_version(host):
    c = host.run('/opt/Python/installations/3.8.1/bin/python3.8 --version')

    assert '3.8.1' in c.stdout
