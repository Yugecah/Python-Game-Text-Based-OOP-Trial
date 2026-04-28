class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add item to inventory"""
        self.items.append(item)
        print(f"{item.name} added to inventory!")

    def remove_item(self, item_name):
        """Remove item by name"""
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} removed from inventory.")
                return
        print("Item not found.")

    def show_inventory(self):
        """Display all items"""
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item}")

    def use_item(self, item_name, player):
        """Use an item and apply its effect"""
        for item in self.items:
            if item.name == item_name:
                item.use(player)
                self.items.remove(item)
                return
        print("Item not found.")