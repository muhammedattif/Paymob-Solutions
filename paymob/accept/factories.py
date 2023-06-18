# First Party Imports
from paymob.utils import ClassFactory

DynamicTransactionFactory = ClassFactory("Transaction")
Order = ClassFactory("Order")
Invoice = ClassFactory("Invoice")
Product = ClassFactory("Product")
DeliveryStatusCallbackFactory = ClassFactory("DeliveryStatusCallback")
CardTokenCallbackFactory = ClassFactory("CardTokenCallback")
