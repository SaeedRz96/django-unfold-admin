from setuptools import setup, find_packages

# Read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    

setup(
    name='django-unfold-admin',
    version='0.1.0',
    url='https://github.com/SaeedRz96/django-unfold-admin',
    author='Saeed Ramazani',
    author_email='saeedramezani75@gmail.com',
    description='RTL Unfold Django Admin Panel Theme',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    packages=find_packages(),  
    include_package_data=True,  
    install_requires=[],
)