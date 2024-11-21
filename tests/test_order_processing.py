import unittest

from exceptions.delivery_error import DeliveryError
from exceptions.out_of_stock_error import OutOfStockError
from exceptions.payment_processing_error import PaymentProcessingError
from handlers.delivery_handler import DeliveryHandler
from handlers.order_handler import OrderHandler
from handlers.payment_processor_handler import PaymentProcessorHandler
from handlers.stock_check_handler import StockCheckHandler
from command.process_order_command import ProcessOrderCommand


class TestOrderProcessing(unittest.TestCase):
    """
    Класс для тестирования обработки заказов в системе.
    """

    def setUp(self):
        """
        Инициализирует тестовые данные: заказ и инвентарь.
        """
        self.order = {"item": "item1", "payment": 100, "address": "UGATU"}
        self.inventory = {
            "item1": 10,
            "item2": 0,
        }

    def test_stock_check_handler(self):
        """
        Тестирует обработчик проверки наличия товара.
        """
        handler = StockCheckHandler(self.inventory)
        order_handler = OrderHandler()
        order_handler.set_next(handler)
        command = ProcessOrderCommand(order_handler, self.order)
        try:
            command.execute()
            result = True
        except OutOfStockError:
            result = False
        self.assertTrue(result)

    def test_payment_processor_handler(self):
        """
        Тестирует обработчик платежей.
        """
        self.order["payment"] = 0
        handler = StockCheckHandler(self.inventory)
        payment_handler = PaymentProcessorHandler()
        order_handler = OrderHandler()
        order_handler.set_next(handler).set_next(payment_handler)
        command = ProcessOrderCommand(order_handler, self.order)
        with self.assertRaises(PaymentProcessingError):
            command.execute()

    def test_delivery_handler(self):
        """
        Тестирует обработчик доставки.
        """
        self.order["address"] = ""
        stock_check_handler = StockCheckHandler(self.inventory)
        payment_processor_handler = PaymentProcessorHandler()
        delivery_handler = DeliveryHandler()
        order_handler = OrderHandler()
        order_handler.set_next(stock_check_handler).set_next(
            payment_processor_handler
        ).set_next(delivery_handler)
        command = ProcessOrderCommand(order_handler, self.order)
        with self.assertRaises(DeliveryError):
            command.execute()


if __name__ == "__main__":
    unittest.main()
