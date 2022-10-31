from importlib.metadata import entry_points
from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Clean folder script',
    url='https://github.com/dzvenyslavavovk/GOIT_python_core_module7_hw',
    author='Dzvenyslava Vovk',
    author_email='dzvinavovk.25@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':['clean-folder=clean_folder.main:main_func']}
)
