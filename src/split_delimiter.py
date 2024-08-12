from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    delimiter_list = ["*", "**", "`" ]
    for node in old_nodes:
        if node.text_type != "text_type_text":
            return node.text
        elif delimiter not in delimiter_list:   
            raise Exception("Invalid markdown syntax")
        else:
            split_text_list = node.text.split(delimiter)
            for text in split_text_list:
                
