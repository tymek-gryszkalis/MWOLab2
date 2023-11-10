import unittest
import controller


class Test(unittest.TestCase):

    def test_getClientThatExists(self):
        res = controller.getClientById(1)
        temp = [(1, 'Kowalski', 'Janusz', 'januszkowalski@gmail.com')]

        self.assertEqual(res, temp)

    def test_getClientThatDoesntExist(self):
        res = controller.getClientById(4)
        temp = []

        self.assertEqual(res, temp)

    def test_getProductThatExists(self):
        res = controller.getProductById(1)
        temp = [(1, 'Wiertarka', 250, 3)]

        self.assertEqual(res, temp)

    def test_getProductThatDoesntExist(self):
        res = controller.getProductById(4)
        temp = []

        self.assertEqual(res, temp)

    def test_getOrderThatExists(self):
        res = controller.getOrderById(1)
        temp = [(1, 1, '1|2|3', 'pending')]

        self.assertEqual(res, temp)

    def test_getOrderThatDoesntExist(self):
        res = controller.getOrderById(2)
        temp = []

        self.assertEqual(res, temp)

unittest.main()