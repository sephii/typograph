#!/usr/bin/env python
from setuptools import find_packages, setup

tests_require = [
    'pytest>=2.7.3',
]

install_requires = [
    'beautifulsoup4>=4.0.0',
    'six>=1.6.0',
]


setup(
    name='typograph',
    version='0.1.0',
    packages=find_packages(exclude=('tests', 'tests.*')),
    description='Automatically fix typography mistakes that are commonly done when writing content on the web',
    author='Sylvain Fankhauser',
    author_email='sylvain.fankhauser@gmail.com',
    url='https://github.com/sephii/typograph',
    install_requires=install_requires,
    license='bsd',
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    include_package_data=False,
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
