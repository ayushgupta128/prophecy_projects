from setuptools import setup, find_packages
setup(
    name = 'pipe1',
    version = '1.0',
    packages = find_packages(include = ('pipe1*', )) + ['prophecy_config_instances.pipe1'],
    package_dir = {'prophecy_config_instances.pipe1' : 'configs/resources/pipe1'},
    package_data = {'prophecy_config_instances.pipe1' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.4'],
    entry_points = {
'console_scripts' : [
'main = pipe1.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
