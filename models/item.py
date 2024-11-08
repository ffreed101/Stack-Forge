from .tag import Tag

class Item:
    def __init__(self, itemNum):
        self.itemNum = itemNum
        self.tags = []

    def createTag(self):
        while True:
            try:
                tag_number = input("Enter tag number: ")
                if not tag_number.isdigit():
                    raise ValueError("Tag number should contain only numbers.")

                piece_count = int(input("Enter piece count: "))
                new_tag = Tag(tag_number, piece_count)
                self.tags.append(new_tag)
                print(f"Tag {tag_number} with piece count {piece_count} added.")

                # Check if the user wants to add another tag
                add_more = input("Add another tag? (Y/N): ").upper()
                if add_more != "Y":
                    break
            except ValueError as e:
                print(f"Invalid input: {e}")