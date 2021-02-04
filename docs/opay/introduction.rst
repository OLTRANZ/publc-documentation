
#####################################
Getting Started with OPAY payment API
#####################################

Oltranz **OPAY PAYMENT API** was created to allow people who have e-commerce businesses or whoever wants to integrate OPAY payment in his/her system to accept payments from **MTN Mobile Money**, **Tigo Cash** and **Airtel Money** with one and unified solution independently of the payment service provider.

Once integrated in the system, payment request will be forwarded from the client application to **OLTRANZ OPAY** system which will take care of contacting the paying person Payment Service Provider and ask him/her to pay **OPAY merchant** the specified amount.

*****************
Intended Audience
*****************

This API documentation is for any developer who is looking for an easy to integration and to use Mobile Payment API. It can be used for any kind application which is able to handle RESTFUL APIs.

********************************************
Requirements to start using OPAY payment API
********************************************

No starting fee is required. All the user/developer has to do is to create merchant account (done online) at the end of which he/she will be given a merchantId (merchant Id) to be used for subsequent payment requests.

The minimum payment request amount is ``100 RWF (one hundred Rwandan Francs)`` and the maximum is ``2,000,000 RWF (two millions Rwanda Francs)`` per day for each payer. But the merchant can be paid any amount of money per day.

OPAY allows merchants to be paid for all collected amount without 24 hours. For that the merchant has to contact oltranz and sign a contract after which he/she will share his/sher banking details and all collected amount will be sent to the specified bank account every single day.

