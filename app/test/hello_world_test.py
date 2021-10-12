import unittest
from app.local import hello_world

class HelloWorldTest(unittest.TestCase):

    def setUp(self):
        self.greeter = hello_world.Greeter('TDD')
        

    def test_hello_world(self):
        expected = 'Hello, World!'
        message = hello_world.hello_world()
        self.assertEqual(expected, message)

    def test_hello_name(self):
        expected = 'Hello, Nosy!'
        message = hello_world.hello_name('Nosy')
        self.assertEqual(expected, message)


    def test_greeter(self):
        expected = 'Hello, TDD!'
        message = self.greeter.greet()
        self.assertEqual(expected, message)




if __name__=='__main__':
    unittest.main()
