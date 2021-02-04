#################################
Sending SMS using SMS Gateway API
#################################

As it has been mentioned before, sending via Oltranz SMS Gateway is very easy because only two values are to be specified; receiver and message.

The following is a sample object

The following is the object which is to be received by your application, operate on it and send the same object (having added the response and the type of action only).

``POST /oltranz/smsgateway/send/customer/<customerId>``

Sample object
=============

.. code-block:: json

    {
      "receiver": "250784456259",
      "message": "Test the documentation"
    }

Request object parameter desription
===================================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - receiver
      - string
      - false
      - Phone number of the SMS recipient
    * - message
      - string
      - false
      - Message to the recipient

Response object
===============

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json;charset=UTF-8
    Content-Length: 154

    {
      "code" : "401",
      "description" : "YOUR ACCOUNT DOES NOT HAVE ENOUGH CREDIT TO SATISFY THE REQUEST. PURCHASE NEW SMS AND TRY AGAIN",
      "body" : null
    }

Response object parameters description
======================================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - code
      - string
      - false
      - ode is an indication on whether sms was successfully sent or not. Value 200 is SUCCESS and value 401 is FAILED
    * - description
      - string
      - false
      - Further description about what happened
    * - body
      - null
      - true
      - Normally contains additional


.. note::

    **Getting customerId**
    Customer Id will be sent via email upon account registration on Oltranz SMS Gateway webportal. If no email is received, please contact oltranz to obtain both credentials and customer Id.
