from abc import ABC, abstractmethod


class ICommand(ABC):
    """
    Интерфейс команды объявляет метод для выполнения команды.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        Выполняет команду.
        """
        pass
