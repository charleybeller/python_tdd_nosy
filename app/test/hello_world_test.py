import unittest
from app.local import hello_world

class HelloWorldTest(unittest.TestCase):

    def test_hello_world(self):
        expected = 'Hello, World!'
        message = hello_world.hello_world()
        self.assertEqual(expected, message)

    def test_hello_name(self):
        expected = 'Hello, Nosy!'
        message = hello_world.hello_name('Nosy')
        self.assertEqual(expected, message)
