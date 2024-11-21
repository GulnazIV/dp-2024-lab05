from handlers.base_handler import BaseHandler
from interfaces.command import ICommand
from interfaces.order_handler import IOrderHandler


class ProcessOrderCommand(ICommand):
    """
    Команда для обработки заказа.
    """

    def __init__(self, order_handler: IOrderHandler, order: dict) -> None:
        """
        Инициализирует команду для обработки заказа.

        :param order_handler: Обработчик заказов, который будет использоваться для обработки переданного заказа.
        :param order: Заказ, который необходимо обработать.
        """
        self._order_handler = order_handler
        self._order = order

    def execute(self) -> None:
        """
        Выполняет команду по обработке заказа.
        """
        self._order_handler.handle(self._order)
