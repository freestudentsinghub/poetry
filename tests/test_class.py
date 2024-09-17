def test_product_init(product):
    assert product.name == "potato"
    assert product.description == "vegetables"
    assert product.price == 100
    assert product.quantity == 3


def test_category_init(category):
    assert category.name == "apples"
    assert category.description == "fruit"
    assert category.products == ["помидор", "огурец"]
    assert len(category.products) == 2

    assert category.total_categories == 1
    assert category.total_products == 2
