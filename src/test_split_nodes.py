import unittest

from textnode import *
from split_nodes import *


class TestSplitNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_no_images(self):
        node = TextNode("This text has no image!", TextType.TEXT)
        self.assertListEqual(split_nodes_image([node]), [TextNode("This text has no image!", TextType.TEXT)])
    
    def test_list_nodes(self):
        nodes = [
            TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT),
            TextNode("This text has no image!", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This text has no image!", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),    
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
                ],
                new_nodes
        ) 

    def test_links_no_trail_or_lead_string(self):
        node = TextNode(
            "[To boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("To boot dev", TextType.LINK, "https://www.boot.dev"),    
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
                ],
                new_nodes
        ) 

    def test_split_link_selectivity(self):
        node = TextNode(
            "![Image](https://i.imgur.com/zjjcJKZ.png) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("![Image](https://i.imgur.com/zjjcJKZ.png) and ", TextType.TEXT),    
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
                ],
                new_nodes
        ) 

    def test_mixed_node(self):
        node = TextNode(
            "![Image](https://i.imgur.com/zjjcJKZ.png) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT)
        new_nodes = split_nodes_image(split_nodes_link([node]))
        self.assertListEqual(
            [
                TextNode("Image",TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and ", TextType.TEXT),    
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
                ],
                new_nodes
        ) 
    
    def test_list_link_nodes(self):
        nodes = [
            TextNode("[This](https://www.google.com) is a link to Google.", TextType.TEXT),
            TextNode("[This](https://www.yahoo.com) is a link to Yahoo.", TextType.TEXT),
            TextNode("This text has no image!", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("This", TextType.LINK, "https://www.google.com"),
                TextNode(" is a link to Google.", TextType.TEXT),
                TextNode("This", TextType.LINK, "https://www.yahoo.com"),
                TextNode(" is a link to Yahoo.", TextType.TEXT),
                TextNode("This text has no image!", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_mixed_list(self):
        nodes = [
            TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT), 
            TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT),
            TextNode("This text has no image!", TextType.TEXT)
        ]
        new_nodes1 = split_nodes_image(split_nodes_link(nodes))
        new_nodes2 = split_nodes_link(split_nodes_image(nodes))
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),    
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode("This text has no image!", TextType.TEXT),
            ], 
            new_nodes1)

        self.assertListEqual(new_nodes1, new_nodes2)
