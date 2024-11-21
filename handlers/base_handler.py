from interfaces.order_handler import IOrderHandler


class BaseHandler(IOrderHandler):
    """
    Базовый обработчик для реализации цепочки ответственности.
    """

    def __init__(self) -> None:
        """
        Инициализирует базовый обработчик.
        """
        self._next_handler = None

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочке.

        :param handler: Обработчик, который будет установлен в качестве следующего.

        :return: Возвращает текущий обработчик для удобства дальнейшей настройки цепочки.
        """
        self._next_handler = handler
        return handler

    def handle(self, order: dict) -> None:
        """
        Обрабатывает запрос и передает его следующему обработчику.

        :param order: Запрос, который необходимо обработать.
        """
        if self._next_handler:
            self._next_handler.handle(order)
