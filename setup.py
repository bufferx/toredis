#!/usr/bin/env python
"""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

KEYWORDS = ['tornado', 'redis', 'hiredis', 'tornado redis']

DESCRIPTION = ('Yet Another toredis, Client Pool Supported. '
               'Forked From https://github.com/mrjoes/toredis/')

setup(
    name='yatoredis',
    version='0.1.3',
    description=DESCRIPTION,
    keywords=KEYWORDS,
    author='ZY ZHANG',
    author_email='idup2x@gmail.com',
    url="http://github.com/bufferx/toredis/",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    packages=['toredis'],
    test_suite='tests.all_tests',
    install_requires=['tornado', 'hiredis'],
)
