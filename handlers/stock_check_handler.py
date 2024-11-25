from handlers.base_handler import BaseHandler
from exceptions.out_of_stock_error import OutOfStockError


class StockCheckHandler(BaseHandler):
    """
    Обработчик проверки наличия товара на складе.
    """

    def __init__(self, inventory: dict) -> None:
        """
        Инициализирует обработчик проверки наличия товара.

        :param inventory: Словарь с запасами товаров.
        """
        self._inventory = inventory
        super().__init__()

    def handle(self, order: dict) -> None:
        """
        Обрабатывает запрос на наличие товара.

        :param order: Словарь с данными запроса, содержащий информацию о заказе.
        """
        if self._inventory[order["item"]] == 0:
            raise OutOfStockError
        print("Товар есть на складе.")
        super().handle(order)
