# -*- coding: utf-8 -*-

"""
:copyright: © 2018 by KeisukeYamashita.
:license: MIT, see LICENSE for more details.
"""

import logging
from unittest import TestCase
from pyplelogger.pyplelogger import Logger, IncrementalLoggerLevel
from logging import Formatter

class TestLogger(TestCase):
    
    def setUp(self):
        self.log = Logger("setUp")
    
    def test_default_log_level(self):
        self.log.set_default_log_level(logging.DEBUG)
        new_logger = Logger("default_log_level")
        self.assertEqual(new_logger.default_LOG_LEVEL, logging.DEBUG)
        self.assertEqual(self.log.default_LOG_LEVEL, new_logger.default_LOG_LEVEL)
        self.log.set_default_log_level(logging.INFO)

    def test_default_format(self):
        default_format = self.log.default_FORMAT

        format = '%(levelname)s %(asctime)s %(message)s'
        Logger.set_default_format(format)
        logger = Logger("default_format")

        self.assertEqual(logger.default_FORMAT, format, "format should be changed")
        self.assertNotEqual(default_format, format, "format should be changed")

        self.log.set_default_format(default_format)

    def test_init(self):
        self.assertIsInstance(self.log, Logger, "init should return Logger object")
        self.assertEqual(self.log.get_logger_name(), "setUp")
        self.assertEqual(self.log.get_log_level(), logging.INFO)

    def test_set_log_level(self):
        log = self.log.set_log_level(logging.ERROR)
        self.assertEqual(log.get_log_level(), logging.ERROR, 40)
        self.assertEqual(log.get_handlers()[0]["level"], logging.ERROR, 40)

    def test_set_format(self):
        test_format_str = '%(message)s'
        log = self.log.set_format(test_format_str)
        self.assertIsInstance(log.get_format(), Formatter)

    def test_build(self):
        log = self.log.build()
        self.assertTrue(not isinstance(log, Logger))

    def test_multi_logger_instance(self):
        log = Logger("logger1").build()
        log_2 = Logger("logger1").build()

        self.assertEqual(log, log_2)
        self.assertNotEqual(self.log, log)

class TestIncrementalLoggerLevel(TestCase):
    def test_convert_logger_level(self):
        count = len([]) 
        level = IncrementalLoggerLevel.convert_logger_level(count)
        self.assertEqual(level, logging.INFO)

        count = len(["-v"])
        level = IncrementalLoggerLevel.convert_logger_level(count)
        self.assertEqual(level, logging.DEBUG)

        count = -1 # WARNING
        level = IncrementalLoggerLevel.convert_logger_level(count)
        self.assertEqual(level, logging.WARNING)
