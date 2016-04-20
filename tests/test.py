import unittest

from src.parser import Parser


class ParserTest(unittest.TestCase):
    def testFixtureOne(self):
        parser = Parser()

        fixture1 = parser.fixture1()
        (address, suite, postcode, description) = parser.parse(fixture1)

        expectedAddress = "Crown House, Toutley Road, Wokingham, Berkshire"
        self.assertEquals(address, expectedAddress)
        self.assertEquals(postcode, "RG41 1QW")
        self.assertEquals(suite, "Suite 2")

        # BONUS:
        # self.assertEqual(description, "This is some test description 1")

    def testFixtureTwo(self):
        parser = Parser()

        fixture2 = parser.fixture2()
        (address, suite, postcode, description) = parser.parse(fixture2)

        expectedAddress = "329 bracknell, Doncastle Road, Bracknell, Berkshire"
        self.assertEquals(address, expectedAddress)
        self.assertEquals(postcode, None)
        self.assertEquals(suite, None)

        # BONUS:
        # self.assertEqual(description, "Description part 1. Desc part 2.")
