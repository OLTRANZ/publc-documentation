#############################
USSD request/response objects
#############################

The following is the object which is to be received by your application, operate on it and send the same object (having added the response and the type of action only).

****************************************
Sample request going to USSD application
****************************************

.. code-block:: json

    {
      "sessionId": "13245200800899890",
      "serviceCode": "123",
      "phoneNumber": "250780000001",
      "text": "",
      "response": "",
      "action": "CON",
      "transactionId": "",
      "requestTime": "2019-01-01 02:10:10",
      "newRequest": 0,
      "charge": "N",
      "amount": 0.0
    }

************************************************
Sample response coming from the USSD application
************************************************

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json;charset=UTF-8
    Content-Length: 291

    {
        "sessionId" : "13245200800899890",
        "serviceCode" : "123",
        "phoneNumber" : "250780000001",
        "text" : "",
        "response" : "UNKOWN APPLICATION",
        "action" : "END",
        "transactionId" : "",
        "requestTime" : "2019-01-01 02:10:10",
        "newRequest" : 1,
        "charge" : "N",
        "amount" : 0.0
    }

**************************************
Description of USSD application object
**************************************

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - sessionId
      - string
      - false
      - The session Id value which is set by the handling telecommunication company. This stays same for the entire session.
    * - serviceCode
      - string
      - false
      - The service short code. Eg. \*123# or \*123\*100#.
    * - phoneNumber
      - string
      - false
      - Telephone number of the person using the USSD service.
    * - text
      - string
      - false
      - The input from the user. Note that USSD is stateless. This means that text value will the the currently entered input from the user not the history of all previous inputs
    * - response
      - string
      - true
      - The response back to the user. This can be the next menu the user has to go trough to accomplish the whole process
    * - action
      - string
      - false
      - Action is an indication to the gateway whether the session is on-going or has to end. Action can have two values which are 'CON' or 'END'. CON is short for CONTINUE. Set value to END only and only if you want the session to end.
    * - transactionId
      - string
      - true
      - Transaction value set from the USSD application side. This value is optional
    * - requestTime
      - string
      - false
      - Request time in the following format: yyyy-MM-dd HH:mm:ss
    * - newRequest
      - number
      - true
      - This value will be set to 1 the very first time the request is received and then set to 0 for additional requests which use the same session number
    * - charge
      - string
      - true
      - Indication whether the session is charged. The parameter can take two values which are Y for Yes and N for No. By default the value is set to N
    * - amount
      - number
      - true
      - If session is charged, this parameter contains the amount to be charged per session. The default value is 0

.. note::

    **No endpoint to send response to?**

    Note that there is no endpoint to send response to but rather send a response to the incoming request will suffice. As the USSD application will be operating as server (please refer to the client-side server architecture), the USSD Gateway which will be working as a client will send a request to your application through the endpoint (URL) mapped to the gateway. Your application will receive the request and simply return a response. And this makes working with Oltranz USSD Gateway far more easier.
