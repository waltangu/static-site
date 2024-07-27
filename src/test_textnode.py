import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_urlnone(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("This is a text node", "bold", "boot.dev")
        self.assertEqual(node.url, "boot.dev")

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold", "boot.dev")
        node2 = TextNode(None, None, None)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
     unittest.main()