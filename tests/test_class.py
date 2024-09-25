import pytest

from src.work import Category, Product


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="Samsung Galaxy S23 Ultra",
        price=180000,
        quantity=5,
    )


@pytest.fixture
def category():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "Samsung Galaxy S23 Ultra", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[product1, product2, product3],
    )


@pytest.fixture
def example_product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def example_product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000
    assert product.quantity == 5


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert (
        category.description == "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 146

    assert category.category_count == 1
    assert category.product_count == 3


def test_products_property(category):
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_product(category):
    assert category.product_count == 9


def test_new_product():
    products = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    products.name = "Samsung Galaxy S23 Ultra"
    products.description = "256GB, Серый цвет, 200MP камера"
    products.price = 180000.0
    products.quantity = 5


def test_price_setter(product):
    product.price = -100
    if product.price <= 0:
        message = "Цена не должна быть нулевая или отрицательная"
        assert message == "Цена не должна быть нулевая или отрицательная"


def test_str_product(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."


def test_str_category(category):
    assert (
        str(category)
        == "Смартфоны, как средство не только коммуникации, "
           "но и получения дополнительных функций для удобства жизни, количество продуктов: 3 шт."
    )


def test_add(example_product1, example_product2):
    assert (example_product1.price * example_product1.quantity) + (
        example_product2.price * example_product2.quantity
    ) == 2580000.0
