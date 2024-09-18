import pytest

from src.work import Product, Category


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="Samsung Galaxy S23 Ultra",
        price=180000,
        quantity=5
    )


@pytest.fixture
def category():
    product1 = Product("Samsung Galaxy S23 Ultra", "Samsung Galaxy S23 Ultra", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        name="Смартфоны",
        description="""Смартфоны, как средство не только коммуникации, 
        но и получения дополнительных функций для удобства жизни""",
        products=[product1, product2, product3]
    )


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000
    assert product.quantity == 5


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == """Смартфоны, как средство не только коммуникации, 
        но и получения дополнительных функций для удобства жизни"""
    assert len(category.products) == 3

    assert category.category_count == 1
    assert category.product_count == 3