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
        return (f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}")