class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name: str, description: str, price: int, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(products) if products else 0


if __name__ == "__main__":
    work1 = Product("potato", "vegetables", 100, 3)
    work = Category("apples", "fruit", ["помидор", "огурец"])
    print(work.name)
    print(work.description)
    print(work.products)
    print(work.total_categories)
    print(work.total_products)
    print(work1.name)
    print(work1.description)
    print(work1.price)
    print(work1.quantity)
