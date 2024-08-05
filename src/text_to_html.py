from textnode import TextNode
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    text_type_text = LeafNode(None, text_node.text, None)
    text_type_bold = LeafNode("b", text_node.text, None)
    text_type_italic = LeafNode("i", text_node.text, None)
    text_type_code = LeafNode("code", text_node.text, None)
    text_type_link = LeafNode("a", text_node.text, {"href": text_node.url})
    text_type_image = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})


    if text_node.text_type == "text":
        return text_type_text
    elif text_node.text_type == "bold":
        return text_type_bold
    elif text_node.text_type == "italic":
        return text_type_italic
    elif text_node.text_type == "code":
        return text_type_code
    elif text_node.text_type == "link":
        return text_type_link
    elif text_node.text_type == "image":
        return text_type_image
    else:
        raise Exception("Unrecognized TextNode type.")