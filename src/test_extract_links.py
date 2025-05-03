import unittest
from extract_links import *
from htmlnode import HTMLNode



class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_multiple_images(self):
        matches = extract_markdown_images("This is text with two images: ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://imgur.com/gallery/happy-sunday-miscMsp)")
        self.assertListEqual([("image1", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://imgur.com/gallery/happy-sunday-miscMsp")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with an [link](https://i.imgur.com)")
        self.assertListEqual([("link", "https://i.imgur.com")], matches)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links("This is text with two links [link1](https://i.imgur.com) and  [link2](https://optical.toys/)")
        self.assertListEqual([("link1", "https://i.imgur.com"), ("link2", "https://optical.toys/")], matches)