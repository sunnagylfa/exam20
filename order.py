class Order:
    def __init__(self, kind, price:"float"):
        """Initializes the class"""
        self.kind=kind
        self.cost=price
    def item(self):
        return self.kind
    def price(self):
        return self.cost
    def __str__(self):
        """Returns string to print"""
        returnstring = f"Item: {self.item}, price: {self.price}"
        return returnstring
    def __add__(self, other)->"Order":
        item=self.kind+other.kind
        price=self.price+other.price
        return Order(item, price)
    def __gt__(self, other):
        """Checks if price is more than price of other"""
        if self.cost>other.cost:
            return True
        else:
            return False
def main(): # Do not change this line
    order1=Order("iphone", 200)
    print(order1.item())

# Main program starts here. Do not change it.
if __name__ == "__main__":
    main()