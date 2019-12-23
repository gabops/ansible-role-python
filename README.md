gabops.python
=========
[![Build Status](https://travis-ci.org/gabops/ansible-role-python.svg?branch=master)](https://travis-ci.org/gabops/ansible-role-python)

Installs Python from source code.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| python_version | 3.8.1 | Defines the Python version to be installed. |
| python_installation_path | /opt/python/3.8.1 | Defines the path where the source code will be installed. Note that by default this does not necessarly means that the Python binaries will be installed here as well. |
| python_build_requirements | "" | Defines the list of packages to be installed in order to build the source code. Note that this role handles its own list of packages already, however, this options exists for allowing you to define your own list of packages if required. |
| python_install_build_requirements | true | Defines if the role should install building requirements (the internal or the ones specified by you in `python_build_requirements`). |
| python_configure_parameters | ['--with-ensurepip=install'] | Defines the list of parameters to be passed to the `./configure` script. |
| python_make_target | altinstall | Defines the make target. I **strongly** recomend to avoid to change this value unless you know what you are doing otherwise you can break your system. |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: gabops.python
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
