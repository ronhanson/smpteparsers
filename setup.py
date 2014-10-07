from setuptools import setup, find_packages
import os

if os.environ.get('USER', '') == 'vagrant':
    del os.link

setup(
    name='smpteparsers',
    version=open('VERSION.txt').read().strip(),
    author='Arts Alliance Media',
    author_email='dev@artsalliancemedia.com',
    url='http://www.artsalliancemedia.com',
    packages=find_packages(where='.', exclude=["*.tests", "*.tests.*", "tests.*", "tests", "libs"]),
    description='A set of python parsers for various SMPTE standards.',
    long_description=open('README.md').read().strip(),
    install_requires=[r.strip() for r in open('requirements.txt').readlines()],
    extras_require={"docs": ("sphinx",)},
)
