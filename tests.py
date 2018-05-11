#!/usr/bin/env python
# coding: utf-8

import sys
import unittest

from streamtest import CatchStreamTestCase
from streamtest.context import _StreamContext


class StdoutTestCase(CatchStreamTestCase):

    def test_print(self):

        with self.catch_stream("stdout") as stream:
            print "hello world"

        self.assertEqual(stream, "hello world\n")

    def test_write(self):

        with self.catch_stream("stdout") as stream:
            sys.stdout.write("hello world")

        self.assertNotEqual(stream, "hello")


class StderrTestCase(CatchStreamTestCase):

    def test_write(self):

        with self.catch_stream("stderr") as stream:
            sys.stderr.write("Error!")

        self.assertEqual(stream, "Error!")


class StreamContextTestCase(unittest.TestCase):

    def test_functions(self):

        context = _StreamContext("stdout")

        context.catch()
        print "hello"
        context.release()

        self.assertEqual(context.output, "hello\n")

    def test_ext(self):

        with _StreamContext("stdout") as stream:
            print "hello world"

        with _StreamContext("stdout") as stream2:
            print "hello"

        self.assertNotEqual(stream, stream2)
        self.assertNotEqual(stream.output, stream2.output)

        with _StreamContext("stdout") as stream3:
            print "hello world"

        self.assertEqual(stream, stream3)
        self.assertEqual(stream.output, stream3.output)
        self.assertEqual(str(stream), str(stream3))


if __name__ == '__main__':

    unittest.main(verbosity=2)
