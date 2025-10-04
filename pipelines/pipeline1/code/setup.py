from setuptools import setup, find_packages
setup(
    name = 'pipeline1',
    version = '1.0',
    packages = find_packages(include = ('pipeline1*', )) + ['prophecy_config_instances.pipeline1'],
    package_dir = {'prophecy_config_instances.pipeline1' : 'configs/resources/pipeline1'},
    package_data = {'prophecy_config_instances.pipeline1' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.4'],
    entry_points = {
'console_scripts' : [
'main = pipeline1.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
