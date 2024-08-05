class HTMLNode:
    def  __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        __html_props_str = ""
        for prop_key in self.props:
            __html_props_str += f' {prop_key}="{self.props[prop_key]}"'
        return __html_props_str
    
    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=str, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=list, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must include tag")
        elif self.children == None or len(self.children) < 1:
            raise ValueError("ParentNode must include list of children")
        else:
            children_str = ""
            #if len(self.children) < 1:
            #    return ParentNode_str
# ParentNode: Must have tag,  must have children. Children may be LeafNodes or other ParentNodes.
# Recursion: take each child and run to_html method; for each child, recurse on any further nested children.
#   self.children is a list of children. Start on the first child, if it has children recurse on that list, before proceeding with the first list.
#   Use indices to progress, i.e. successive recursion input would be children[1:]. When the len(list) < 1, stop recursing. 
           
            for child in self.children:
                if isinstance(child, ParentNode):
                    children_str += f'{child.to_html()}'
                else:
                    children_str += f"{LeafNode.to_html(child)}"
                
            ParentNode_str = f'<{self.tag}>{children_str}</{self.tag}>'

            return ParentNode_str 