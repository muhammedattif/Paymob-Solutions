class AcceptCallbackTypes:
    TRANSACTION = "TRANSACTION"
    CARD_TOKEN = "TOKEN"
    DELIVERY_STATUS = "DELIVERY_STATUS"


class PaymentSubTypes:
    AGGREGATOR = "AGGREGATOR"
    WALLET = "WALLET"
    CASH = "CASH"
    TOKEN = "TOKEN"


class DeliveryStatuses:
    SCHEDUALED = "Scheduled"
    CONTACTING_MERCHANT = "Contacting Merchant"
    PICKING_UP = "Picking Up"
    COURIER_RECEIVED = "Courier Received"
    AT_WAREHOUSE = "At Warehouse"
    AGENT_OUT = "Agent Out"
    ON_ROUTE = "On Route"
    AT_CUSTOMER = "At Customer"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"
    DELIVERY_FAILED = "Delivery Failed"
    RETURN_SCHEDULED = "Return Scheduled"
    PACKAGE_RETURNED = "Package Returned"
