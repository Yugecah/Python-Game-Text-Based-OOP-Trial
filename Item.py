class Item:
class Item:
    def __init__(self, name, item_type, value):
        self.name = name            # Name of the item
        self.item_type = item_type  # e.g. "heal", "attack", "misc"
        self.value = value          # Effect value (heal amount, damage boost, etc.)

    def use(self, player):
        """Apply item effect to player"""
        if self.item_type == "heal":
            player.health += self.value
            print(f"{player.name} used {self.name} and restored {self.value} health!")

        elif self.item_type == "attack":
            print(f"{self.name} will increase next attack by {self.value}!")

        else:
            print(f"{self.name} has no effect.")

    def __str__(self):
        return f"{self.name} ({self.item_type}: {self.value})"