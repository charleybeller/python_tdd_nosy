# Test Driven Development in Python with Nosy
Example of using Python with Nosy for test driven development

## Create a virtual environment
`$ python3 -m venv nosy_env`

## Activate the virtual environment
`$ source nosy_env/bin/activate`

## Install the requirements
These requirements include the test runner `nose`, the colorizer `rednose`, and `nosy` which automates watching files and running tests on every change.
`(nosy_env)$ pip install -r requirements.txt`


## Project setup
The project is organized to have test files in app/test/
Implementation code is in app/local/

## Nosy configuration
Nosy is configured in the `setup.cfg` file which provides the base_path of the project, the path where tests are stored, and glob_patterns and extra_paths to let nosy know which files to watch for changes. Right now all .py files in both app/test/ and app/local/ will trigger a test run on change, as will the setup.cfg file.


## Unittest
Unittest is an out-of-the-box testing framework included with Python. Group tests into classes (typically one per module) and name each testing method with the prefix `test_`.
You can use the setUp(self) method to add testing fixtures.
TestCase.assertEqual() is the basic test assertion. More assertion methods can be found at [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)