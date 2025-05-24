import unittest
from blocks import *

class test_block_splitter(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        self.assertEqual(
            markdown_to_blocks(md),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = """
            Line1
            Line2
            Line3
            Line4
            """
        self.assertEqual(
            markdown_to_blocks(md), ["Line1\nLine2\nLine3\nLine4"]
        )
