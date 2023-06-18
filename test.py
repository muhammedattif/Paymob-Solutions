# First Party Imports
from paymob.accept.callbacks import AcceptCallback

incoming_hmac = "94812480175cb046b20324c293abf067f78627cbb4f5db80e61d71e2314f0ba70cce56a34ee1c56614fad5b0653345d46e18b55f2cb9d1cdf08b4ecb78dc2f82"
callback = {
    "type": "TRANSACTION",
    "obj": {
        "id": 109628234,
        "pending": False,
        "amount_cents": 1000,
        "success": True,
        "is_auth": False,
        "is_capture": False,
        "is_standalone_payment": True,
        "is_voided": False,
        "is_refunded": False,
        "is_3d_secure": False,
        "integration_id": 3871725,
        "profile_id": 787951,
        "has_parent_transaction": False,
        "order": {
            "id": 126087094,
            "created_at": "2023-06-01T21:45:56.993153",
            "delivery_needed": False,
            "merchant": {
                "id": 787951,
                "created_at": "2023-05-14T19:41:48.955870",
                "phones": ["+201028362012"],
                "company_emails": [],
                "company_name": "Mahmoud",
                "state": "",
                "country": "EGY",
                "city": "Cairo",
                "postal_code": "",
                "street": "",
            },
            "collector": None,
            "amount_cents": 1000,
            "shipping_data": {
                "id": 61920183,
                "first_name": "Brett",
                "last_name": "Roberts",
                "street": "NA",
                "building": "NA",
                "floor": "NA",
                "apartment": "NA",
                "city": "NA",
                "state": "NA",
                "country": "NA",
                "email": "swsz2qbisz@amenli.com",
                "phone_number": "01550272164",
                "postal_code": "NA",
                "extra_description": "",
                "shipping_method": "UNK",
                "order_id": 126087094,
                "order": 126087094,
            },
            "currency": "EGP",
            "is_payment_locked": False,
            "is_return": False,
            "is_cancel": False,
            "is_returned": False,
            "is_canceled": False,
            "merchant_order_id": "lead_20__1685645156",
            "wallet_notification": None,
            "paid_amount_cents": 0,
            "notify_user_with_email": False,
            "items": [],
            "order_url": "https://accept.paymob.com/standalone/?ref=i_LRR2Q3VHeUtzaTBFb0xSdG0rRVY2YzA4dz09X0JLelBTZElyRXRpM3hkR0tHU1RDQlE9PQ",
            "commission_fees": 0,
            "delivery_fees_cents": 0,
            "delivery_vat_cents": 0,
            "payment_method": "tbc",
            "merchant_staff_tag": None,
            "api_source": "OTHER",
            "data": {},
        },
        "created_at": "2023-06-01T21:45:57.830530",
        "transaction_processed_callback_responses": [
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': 'd1cde7b7-5fda-4ea4-9d3b-ddc9b12ff94e', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Thu, 01 Jun 2023 18:46:17 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-01T18:46:17.484494",
            },
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': 'd94f0ad8-37c7-4fc5-bec5-0fe484657093', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Sat, 17 Jun 2023 00:09:39 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-17T00:09:39.778552",
            },
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': 'da022fab-09c5-43ae-abf8-29623b3defaf', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Sat, 17 Jun 2023 00:15:22 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-17T00:15:22.832033",
            },
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': '21672fb8-e480-4073-b5e2-a1fb954c4ead', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Sat, 17 Jun 2023 00:16:59 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-17T00:16:59.202569",
            },
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': 'cc7e6e29-36b0-450b-ae03-917537e9a63d', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Sat, 17 Jun 2023 00:25:49 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-17T00:25:49.627892",
            },
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': 'bf562c77-5466-4118-9b6c-adfa0e8cc71d', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Sat, 17 Jun 2023 14:53:05 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-17T14:53:05.334883",
            },
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': '2a14e5cd-0f90-49f5-9d0b-839dbc244d77', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Sat, 17 Jun 2023 14:53:12 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-17T14:53:12.429113",
            },
            {
                "response": {
                    "status": "200",
                    "content": "None",
                    "headers": "{'Server': 'nginx', 'Content-Type': 'text/plain; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Vary': 'Accept-Encoding', 'X-Request-Id': '5c81c509-7cfd-4504-81dd-5d14fb80c45b', 'X-Token-Id': 'ac84f01e-0bc5-41d3-be08-b5b3912f8148', 'Cache-Control': 'no-cache, private', 'Date': 'Sat, 17 Jun 2023 14:53:32 GMT', 'Content-Encoding': 'gzip'}",
                    "encoding": "UTF-8",
                },
                "callback_url": "https://webhook.site/ac84f01e-0bc5-41d3-be08-b5b3912f8148",
                "response_received_at": "2023-06-17T14:53:32.162453",
            },
        ],
        "currency": "EGP",
        "source_data": {
            "pan": "01010101010",
            "type": "wallet",
            "sub_type": "wallet",
            "owner_name": None,
            "phone_number": "01010101010",
        },
        "api_source": "OTHER",
        "terminal_id": None,
        "merchant_commission": 0,
        "installment": None,
        "discount_details": [],
        "is_void": False,
        "is_refund": False,
        "data": {
            "klass": "WalletPayment",
            "token": "",
            "amount": 1000,
            "method": 0,
            "message": "Transaction has been completed successfully.",
            "currency": "EGP",
            "created_at": "2023-06-01T18:45:57.876617",
            "mpg_txn_id": "213412341",
            "order_info": "swsz2qbisz@amenli.com",
            "uig_txn_id": "4351324134",
            "upg_txn_id": None,
            "mer_txn_ref": "3871725_3fb960d3f7495a998f8984e89b978f10",
            "redirect_url": "https://accept.paymobsolutions.com/api/acceptance/wallet_other_test/wallet_template?token=ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklsUnlZVzV6WVdOMGFXOXVJaXdpZEhKaGJuTmhZM1JwYjI1ZmNHc2lPakV3T1RZeU9ESXpOQ3dpYzNWaVgzUjVjR1VpT2lKM1lXeHNaWFFpZlEuaXZRb3pMRlhkMVl5OWphUW4zZ0hYeTZCTXNQaXdYQmQ3dTN1VXd0djJMNlFmaHdXdGw5SGFLNjZxd2RQd2Y3SHNUZDlUR3F2aE5jeDFEUEJ2TnQtUmc=",
            "wallet_issuer": "VODAFONE",
            "wallet_msisdn": "01010101010",
            "gateway_source": "",
            "upg_qrcode_ref": "4351324134",
            "txn_response_code": "200",
            "gateway_integration_pk": 3871725,
        },
        "is_hidden": False,
        "payment_key_claims": {
            "extra": {},
            "pmk_ip": "197.62.181.81",
            "user_id": 1363533,
            "currency": "EGP",
            "order_id": 126087094,
            "amount_cents": 1000,
            "billing_data": {
                "city": "NA",
                "email": "swsz2qbisz@amenli.com",
                "floor": "NA",
                "state": "NA",
                "street": "NA",
                "country": "NA",
                "building": "NA",
                "apartment": "NA",
                "last_name": "Roberts",
                "first_name": "Brett",
                "postal_code": "NA",
                "phone_number": "01550272164",
                "extra_description": "NA",
            },
            "integration_id": 3871725,
            "lock_order_when_paid": False,
            "single_payment_attempt": False,
        },
        "error_occured": False,
        "is_live": False,
        "other_endpoint_reference": "4351324134",
        "refunded_amount_cents": 0,
        "source_id": -1,
        "is_captured": False,
        "captured_amount": 0,
        "merchant_staff_tag": None,
        "updated_at": "2023-06-17T17:53:32.176405",
        "is_settled": False,
        "bill_balanced": False,
        "is_bill": False,
        "owner": 1363533,
        "parent_transaction": None,
    },
    "transaction_processed_callback_responses": "",
}

