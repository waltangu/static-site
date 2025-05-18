def main():
    from textnode import TextNode, TextType
    node = TextNode("This is a link text node", TextType.LINK, "https://boot.dev")
    print(node.__repr__)
main()

