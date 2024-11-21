from handlers.base_handler import BaseHandler
from exceptions.delivery_error import DeliveryError


class DeliveryHandler(BaseHandler):
    """
    Обработчик доставки.
    """

    def handle(self, order: dict) -> None:
        """
        Обрабатывает запрос на доставку.

        :param order: Словарь с данными запроса, содержащий информацию о заказе.
        """
        if not order["address"]:
            raise DeliveryError
        print("Обрабатываем доставку.")
        super().handle(order)
