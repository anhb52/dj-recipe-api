from django.test import SimpleTestCase

from app import add

class CalcTest(SimpleTestCase):

    def test_add_number(self):
        result = add.add(3,4)
        self.assertEqual(result,7)
