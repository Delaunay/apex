from setuptools import setup, find_packages

setup(
    name='apex',
    version='0.1',
    packages=find_packages(exclude=('build', 
                                    'csrc', 
                                    'include', 
                                    'tests', 
                                    'dist',
                                    'docs',
                                    'tests',
                                    'examples',
                                    'apex.egg-info',)),
    description='PyTorch Extensions written by NVIDIA',
)
