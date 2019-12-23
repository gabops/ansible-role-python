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
| python_source_installation_path | /opt/Python/source/3.8.1 | Defines the path where the source code will be installed. |
| python_custom_installation_path | "" | Defines a custom installation path to install Python in. Note that this parameter is not required. See Notes. |
| python_build_requirements | "" | Defines the list of packages to be installed in order to build the source code. Note that this role handles its own list of packages already, however, this options exists for allowing you to define your own list of packages if required. |
| python_install_build_requirements | true | Defines if the role should install building requirements (the internal or the ones specified by you in `python_build_requirements`). |
| python_configure_parameters | ['--with-ensurepip=install'] | Defines the list of parameters to be passed to the `./configure` script. |
| python_make_target | altinstall | Defines the make target. I **strongly** recomend to avoid to change this value unless you know what you are doing otherwise you can break your system. |

**Notes:**

- As you can see, the default value for `python_make_target` is `altinstall`. This means that by default Python will be installed in **/usr/local/lib/Python\*** and the binary in **/usr/local/bin/python\***. For changing this behaviour and installing Python in the directory defined in `python_custom_installation_path` you can use for example:

```yaml
python_custom_installation_path: /opt/installations/python3

python_configure_parameters:
  - --with-ensurepip=install
  - --prefix={{ python_custom_installation_path }}"

python_make_target: install
```
Bare in mind that with the configuration in the example you will need to configure the PATH environment variable in order to add `/opt/installations/python3/bin` to it.

Dependencies
------------

None.

Example Playbook
----------------

Simple installation:
```yaml
- hosts: servers
  roles:
    - role: gabops.python
```
Or go crazy with several Python versions:
```yaml
- hosts: servers
  tasks:
    - name: Install Python
      include_role:
        name: gabops.python
      vars:
        python_version: "{{ item.version }}"
        python_installation_path: "{{ item.path }}"
      loop:
        - version: 3.8.1
          path: /opt/Python/3.8.1

        - version: 3.7.6
          path: /opt/Python/3.7.6
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
