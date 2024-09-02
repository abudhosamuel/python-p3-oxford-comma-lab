def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        return ', '.join(items[:-1]) + f", and {items[-1]}"

print(oxford_comma(["fiddleheads"]))  # => "fiddleheads"
print(oxford_comma(["fiddleheads", "okra"]))  # => "fiddleheads and okra"
print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))  # => "fiddleheads, okra, and kohlrabi"
