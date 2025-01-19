import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        a1 = Runner('Walk')
        for i in range(10):
            a1.walk()
        self.assertEqual(a1.distance, 50)

    def test_run(self):
        a1 = Runner('Run')
        for i in range(10):
            a1.run()
        self.assertEqual(a1.distance, 100)

    def test_chellenger(self):
        a1 = Runner('Walk_1')
        a2 = Runner('Run_1')
        for i in range(10):
            a1.walk()
            a2.run()
        self.assertNotEqual(a1.distance, a2.distance)

if __name__ =='__main__':
    unittest.main()