def handle_single_splits(markdown):
    if "\n" not in markdown:
        return markdown
    else:
        lines = markdown.split("\n")
        cleaned_lines = []
        for line in lines:
            if line.strip() == "":
                pass
            else:
                cleaned_lines.append(line.strip())
        marked_string = cleaned_lines[0]
        if len(cleaned_lines) >= 1:
            for line in cleaned_lines[1:]:
                marked_string += "\n" + line
    return marked_string


def markdown_to_blocks(markdown):
        splits = []
        if "\n\n" not in markdown:
            splits.append(handle_single_splits(markdown))
        else:
            # Split text at double newlines:
            double_split = markdown.split("\n\n")
            # Split double newlines again at single newline splits:
            for item in double_split:
                if "\n" not in item:
                     splits.append(item.strip())
                else:
                    # Remove newline markers so the list so the list can be cleaned:
                    single_split = item.split("\n")
                    stripped_splits = []

                    # Build cleaned list of single line splits:
                    for item in single_split:
                        if item.strip() == "":
                            pass
                        else:
                            stripped_splits.append(item.strip())
    
                    # Build split strings. Add newline markers as needed inside blocks:
                    split = stripped_splits[0]
                    if len(stripped_splits) == 1:
                        splits.append(split)
                    else:
                        for item in stripped_splits[1:]:
                            split += "\n" + item
                        splits.append(split)
        return splits