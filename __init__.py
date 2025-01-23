from products import dao


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        """
        A class to represent a product.

        :param id: Product ID
        :param name: Product name
        :param description: Product description
        :param cost: Product cost
        :param qty: Product quantity (default is 0)
        """
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> "Product":
        """
        Create a Product object from a dictionary.

        :param data: A dictionary containing product details
        :return: Product object
        """
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data.get('qty', 0)  # Default qty to 0 if not provided
        )


def list_products() -> list[Product]:
    """
    Fetch all products from the DAO and return them as a list of Product objects.

    :return: A list of Product objects
    """
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Product:
    """
    Fetch a single product by its ID.

    :param product_id: The ID of the product to fetch
    :return: Product object
    """
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load(product_data)


def add_product(product: dict):
    """
    Add a new product using the DAO.

    :param product: A dictionary containing product details
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Update the quantity of a product.

    :param product_id: The ID of the product to update
    :param qty: The new quantity of the product
    :raises ValueError: If the quantity is negative
    """
    if qty < 0:
        raise ValueError('Quantity cannot be negative.')
    dao.update_qty(product_id, qty)