from textnode import TextNode

# Convert markdown string to a list of TextNodes using markdown delimiters.
# Argument "old_nodes" is a list of TextNodes with markdown in TextNode.text.
# TextNodes in "old_nodes" will only be of text type "text."
# One matching set of delimiter/text_type will be the other two arguments.

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    split_text = []
    text_type_text="text"
    text_type_code="code"
    text_type_italic="italic"
    text_type_bole="bold"
    
    
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
        elif delimiter == None or delimiter not in old_node.text:
            new_nodes.append(old_node)
        elif old_node.text.count(delimiter)%2 != 0:
            raise SyntaxError(f"Markdown string '{old_node.text}' must include closing delimiter.")
        elif old_node.text[0] == delimiter:
            split_text.extend(old_node.text.split(delimiter))
            
            for split in split_text:
                if (split_text.index(split)+2)%2 == 1:
                    new_node = TextNode(split, "text")
                    new_nodes.append(new_node)
                
                else:
                    new_node = TextNode(split, text_type)
                    new_nodes.append(new_node)
        else:
            split_text.extend(old_node.text.split(delimiter))
            
            for split in split_text:
                if (split_text.index(split)+2)%2 == 0:
                    new_node = TextNode(split, "text")
                    new_nodes.append(new_node)
                
                else:
                    new_node = TextNode(split, text_type)
                    new_nodes.append(new_node)
    for new_node in new_nodes:
        if new_node.text == "":
            new_nodes.remove(new_node)


    return new_nodes