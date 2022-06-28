

class Item(object):
    def __init__(self, item):
        self.item = item

    def attribute_match(self, name, value):
        assert self.item.get_attribute(name) == value

    def text_match(self, value):
        assert self.item.text == value

    def click(self):
        return self.item.click()

