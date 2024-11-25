from command.process_order_command import ProcessOrderCommand
from handlers.delivery_handler import DeliveryHandler
from handlers.order_handler import OrderHandler
from handlers.payment_processor_handler import PaymentProcessorHandler
from handlers.stock_check_handler import StockCheckHandler
from exceptions.delivery_error import DeliveryError
from exceptions.out_of_stock_error import OutOfStockError
from exceptions.payment_processing_error import PaymentProcessingError

inventory = {
    "item1": 10,
    "item2": 0,  # Товар отсутствует
}

# Пример заказа
order = {"item": "item1", "payment": 100, "address": "UGATU"}

# Создание цепочки обработчиков
stock_check_handler = StockCheckHandler(inventory)
payment_processor_handler = PaymentProcessorHandler()
delivery_handler = DeliveryHandler()
order_handler = OrderHandler()

order_handler.set_next(stock_check_handler).set_next(
    payment_processor_handler
).set_next(delivery_handler)
try:
    command = ProcessOrderCommand(order_handler, order)
    command.execute()
except (OutOfStockError, PaymentProcessingError, DeliveryError) as e:
    print(f"Ошибка во время обработки заказа: {e}")
