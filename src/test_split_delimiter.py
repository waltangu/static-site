import unittest

from textnode import *
from inline import *


class TestSplitDelim(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]
        self.assertListEqual(new_nodes, expected)

    @unittest.expectedFailure 
    def test_invalid_syntax(self):
        node = TextNode("This is text with an _italic word", TextType.TEXT)
        split_nodes_delimiter([node], "_", TextType.ITALIC)

    @unittest.expectedFailure
    def test_invalid_delimiter_arg(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        split_nodes_delimiter([node], "-", TextType.ITALIC)
        
    def test_leading_delimiter(self):
        node = TextNode("**This** is text with a bold word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("This" , TextType.BOLD), TextNode(" is text with a bold word", TextType.TEXT)]
        self.assertListEqual(new_nodes, expected)

    def test_mixed_types_1f(self):
        node = [TextNode("This is a `code block`, this is *italic*, this is **bold**.", TextType.TEXT)]
        expected = [
            TextNode("This is a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(", this is *italic*, this is **bold**.", TextType.TEXT),
            ]
        self.assertListEqual(split_nodes_delimiter(node, "`", TextType.CODE), expected)

    def test_multiple_input_nodes(self):
        nodes = [
            TextNode("A **bold** word.", TextType.TEXT),
            TextNode("A `code block` section.", TextType.TEXT),
            TextNode("An _italic_ word.", TextType.TEXT)
            ]
        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT),
            TextNode("A `code block` section.", TextType.TEXT),
            TextNode("An _italic_ word.", TextType.TEXT)
        ]
        self.assertListEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)
    
    def test_mixed_types_2f(self):
        node = [TextNode("This is a `code block`, this is _italic_, this is **bold**.", TextType.TEXT)]
        expected = [
            TextNode("This is a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(", this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", this is **bold**.", TextType.TEXT),
            ]
        self.assertListEqual(split_nodes_delimiter(split_nodes_delimiter(node, "`", TextType.CODE), "_", TextType.ITALIC), expected)

    def test_mixed_types_3f(self):
        node = [TextNode("This is a `code block`, this is _italic_, this is **bold**.", TextType.TEXT)]
        expected = [
            TextNode("This is a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(", this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(".", TextType.TEXT)
            ]
        self.assertListEqual(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(node, "`", TextType.CODE), "_", TextType.ITALIC), "**", TextType.BOLD), expected)