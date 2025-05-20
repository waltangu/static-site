from textnode import *

# Convert markdown string to a list of TextNodes using markdown delimiters.
# Argument "old_nodes" is a list of TextNodes with markdown in TextNode.text.
# TextNodes in "old_nodes" will only be of text type "text."
# One matching set of delimiter/text_type will be the other two arguments.

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