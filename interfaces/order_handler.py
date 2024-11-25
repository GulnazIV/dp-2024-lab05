from abc import abstractmethod, ABC


class IOrderHandler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков.
    """

    @abstractmethod
    def set_next(self, handler: "IOrderHandler") -> "IOrderHandler":
        """
        Устанавливает следующий обработчик в цепочке.

        :param handler: Обработчик, который будет установлен в качестве следующего.
        """
        pass

    @abstractmethod
    def handle(self, order: str) -> None:
        """
        Обрабатывает входящий запрос.

        :param order: Запрос, который необходимо обработать.
        """
        pass
