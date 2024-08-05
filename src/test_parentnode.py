import unittest

from htmlnode import LeafNode
from htmlnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_no_tag_err(self):
        children = ["a","b","c"]
        try:    
            node = ParentNode(None, children, None)
            node.to_html()
        except ValueError:
            print(".")

    def test_no_children_err(self):
        node = ParentNode(None, "", None)
        try:    
            node.to_html()
        except ValueError:
            print('.')         
                  
    def test_1xleafnode(self):
        children = [LeafNode("b", "Bold text", None)]
        node = ParentNode("p", children, None)
        self.assertEqual(node.to_html(),"<p><b>Bold text</b></p>")

    def test_2xleafnode(self):
        children = [LeafNode("b", "Bold text", None), LeafNode("i", "Italic text", None)]
        node = ParentNode("p", children, None)
        self.assertEqual(node.to_html(),"<p><b>Bold text</b><i>Italic text</i></p>")

    def test_nested_parent(self):
        children = [ParentNode("p", [LeafNode("i", "Italic text", None)], None), LeafNode("b", "Bold text", None)]
        node = ParentNode("p", children, None)
        self.assertEqual(node.to_html(),"<p><p><i>Italic text</i></p><b>Bold text</b></p>")


    def test_double_nest(self):
        children = [ParentNode("p", [ParentNode("p", [LeafNode(None, "Normal text"), LeafNode("i", "Italic text", None)], None), LeafNode("b", "Bold text", None)], None)]
        node = ParentNode("p", children, None)
        self.assertEqual(node.to_html(), "<p><p><p>Normal text<i>Italic text</i></p><b>Bold text</b></p></p>")
"""
    def test_to_html(self):
        node = LeafNode("a", "Text inside paragraph", {"href": "https://www.google.com", 
        "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Text inside paragraph</a>')
    
    def test_to_html_noprop(self):
        node = LeafNode("p", "This is a paragraph of text", None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text</p>")
"""

if __name__ == "__main__":
     unittest.main()