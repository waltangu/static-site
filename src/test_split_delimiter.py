import unittest

from textnode import TextNode
from split_delimiter import *


class TestSplitDelim(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        expected = [TextNode("This is text with a " , "text", None), TextNode("code block", "code", None), TextNode(" word", "text", None)]
        self.assertEqual(new_nodes, expected)

    @unittest.expectedFailure 
    def test_invalid_syntax(self):
        node = TextNode("This is text with an *italic word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        
    def test_leading_delimiter(self):
        node = TextNode("**This** is text with a bold word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        expected = [TextNode("This" , "bold", None), TextNode(" is text with a bold word", "text", None)]
        self.assertEqual(new_nodes, expected)