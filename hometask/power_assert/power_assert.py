

class PowerAssert:
    def __init__(self, softly=False):
        self.assertions = []
        self.softly = softly
        self.failures = []


    def assert_that(self, actual, expected):
        if self.softly:
            self.assertions.append((actual, expected))
        else:
            assert actual == expected


    def assert_all(self):
        for i in self.assertions:
            try:
                assert i[0] == i[1], f"\n\033[91m [F] Expected {i[0]} to be equal {i[1]} but it is not!\033[0m"
            except AssertionError as error:
                self.failures.append(error)
        for f in self.failures:
            print(f)
        assert len(self.failures) == 0, 'There are some failed assertions'






