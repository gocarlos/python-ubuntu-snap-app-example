from myapp_source import my_great_app
import unittest


class MyTest(unittest.TestCase):
    def test(self):
        print ('\n\n\n\n\n\nInside the test\n\n\n\n')
        self.assertEqual(my_great_app.fun(3), 4)


if __name__ == '__main__':
    unittest.main()
