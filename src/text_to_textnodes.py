from extract_links import *
from split_delimiter import *

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    extract_markdown_links(
        extract_markdown_links(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        node, "**", TextType.BOLD), "_", TextType.ITALIC
                ), "`", TextType.CODE  
            )
        )
    )