"""
Validate log configuration
"""
import logging
import os
import unittest

import flask
# pylint: disable=no-name-in-module,import-error
from flask.ext.log import Logging
import mock

TEST_LOG_LEVEL = 'DEBUG'
TEST_FORMATTER = 'stuff'


class TestLogConfiguration(unittest.TestCase):
    """
    Make sure we are setting up logging like we expect.
    """

    def setUp(self):
        """Setup a fresh flask app to work on for each test"""
        self.app = flask.Flask(__name__)
        self.app.debug = True

    def test_config_log_level(self):
        """Validate that log level can be set with application"""
        root_logger = logging.getLogger()
        log_level = root_logger.level
        self.assertEqual(logging.NOTSET, log_level)

        self.app.config['FLASK_LOG_LEVEL'] = TEST_LOG_LEVEL
        Logging(self.app)
        root_logger = logging.getLogger()
        self.assertEqual(root_logger.level, getattr(logging, TEST_LOG_LEVEL))

    def test_bad_log_level(self):
        """
        Set a non-existent log level and make sure we raise properly
        """
        root_logger = logging.getLogger()
        log_level = root_logger.level
        self.assertEqual(logging.NOTSET, log_level)

        self.app.config['FLASK_LOG_LEVEL'] = 'Not a real thing'
        with self.assertRaisesRegexp(ValueError, 'Invalid log level.+'):
            Logging(self.app)

    def test_no_log_level(self):
        """
        Make sure we leave things alone if no log level is set.
        """
        self.app.config['FLASK_LOG_LEVEL'] = None
        flask_log = Logging(self.app)

        self.assertEqual(logging.NOTSET, flask_log.log_level)

    def test_syslog_devices(self):
        """Test syslog address handling and handler"""
        for log_device in ['/dev/log', '/var/run/syslog', '']:
            root_logger = logging.getLogger()
            # Nuke syslog handlers from init_app
            syslog_handlers = []
            for handler in root_logger.handlers:
                if isinstance(handler, logging.handlers.SysLogHandler):
                    syslog_handlers.append(handler)
            for handler in syslog_handlers:
                root_logger.removeHandler(handler)

            real_exists = os.path.exists(log_device)

            def mock_effect(*args):
                """Contextual choice of log device."""
                # pylint: disable=cell-var-from-loop
                return args[0] == log_device

            # Call so that it will think /dev/log exists
            with mock.patch('os.path') as os_exists:
                os_exists.exists.side_effect = mock_effect
                if not real_exists and log_device != '':
                    with self.assertRaises(Exception):
                        Logging(self.app)
                else:
                    Logging(self.app)
                    syslog_handler = None
                    for handler in root_logger.handlers:
                        if isinstance(handler, logging.handlers.SysLogHandler):
                            syslog_handler = handler
                    self.assertIsNotNone(syslog_handler)
                    if log_device == '':
                        self.assertEqual(
                            syslog_handler.address, ('127.0.0.1', 514)
                        )
                    else:
                        self.assertEqual(syslog_handler.address, log_device)

    def test_set_formatter(self):
        """Test that we can override the default formatter"""
        flask_log = Logging(self.app)
        flask_log.set_formatter(TEST_FORMATTER)
        root_logger = logging.getLogger()
        # Make fake record and assert we are formatting properly
        log_record = logging.LogRecord(
            'a', logging.CRITICAL, 'a.py', 1, 'things', None, None
        )
        # Format should ignore message and everything, and no matter
        # what gets passed in we should just get 'stuff' back.
        for handler in root_logger.handlers:
            self.assertEqual(
                handler.formatter.format(log_record),
                TEST_FORMATTER
            )
