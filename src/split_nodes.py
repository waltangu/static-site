from extract_links import *
from textnode import *

def split_nodes_image(old_nodes):
    #Boots:
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
