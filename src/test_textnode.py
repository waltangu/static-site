import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_urlnone(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("This is a text node", TextType.LINK, "boot.dev")
        self.assertEqual(node.url, "boot.dev")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
     unittest.main()