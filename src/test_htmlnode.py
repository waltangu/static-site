import unittest

from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):
    def test_prop_to_HTML(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", 
        "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_repr(self):
        Child1 = HTMLNode("a", "Hello Child1", None, None)
        Child2 = HTMLNode("h1", "Hello Child2", None, None)
        children = [Child1, Child2]
        node = HTMLNode("a", "Text inside paragraph", children, {"href": "https://www.google.com", 
        "target": "_blank"})
        self.assertEqual(node.__repr__(), "tag = a, value = Text inside paragraph, children = [tag = a, value = Hello Child1, children = None, props = None, tag = h1, value = Hello Child2, children = None, props = None], props = {'href': 'https://www.google.com', 'target': '_blank'}")
        #print(node.__repr__())
    
    def test_no_input(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
    
    def test_tag(self):
        node = HTMLNode("a")
        self.assertIs(node.tag, 'a')
    
    def test_value(self):
        node = HTMLNode(None,"Text inside paragraph")
        self.assertIs(node.value, "Text inside paragraph")

if __name__ == "__main__":
     unittest.main()