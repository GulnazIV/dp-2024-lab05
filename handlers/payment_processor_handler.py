from handlers.base_handler import BaseHandler
from exceptions.payment_processing_error import PaymentProcessingError


class PaymentProcessorHandler(BaseHandler):
    """
    Обработчик процесса оплаты.
    """

    def handle(self, order: dict) -> None:
        """
        Обрабатывает запрос на оплату.

        :param order: Словарь с данными запроса, содержащий информацию о заказе.
        """
        if order["payment"] == 0:
            raise PaymentProcessingError
        print("На счету достаточно средств.")
        super().handle(order)
