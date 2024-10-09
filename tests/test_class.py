import pytest

from src.work import Category, LawnGrass, Product, Smartphone


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


@pytest.fixture
def smartphone():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def lawngrass():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


@pytest.fixture()
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture()
def product_2():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def product_6():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


@pytest.fixture
def product_7():
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава",
        price=450.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый",
    )


@pytest.fixture
def category_1():
    return Category(
        name="Пустая категория", description="Категория без продуктов", products=[]
    )


def test__add(product_1, product_2, product_6, product_7):
    assert Product.__add__(product_1, product_2) == 2580000.0
    assert Product.__add__(product_6, product_7) == 16750.0


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
    assert str(category) == "Смартфоны, количество продуктов: 12 шт."


def test_add(example_product1, example_product2):
    assert (example_product1.price * example_product1.quantity) + (
        example_product2.price * example_product2.quantity
    ) == 2580000.0


def test_smartphone_init(smartphone):
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawngrass_init(lawngrass):
    assert lawngrass.name == "Газонная трава"
    assert lawngrass.description == "Элитная трава для газона"
    assert lawngrass.price == 500.0
    assert lawngrass.quantity == 20
    assert lawngrass.country == "Россия"
    assert lawngrass.germination_period == "7 дней"
    assert lawngrass.color == "Зеленый"


def test_mixin_print(capsys):
    Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)'

    Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    message = capsys.readouterr()
    assert (
        message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    )

    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
    )


def test_quantity_zero(product_1):
    product_1.quantity = 0
    assert "Цена не должна быть нулевая или отрицательная"


def test_price_category(category, category_1):
    assert Category.middle_price(category_1) == 0
    assert Category.middle_price(category) == 140333
