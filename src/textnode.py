class Textnode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        if (self.text == other.text and self.text_type == other.text_type and
                self.url == other.url):
            return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def main():
    node = Textnode("This is a text node", "bold", "https://boot.dev")
    print("test")
    return __repr__(node)