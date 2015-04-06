"""
Flask-Log
---------
This is a handy flask extension for setting up logging for your
application that is super simple to setup.

Links
`````

- `documentation
   <https://github.com/mitodl/flask-log/blob/master/README.rst>`_
- `development version
  <https://github.com/mitodl/flask-log/archive/master.tar.gz#egg=flask-log-dev>`_
"""
from setuptools import setup

with open('README.rst') as readme:
    README = readme.read()

with open('test_requirements.txt') as test_reqs:
    TESTS_REQUIRE = test_reqs.readlines(),


setup(
    name='flask-log',
    version='0.1.0',
    url='http://github.com/mitodl/flask-log',
    license='BSD',
    author='MIT ODL Engineering',
    author_email='odl-engineering@mit.edu',
    description='Configure logging in flask applications',
    long_description=__doc__,
    py_modules=['flask_log'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    tests_require=TESTS_REQUIRE,
    test_suite="nose.collector",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
