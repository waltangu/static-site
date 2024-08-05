import unittest

from htmlnode import LeafNode
from textnode import TextNode
from text_to_html import *

class TestTextToHTML(unittest.TestCase):
    def  test_text(self):
        text_node_text = TextNode("This is text.", "text", None)
        html_node = text_node_to_html_node(text_node_text)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNone(html_node.tag)

    def test_bold(self):
        text_node_bold = TextNode("This is bold text.", "bold", None)
        html_node = text_node_to_html_node(text_node_bold)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "b")

    def test_italic(self):
        text_node_italic = TextNode("This is italic text.", "italic", None)
        html_node = text_node_to_html_node(text_node_italic)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "i")

    def test_link(self):
        text_node_link = TextNode("This is a link.", "link", "boot.dev")
        html_node = text_node_to_html_node(text_node_link)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "boot.dev"})
        #print(html_node.to_html())

    def test_image(self):
        text_node_image = TextNode("This is the image alt text.", "image", "google.com")
        html_node = text_node_to_html_node(text_node_image)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src":"google.com", "alt": "This is the image alt text."})
        #print(html_node.to_html())



if __name__ == "__main__":
     unittest.main()