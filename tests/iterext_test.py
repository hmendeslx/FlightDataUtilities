# -*- coding: utf-8 -*-
# vim:et:ft=python:nowrap:sts=4:sw=4:ts=4
##############################################################################

'''
Flight Data Utilities: Iter Extensions: Unit Tests
'''

##############################################################################
# Imports


import logging
import unittest

from flightdatautilities import iterext


##############################################################################
# Module Setup


def setUpModule():
    logging.disable(logging.CRITICAL)


##############################################################################
# Test Cases


class TestBatch(unittest.TestCase):

    def test_batch(self):
        self.assertEqual(list(iterext.batch(0, 5, 2)), [(0, 2), (2, 4), (4, 5)])
        self.assertEqual(list(iterext.batch(1, 5, 2)), [(1, 3), (3, 5)])
        self.assertEqual(list(iterext.batch(0, 10, 5)), [(0, 5), (5, 10)])
        self.assertEqual(list(iterext.batch(0, 11, 5)), [(0, 5), (5, 10), (10, 11)])


class TestDropLast(unittest.TestCase):

    def test_droplast(self):
        self.assertEqual(list(iterext.droplast(1, range(10))), list(range(9)))
        self.assertEqual(list(iterext.droplast(5, range(10))), list(range(5)))
        self.assertEqual(list(iterext.droplast(10, range(10))), [])
        self.assertEqual(list(iterext.droplast(20, range(10))), [])


class TestNestedGroupby(unittest.TestCase):

    @unittest.skip('Not implemented.')
    def test_nested_groupby(self):
        pass
