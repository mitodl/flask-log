Flask-Log
---------

.. image:: https://img.shields.io/travis/mitodl/flask-log.svg
    :target: https://travis-ci.org/mitodl/flask-log
.. image:: https://img.shields.io/coveralls/mitodl/flask-log.svg
    :target: https://coveralls.io/r/mitodl/flask-log
.. image:: https://img.shields.io/github/issues/mitodl/flask-log.svg
    :target: https://github.com/mitodl/flask-log/issues
.. image:: https://img.shields.io/pypi/dm/flask-log.svg
    :target: https://pypi.python.org/pypi/flask-log/0.1.0
.. image:: https://img.shields.io/pypi/v/flask-log.svg
    :target: https://pypi.python.org/pypi/flask-log/0.1.0
.. image:: https://img.shields.io/badge/license-BSD-blue.svg
    :target: https://github.com/mitodl/flask-log/blob/master/LICENSE

This is a handy flask extension for setting up logging for your
application that is super simple to setup.  A basic example is:

.. code-block:: python

  import flask
  from flask.ext.log import Logging

  app = flask.Flask(__name__)
  app.config['FLASK_LOG_LEVEL'] = 'DEBUG'
  flask_log = Logging(app)
  

  app.logger.debug('Testing a debug message')

So the level of logging is configurable through regular flask
configuration methods.  Additionally, since we are setting up the root
logger, you can use whatever logger you want as you aren't restricted
to the flask application logger. i.e. something like:

.. code-block:: python

  import logging

  log = logging.getLogger('my-special-logger')
  log.critical('Oh my!')

will also keep the formatter and level if the extensions has been
initialized anywhere.

Features
========

- Sets up syslog handling to either ``/dev/log``, ``/var/run/syslog``,
  or ``127.0.0.1`` on UDP port 514 depending on what is available.
- Adds a log formatter packed with information and by default produces
  output like: ``[2015-03-31 18:10:17,816] CRITICAL 42282 [__main__]
  example.py:7 - [my_hostname] - Hi``
- Full code coverage
- The log formatter can be overidden with something like:

  .. code-block:: python

    flask_logger = Logging(app)
    flask_logger.set_formatter('Log message follows: %(message)s')

Links
`````

- `documentation <https://github.com/mitodl/flask-log/blob/master/README.rst>`_
- `development version <https://github.com/mitodl/flask-log/archive/master.tar.gz#egg=flask-log-dev>`_
