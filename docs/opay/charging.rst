#####################################
OPAY Charging and Testing Environment
#####################################

****************
Service Charging
****************

OPAY payment requests are charged by transactions. For each payment request done through OPAY, OLTRANZ charges ``2.5% (two and half percent)`` of the total paid amount. This means that if the payer paid ``100 RWF``, the commission charged by OLTRANZ will be ``2.5 RWF`` and the remaining for the merchant will be ``97.5 RWF``.

*****************
Testing with OPAY
*****************

OPAY offers a testing environment where developers can play with all APIs listed in this document before they launch into production. Working with OPAY testing environment will give to developers confidence to fully test all possible APIs again OPAY backend in order to be confident by they time they go live with their own systems.

.. note::

    **Payments on testing env**

    While OPAY provides a testing environment, we are sorry we do not offer the possibility to test payments without engaging real money at telecommunication partnering companies. This is the reason why we will guarantee that payments can be done with lower amounts (at testing environments), no more that 100 RWF.

    We will over also the possibility to migrate from testing to production. It is the migration from testing to environment which will make all money used during testing liquidable (payable back to the testing entity).
