import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_none_value(self):
        try:
            node = LeafNode(None, None, None)
            node.to_html()
        except ValueError:
           print(".")

    def test_blank_value(self):
        node = LeafNode(None, "", None)
        try:    
            node.to_html()
        except ValueError:
            print(".")         
                         
    def test_no_tag(self):
        node = LeafNode(None, "raw text", None)
        self.assertIs(node.value,"raw text")

    def test_to_html(self):
        node = LeafNode("a", "Text inside paragraph", {"href": "https://www.google.com", 
        "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Text inside paragraph</a>')
    
    def test_to_html_noprop(self):
        node = LeafNode("p", "This is a paragraph of text", None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text</p>")

if __name__ == "__main__":
     unittest.main()