class TextNode:
    def __init__(self, text, tect_type, url=None):
        self.text = text
        self.text_type = tect_type
        self.url = url
    def __eq__(self, other):
        if (self.text == other.text and self.text_type == other.text_type and
                self.url == other.url):
            return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
