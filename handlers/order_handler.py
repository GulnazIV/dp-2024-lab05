from handlers.base_handler import BaseHandler


class OrderHandler(BaseHandler):
    """
    Обработчик заказов.
    """

    def handle(self, order: dict) -> None:
        """
        Начинает обработку данных заказа.

        :param order: Словарь с данными запроса, содержащий информацию о заказе.
        """
        print("Начинаем обработку данных.")
        super().handle(order)
