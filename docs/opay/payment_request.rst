########################
OPAY Payment Request API
########################

***************
Payment Request
***************
Making a payment request with OPAY is very easy. With the merchant Id obtained upon merchant registration, the following API allows you to do mobile payment request either to MTN mobile money, Tigo Cash or Airtel money. All you have is to specify the telephone number of the payer and OPAY will do the job to determine which mobile payment operator will be handling your request.

.. note::

    **Response to the request**

    Note that payment is accomplished in many steps and that the payer may take longer to complete the payment. This is the reason why payment cannot be completed immediately but rather a bit later. The immediate response that will be given on the payment request will be an indication whether your request is in PENDING (with code value of 200) status ( meaning that the mobile payment operation is waiting for th payer to complete the payment), or if it has failed due to different reason such as the fact that mentionned account does not exist, the payer does not have enough resources to complete payment and so on.

``POST https://opay-api.oltranz.com/opay/paymentrequest``


Sample object
=============

.. code-block:: http

    POST /opay/paymentrequest HTTP/1.1
    Content-Type: application/json
    Accept: application/json
    Host: localhost:8080
    Content-Length: 290

    {
      "telephoneNumber" : "250780000001",
      "amount" : 100.0,
      "organizationId" : "4028810b67c1af1a0167c2073da60001",
      "description" : "Payment for Printing services",
      "callbackUrl" : "http://myonlineprints.com/payments/callback",
      "transactionId" : "ffe037792fc5a11e8b4a4663af0064a00"
    }

Payment request object parameters description
=============================================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - telephoneNumber
      - string
      - false
      - Payer Telephone Number
    * - amount
      - Number
      - false
      - Amount to be Paid
    * - organizationId
      - string
      - false
      - Merchant Id
    * - description
      - string
      - true
      - Payment request description message
    * - callbackUrl
      - String
      - true
      - Payment completed callback endpoint or url
    * - transactionId
      - string
      - false
      - Payment Transaction ID. Using UUID recommended


Sample payment request object
=============================

.. code-block:: json

    {
      "code": "401",
      "description": "DUPLICATED TRANSACTION ID ffe037792fc5a11e8b4a4663af0064a00",
      "body": null,
      "status": "DUPLICATED_TRANSACTION_ID"
    }

Payment request object parameters description
=============================================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - code
      - String
      - false
      - 200: SUCCESS and 401 : FAILED
    * - status
      - String
      - false
      - Possible values are the following: + ([SUCCESS, PENDING] → code=200), + ([UNKNOWN_ACCOUNT,TIMEOUT, DECLINED, ERRONEOUS, FAILURE, INVALID_PIN, ACCOUNT_NOT_ACTIVE, BELOW_MINIMUM_ALLOWED_AMOUNT, NO_SUFFICIENT_FUNDS, ACCOUNT_NOT_FOUND, ABOVE_MAXIMUM_ALLOWED_AMOUNT, DUPLICATED_TRANSACTION_ID] → code=401)
    * - description
      - String
      - false
      - Detailed info about the status
    * - body
      - string
      - true
      - Containts the object about PENDING payment request
    * - body.transactionId
      - string
      - true
      - Payment Request transaction Id


************************
Payment Request Callback
************************

As mentioned earlier, the payment request takes time to be completed at Mobile Payment Service Operator, in average it takes between 5 and 10 seconds between the time the payer receives the payment request prompt message and the moment he/she entered the PIN to confirm the payment.

For this, the OPAY merchant system has to have an implemented mechanism to question OPAY system to know if the payment is completed. Though, this task can be accomplished in a variety of ways, the easiest and less complicated on the side of the merchant is to use a callback.

Callback will be an endpoint (a web-service) which will be implemented on the system of the merchant side to accept the object below. The endpoint of that web-service will be put in the payment request object (please refer to the payment request object for the callback path).

Thus, the callback web-service should be made to accept the object below.

.. note::

    **Callback endpoint/url**

    It has been shown that when it comes to callback endpoint, many are those who does not it immediately that by callback endpoint, we mean the endpoint in their backend where we will be posting (the callback endpoint should implement POST HTTP Method) results of some computation on our end.

    Normally callbacks are used to avoid blocking events on the side of clients. Whenever there is an event which takes long, it is recommended to use callback mechanisms rather to overcome the problem of long waits on the client.

    The callback can be set once in the OPAY system backend once for all for a given merchant (if he/she wants things to be done so). But the merchant is free to send callback on every single payment request and the callback in the payment request is given higher priority compared to the endpoint which existed on the OPAY system.


Sample payment request callback object
======================================

.. code-block:: json

    {
      "statusDescription": "PAID DONE SUCCESSFULLY",
      "spTransactionId": "1189008900089",
      "walletTransactionId": "142bd904043011e989e1a30736f9425c",
      "chargedCommission": 2.5,
      "currency": "RWF",
      "paidAmount": 100,
      "transactionId": "ffe037792fc5a11e8b4a4663af0064a00",
      "statusCode": "200",
      "status": "SUCCESS"
    }

Payment request callback object parameters description
======================================================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - transactionId
      - string
      - false
      - The transaction Id sent during the payment request
    * - walletTransactionId
      - string
      - false
      - Transaction Id in Oltranz Wallet
    * - spTransactionId
      - String
      - false
      - Transaction Id at Mobile Money Operator
    * - paidAmount
      - Double
      - false
      - Amount paid by the payer
    * - chargedCommission
      - Double
      - false
      - The commission charged by Oltranz
    * - currency
      - string
      - false
      - Currency. RWF for instance
    * - statusCode
      - string
      - false
      - 200 for Success and 401 for anything else
    * - status
      - string
      - false
      - SUCCESS or FAILED
    * - statusDescription
      - string
      - false
      - Further explanation of what happened
