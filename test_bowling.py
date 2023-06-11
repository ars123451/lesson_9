import unittest
import random
import bowling


class My_Test(unittest.TestCase):

    def test_strike(self):
        ball_2 = random.randint(0, 10)
        self.assertEqual(bowling.frame(1, 10, ball_2), "X")

    def test_spare(self):
        self.assertEqual(bowling.frame(2, 4, 6), '4/')

    def test_00(self):
        self.assertEqual(bowling.frame(3, 0, 0), '00')


if __name__ == '__main__':
    unittest.main()