token_callback = {
    "type": "TOKEN",
    "obj": {
        "id": 10,
        "token": "d20d94...8000687835c3f1a9da9",
        "masked_pan": "xxxx-xxxx-xxxx-2346",
        "merchant_id": 1,
        "card_subtype": "MasterCard",
        "created_at": "2016-12-26T06:49:18.017207Z",
        "email": "test@email.com",
        "order_id": "55",
    },
}

delivery_callback = {
    "type": "DELIVERY_STATUS",
    "obj": {
        "order_id": 5530,
        "order_delivery_status": "Scheduled",
        "merchant_id": 455,
        "merchant_name": "Test Merchant",
        "updated_at": "2017-01-24T13:29:40",
    },
}
callback = AcceptCallback(incoming_hmac=incoming_hmac, callback_dict=callback)
print(f"Callback: {callback}")
print(f"Callback Type: {callback.type}")
print(f"Obj id: {callback.obj.id}")
print(f"HMAC Check: {callback.is_valid}")  # Do the HMAC Check
# hmac = HMACValidator(
#     incoming_hmac=incoming_hmac,
#     callback_dict=callback,
# )
# print(hmac.is_valid)
# accept = AcceptAPIClient()

# code, transaction, feedback = accept.get_order(
#     order_id=128466640,
# )
# print(f"Code: {code}")
# print(f"Transaction: {transaction}")
# print(f"Feedback Message: {feedback.message}")
# print(f"Feedback Data: {feedback.data}")
# print(f"Feedback Status Code: {feedback.status_code}")

