import re
from textnode import *

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((https?:\/\/.*?\..*?)\)", text)
  

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((https?:\/\/.*?\..*?)\)", text)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    split_text = []
    allowed_delimiters = ["`",'*',"**","_", "__"] #code, bold, italics
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        elif delimiter not in allowed_delimiters:
            raise NameError(f"Delimiter '{delimiter}' is not recognized.")
        elif delimiter not in old_node.text:
            new_nodes.append(old_node)
        elif old_node.text.count(delimiter)%2 != 0:
            raise SyntaxError(f"Markdown string '{old_node.text}' must include closing delimiter.")
        else:
            split_text.extend(old_node.text.split(delimiter))
            for i in range(0, len(split_text)):
                if i%2  == 0:
                    new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_text[i], text_type))
    # Remove empty TextNodes:
    for new_node in new_nodes:
        if new_node.text == "":
            new_nodes.remove(new_node)
    return new_nodes


def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue   
        image_tuples = extract_markdown_images(old_node.text)
        if not image_tuples:
            result.append(old_node)
            continue
        
        # Process the first image
        image_alt, image_url = image_tuples[0]
        parts = old_node.text.split(f"![{image_alt}]({image_url})", 1)
        
        # Add text before image if not empty
        if parts[0] != "":
            result.append(TextNode(parts[0], TextType.TEXT))
            
        # Add the image node
        result.append(TextNode(image_alt, TextType.IMAGE, image_url))
        
        # Process remaining text recursively if not empty
        if len(parts) > 1 and parts[1] != "":
            remaining_nodes = split_nodes_image([TextNode(parts[1], TextType.TEXT)])
            result.extend(remaining_nodes)
    
    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
            
        link_tuples = extract_markdown_links(old_node.text)
        if len(link_tuples) == 0:
            result.append(old_node)
            continue
            
        # Process the first link
        anchor_text, link_url = link_tuples[0]
        parts = old_node.text.split(f"[{anchor_text}]({link_url})", 1)
        
        # Add text before link if not empty
        if parts[0] != "":
            result.append(TextNode(parts[0], TextType.TEXT))
            
        # Add the link node
        result.append(TextNode(anchor_text, TextType.LINK, link_url))
        
        # Process remaining text recursively if not empty
        if len(parts) > 1 and parts[1] != "":
            remaining_nodes = split_nodes_link([TextNode(parts[1], TextType.TEXT)])
            result.extend(remaining_nodes)

    return result

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