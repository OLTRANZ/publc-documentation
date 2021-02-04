#######################
OPAY Money Transfer API
#######################

Money Transfer is a service offered to whoever would like to integrate their systems and be able to send money to mobile users, with money which will be deducted from their Opay Wallet. One has to register a Opay merchant and get merchant Id to begin use this service.

If you have a merchant Id and you want to integrate funds transfer functionality in your system, please contact Oltranz to get an access key

``POST /opay/wallet/fundstransfer``

Headers
=======

.. list-table::
    :header-rows: 1

    * - Name
      - Description
    * - accessKey
      - Service access key

Sample request object
=====================

.. code-block:: http

    POST /opay/wallet/fundstransfer HTTP/1.1
    Content-Type: application/json
    accessKey: 1f5a9bfe6cc611e9a8e49f13814dfe15
    Accept: application/json
    Host: localhost:8080
    Content-Length: 308

    {
      "merchantId": "4028810b67c1af1a0167c2073da60001",
      "receiverAccount": "400000000000012",
      "type": "BANK",
      "bankName": "BK",
      "transactionId": "c3c0eb866cb611e9a8e49f13814dfe15",
      "amount": 1000.0,
      "callbackUrl": "http://localhost:3000/callback",
      "description": "FUNDS TRANSFER TEST",
      "firstName": "Joe",
      "lastName": "DOE"
    }


Parameters description
======================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - merchantId
      - string
      - false
      - Merchant Id
    * - receiverAccount
      - String
      - false
      - Mobile Money or Bank account of the funds receiver
    * - transactionId
      - string
      - false
      - Transfer request transaction id. To avoid collusion better use UUID to generate this kind of transaction id
    * - amount
      - Double
      - false
      - Amount to be sent to the receiver
    * - callbackUrl
      - Double
      - false
      - Callback endpoint where transfer response will be sent
    * - description
      - string
      - true
      - Transactions Description to be sent to the receiver. Eg. Money From Jessica In USA
    * - firstName
      - string
      - true
      - First name of the receiver
    * - lastName
      - string
      - true
      - Last name of the receiver
    * - type
      - string
      - true
      - MOBILE or BANK
    * - bankName
      - string
      - true
      - Funds receiver bank name. To be specified only in case of transfer to bank account


Sample payment request object
=============================

.. code-block:: json

    {
      "code": "406",
      "description": "YOUR REQUEST CANNOT BE FULFILLED. INSUFFICIENT FUNDS",
      "body": null,
      "status": "INSUFFICIENT_FUNDS"
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
      - 201, 401, 402, 403, 404, 405, 406, 407
    * - status
      - String
      - false
      - PENDINg, FAILED, UNKNOWN_TRANSER_TYPE, NO_WALLET_FOUND, WALLET_HAS_NO_ACCESS_KEY, INVALID_ACCESS_KEY, UNKNOWN_TRANSER_TYPE, INSUFFICIENT_FUNDS, DUPLICATE_TRANSACTION_ID
    * - description
      - String
      - false
      - Further explanations about the request
    * - body
      - String
      - true
      - This part will be empty for this case

************************************
Callback for money transfer requests
************************************

The following is the callback response object which will be sent and funds transfer definitive response.

Sample callback response object
===============================

.. code-block:: json

    {
      "code": 200,
      "status": "SUCCESS",
      "description": "FUNDS TRANSFERRED SUCCESSFULLY",
      "transactionId": "c3c0eb866cb611e9a8e49f13814dfe15",
      "transferTransactionId": "1190080",
      "walletBalance": 15000.0,
      "transferedAmount": 1000.0,
      "commission": 25.0,
      "total": 1025.0
    }


Response parameters description
===============================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - code
      - integer
      - false
      - 200: SUCCESS and 401: FAILED
    * - status
      - string
      - false
      - SUCCESS or FAILED
    * - description
      - double
      - false
      - Description of the operation
    * - transactionId
      - Double
      - false
      - Unique identifier of the transaction
    * - transferTransactionId
      - string
      - true
      - Mobile payment operator money transfer reference. Value set only on successful transfer
    * - walletBalance
      - double
      - true
      - Remaining amount on the wallet. Value set only on successful transfer
    * - transferedAmount
      - double
      - true
      - Amount paid to the receiver
    * - commission
      - double
      - true
      - Charged commission
    * - total
      - double
      - true
      - Total cut to the wallet (transferred amount + commission)
