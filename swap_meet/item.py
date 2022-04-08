## Attempting to define these below in Item instead of globally. 
# CATEGORIES = {
#     "": "Hello World!",
#     "Clothing": "The finest clothing you could wear.",
#     "Decor": "Something to decorate your space.",
#     "Electronics": "A gadget full of buttons and secrets.",
# }

# CONDITION_DESCRIPTORS = {
#     0: "Oof. Are you sure you want this?",
#     1: "Wow. It's pretty bad.",
#     2: "Significant damage.",
#     3: "Needs some love.",
#     4: "Minor signs of wear or damage.",
#     5: "So good it might be a scam.",
# }

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    CATEGORIES = {
        "": "Hello World!",
        "Clothing": "The finest clothing you could wear.",
        "Decor": "Something to decorate your space.",
        "Electronics": "A gadget full of buttons and secrets.",
    }

    CONDITION_DESCRIPTORS = {
        0: "Oof. Are you sure you want this?",
        1: "Wow. It's pretty bad.",
        2: "Significant damage.",
        3: "Needs some love.",
        4: "Minor signs of wear or damage.",
        5: "So good it might be a scam.",
    }

    def __str__(self):
        return Item.CATEGORIES[self.category]

    def condition_description(self):
        return Item.CONDITION_DESCRIPTORS[int(self.condition)]