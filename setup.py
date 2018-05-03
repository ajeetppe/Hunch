from setuptools import setup, find_packages

import hunchsdk

VERSION = hunchsdk.__version__

setup(name='hunch',
      version=VERSION,
      description='Hunch Server and Hunch SDK',
      author='ML Platform Dev Team @Flipkart',
      license='Apache-2.0',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=['requests', 'retrying', 'simplejson']
      )
