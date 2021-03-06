# Test Driven Development in Python with Nosy
This repo provides and example project set up for Test Driven Development (TDD) in Python with the tool `nosy`.

The project is organized to have test files in [app/test/](./app/test/)

Implementation code is in [app/local/](./app/local)

To start clone this repo from [https://github.ibm.com/cebeller/python_tdd_nosy](https://github.ibm.com/cebeller/python_tdd_nosy) and navigate to the repo directory.

`$ git clone git@github.ibm.com:cebeller/python_tdd_nosy.git`
`$ cd python_tdd_nosy`

## Create a virtual environment
The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

More information at
[https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)

`$ python3 -m venv nosy_env`

## Activate the virtual environment

`$ source nosy_env/bin/activate`

Once a virtual environment has been created, it can be “activated” using a script in the virtual environment’s binary directory. The invocation of the script is platform-specific (<venv> must be replaced by the path of the directory containing the virtual environment):

| Platform | Shell | Command to activate virtual environment |
|--|--|--|
| POSIX | bash/zsh | `$ source <venv>/bin/activate` |
| | fish | `$ source <venv>/bin/activate.fish` |
| | csh/tcsh | `$ source <venv>/bin/activate.csh` |
| | PowerShell Core | `$ <venv>/bin/Activate.ps1` |
| Windows | cmd.exe | `C:\> <venv>\Scripts\activate.bat` |
| | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1` |


## Install the requirements
`pip` is the most popular tool for installing Python packages, and the one included with modern versions of Python.

It provides the essential core features for finding, downloading, and installing packages from PyPI and other Python package indexes, and can be incorporated into a wide range of development workflows via its command-line interface (CLI).

More information at
[https://packaging.python.org/key_projects/#pip](https://packaging.python.org/key_projects/#pip)

We'll use `pip` to install a list of requirements from a requirement.txt file.
These requirements include the test runner `nose`, the colorizer `rednose`, and `nosy` which automates watching files and running tests on every change.
`(nosy_env)$ pip install -r requirements.txt`


## Nosy configuration
Nosy is configured in the `setup.cfg` file which provides the base_path of the project, the path where tests are stored, and glob_patterns and extra_paths to let nosy know which files to watch for changes. Right now all .py files in both app/test/ and app/local/ will trigger a test run on change, as will the setup.cfg file.


## Unittest
Unittest is an out-of-the-box testing framework included with Python. Group tests into classes (typically one per module) and name each testing method with the prefix `test_`.
You can use the `setUp(self)` method to add testing fixtures.
`TestCase.assertEqual(expected, actual)` is the basic test assertion. More assertion methods can be found at [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)

## Running `nosy`
When developing, I'll open a dedicated terminal window to run continuous testing using `nosy` and edit my files in my text editor or IDE of choice (e.g. PyCharm, emacs, vim, etc.)

Make sure to activate the virtual environment before invoking `nosy`!

`$ cd python_tdd_nosy`
`$ source nosy_env/bin/activate`
`$ nosy`