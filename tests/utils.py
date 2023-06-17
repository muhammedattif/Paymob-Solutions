class AbstractTestCase:
    """
    Abstract TestCase Class which provides a punch of an assertions utility functions
    """

    def assertEqual(self, actual, expected):
        assert actual == expected

    def assertIsNone(self, variable):
        assert variable is None

    def assertIsNotNone(self, variable):
        assert variable is not None

    def assertTrue(self, variable):
        assert variable is True

    def assertFalse(self, variable):
        assert variable is False

    def assertHasAttr(self, obj, attr):
        assert hasattr(obj, attr) is True

    def assertNoHasAttr(self, obj, attr):
        assert hasattr(obj, attr) is not True
