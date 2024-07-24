def main():
    from textnode import Textnode
    node = Textnode("This is a text node", "bold", "https://boot.dev")
    return node.__repr__