# trx = {
#    "id":111859918,
#    "pending":False,
#    "amount_cents":1000,
#    "success":False,
#    "is_auth":False,
#    "is_capture":False,
#    "is_standalone_payment":True,
#    "is_voided":False,
#    "is_refunded":False,
#    "is_3d_secure":False,
#    "integration_id":3871725,
#    "terminal_id":"None",
#    "has_parent_transaction":False,
#    "order":{
#       "id":128466640,
#       "created_at":"2023-06-11T14:11:56.610219",
#       "delivery_needed":False,
#       "merchant":{
#          "id":787951,
#          "created_at":"2023-05-14T19:41:48.955870",
#          "phones":[
#             "+201028362012"
#          ],
#          "company_emails":[

#          ],
#          "company_name":"Mahmoud",
#          "state":"",
#          "country":"EGY",
#          "city":"Cairo",
#          "postal_code":"",
#          "street":""
#       },
#       "collector":"None",
#       "amount_cents":1000,
#       "shipping_data":{
#          "id":63163429,
#          "first_name":"first_name",
#          "last_name":"last_name",
#          "street":"NA",
#          "building":"NA",
#          "floor":"NA",
#          "apartment":"NA",
#          "city":"NA",
#          "state":"NA",
#          "country":"NA",
#          "email":"email@gmail.com",
#          "phone_number":"1000000000",
#          "postal_code":"NA",
#          "extra_description":"",
#          "shipping_method":"UNK",
#          "order_id":128466640,
#          "order":128466640
#       },
#       "currency":"EGP",
#       "is_payment_locked":False,
#       "is_return":False,
#       "is_cancel":False,
#       "is_returned":False,
#       "is_canceled":False,
#       "merchant_order_id":"4441",
#       "wallet_notification":"None",
#       "paid_amount_cents":0,
#       "notify_user_with_email":False,
#       "items":[

#       ],
#       "order_url":"https://accept.paymob.com/standalone/?ref=i_LRR2WlRxTXBVTGlPOW9tWk11aE1CbXdjUT09X3V3Wjl1UHpZV1pkeEcwNHBwenJEbFE9PQ",
#       "commission_fees":0,
#       "delivery_fees_cents":0,
#       "delivery_vat_cents":0,
#       "payment_method":"tbc",
#       "merchant_staff_tag":"None",
#       "api_source":"OTHER",
#       "data":{

#       }
#    },
#    "created_at":"2023-06-11T14:12:16.582804",
#    "paid_at":"None",
#    "currency":"EGP",
#    "source_data":{
#       "pan":"010",
#       "type":"wallet",
#       "sub_type":"wallet",
#       "owner_name":"None",
#       "phone_number":"010"
#    },
#    "api_source":"OTHER",
#    "fees":"N/A",
#    "vat":"N/A",
#    "converted_gross_amount":"N/A",
#    "data":{
#       "message":"Invalid Mobile Number"
#    },
#    "is_cashout":False,
#    "wallet_transaction_type":"None",
#    "is_upg":False,
#    "is_internal_refund":False,
#    "billing_data":{
#       "id":83275207,
#       "first_name":"first_name",
#       "last_name":"last_name",
#       "street":"NA",
#       "building":"NA",
#       "floor":"NA",
#       "apartment":"NA",
#       "city":"NA",
#       "state":"NA",
#       "country":"NA",
#       "email":"email@gmail.com",
#       "phone_number":"1000000000",
#       "postal_code":"NA",
#       "ip_address":"",
#       "extra_description":"NA",
#       "transaction_id":111859918,
#       "created_at":"2023-06-11T14:12:16.595757"
#    },
#    "installment":"None",
#    "integration_type":"online_new",
#    "card_type":"wallet",
#    "routing_bank":"-",
#    "card_holder_bank":"-",
#    "merchant_commission":0,
#    "extra_detail":"None",
#    "discount_details":[

#    ],
#    "pre_conversion_currency":"None",
#    "pre_conversion_amount_cents":"None",
#    "is_host2host":False,
#    "installment_info":{
#       "items":"None",
#       "administrative_fees":"None",
#       "down_payment":"None",
#       "tenure":"None",
#       "finance_amount":"None"
#    },
#    "vf_loyalty_details":{

#    },
#    "purchase_fees":0,
#    "original_amount":1000,
#    "is_trx_bank_installment":False,
#    "is_void":False,
#    "is_refund":False,
#    "is_hidden":False,
#    "error_occured":False,
#    "is_live":False,
#    "other_endpoint_reference":"None",
#    "refunded_amount_cents":0,
#    "source_id":-1,
#    "is_captured":False,
#    "captured_amount":0,
#    "merchant_staff_tag":"None",
#    "updated_at":"2023-06-11T14:12:17.166506",
#    "is_settled":False,
#    "bill_balanced":False,
#    "is_bill":False,
#    "owner":1363533,
#    "parent_transaction":"None"
# }
# transaction_class = get_transaction_class()

# transaction = transaction_class(connection=1, **trx)
# print(transaction.order.items)
# print(transaction.order.shipping_data.id)
