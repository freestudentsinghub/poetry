import pytest

from src.work import Category, Product


@pytest.fixture
def product():
    return Product(name="potato", description="vegetables", price=100, quantity=3)


@pytest.fixture
def category():
    return Category(name="apples", description="fruit", products=["помидор", "огурец"])
