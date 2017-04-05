# -*- coding: utf-8 -*-
# from distutils.core import setup
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='AIST_novel_downloader',
    version='0.1',
    description='novel downloader service',
    long_description=long_description,
    author='winxos',
    author_email='winxos@hotmail.com',
    url='https://github.com/winxos/novel_downloader',  # use the URL to the github repo
    download_url='https://github.com/winxos/novel_downloader',
    keywords=['novel', 'winxos', 'aist'],  # arbitrary keywords
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['aist_novel_grab'],
    packages=find_packages(),
    package_dir={'novel_downloader': 'novel_downloader'},
)
