import unittest
from unittest.mock import Mock
import bowling


class My_Test(unittest.TestCase):

    def test_strike(self):
        do_throw_ball = Mock(return_value=10)

        first = bowling.Game()
        assertEq