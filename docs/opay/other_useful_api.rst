#################
Other Useful APIs
#################

The following are the APIs which can help one to change user password as a functionality embedded directly in his/her application be it web or mobile.

**************
Reset Password
**************

It may happen that the person forget his/her password to the point that accessing OPAY services becomes impossible. In fact the majority of services offered by OPAY require strong authentication.

In that case OPAY offers a user-friendly service to reset password through a functionality commonly known as forgot-password. This service is only available two the users with an-existing OPAY account.

************************
Password Reset Procedure
************************

The password recovery is done into two phases which are Forgot password and reset password.

***************
Forgot Password
***************

In this phase, the user sends a request to OPAY system notifying that he/she has lost the password and would like to set it. All the user has to do is to specify his/her email and if the email is found existing in the system, OPAY will forward send a passcode to him/her via his email. Thus as developer you should be able to tell to the user to look check their emails and discover the passcode. It is the passcode which will help them to then reset passwords.

The following are sample forgot-password request and response samples.

``POST https://opay-api.oltranz.com/opay/forgotpassword?email=usermail``

Sample forgot password response
===============================

.. code-block:: json

    {
      "code": "200",
      "description": "Request to change password processed successfully",
      "body": null
    }

Response fields description
===========================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - code
      - string
      - false
      - 200: SUCCESS and 401 : FAILED
    * - description
      - string
      - false
      - Further explainations about the request.
    * - body
      - string
      - true
      - Containts additional data to be shared with the user. But it will be null for this request


**************
Reset Password
**************

It is during this phase that the actual action of reseting password happen. The request will require only two parameters which are the passcode (the one sent via email) and the new password.

.. note::

    **Passcode validity:** the passcode has a validity period of 24 hrs only and it can be use only once.

.. warning::

    **Strong password only!**

    OPAY only requires strong passwords thus the user which to reset his/her password have to ensure that the new password meets all characteristics of a strong password which are: The password should be 8 characters long having the following:

    * At least 1 lower case character
    * At least 1 UPPER CASE character
    * At least 1 numeric digit (numbers)
    * At least 1 special character: allowed special characters are: ! @ # $ % ^ & + = _ -

``POST https://opay-api.oltranz.com/opay/password/reset``

.. code-block:: http

    POST /opay/password/reset HTTP/1.1
    Content-Type: application/json
    Accept: application/json
    Host: localhost:8080
    Content-Length: 65

    {
      "passcode" : "5433543224553",
      "newPassword" : "P@ssw0rd!"
    }

Parameters description
======================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - passcode
      - string
      - false
      - Upon successful password reset request, the passcode is sent to the user’s email.
    * - newPassword
      - String
      - false
      - The new Password of the user. The new password has to fulfill the following criteria: 1. At least 8 characters long. It must have at least 1 lower case, upper case (capital), numeric digit (numbers), special character. The allowed special characters are: ! @ # $ % ^ & + = _ - (any of these)


Sample response
===============

.. code-block:: json

    {
      "code": "401",
      "description": "Attempt with to reset password with invalid activation token",
      "body": null
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
      - string
      - false
      - 200: SUCCESS and 401 : FAILED
    * - description
      - String
      - false
      - Further explainations about the request.
    * - body
      - string
      - true
      - Containts additional data to be shared with the user. But it will be null for this request


***************
Change Password
***************

Change password API allows to the user who want to change their current password to go ahead and change it without any reason. But the new password to be supposed should mean the same strop password requirements as for the password reset functionality.

.. warning:: 

    Change password requires that the identity of the user be known ahead of time. This is the reason why authentication is required here. Once user authenticated, the access-token will be sent as **Authorization header** value.

``POST https://opay-api.oltranz.com/opay/password/users/changepassword``


Headers
=======

.. list-table::
    :header-rows: 1

    * - Name
      - Description
    * - Authorization
      - The access Token received upon login


Sample request
==============

.. code-block:: http

    POST /opay/users/change/password HTTP/1.1
    Content-Type: application/json
    Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsib2F1dGgyLXJlc291cmNlIl0sInVzZXJfbmFtZSI6ImpvZWRvZUBnbWFpbC5jb20iLCJzY29wZSI6WyJyZWFkIiwid3JpdGUiLCJ0cnVzdCJdLCJleHAiOjE1NDYwMTQ1NDIsImF1dGhvcml0aWVzIjpbIlJPTEVfVVNFUiJdLCJqdGkiOiI0OGM3ZmQxMi04NTQ3LTRmZTUtYjZhYS0xYzFjNWM5YTMwZTciLCJjbGllbnRfaWQiOiIkMmEkMDYkWkFPbXNCYlVldGIuOU1mV2VnTDBjZVV2SWJqUzVMWjdrZlN2Q3hFTWZBVFRtZzdwRkxqaEcifQ.0AtoNSAF-XZj68-GphTcvWlmlIbijrR8l53VQLq8dkU
    Accept: application/json
    Host: localhost:8080
    Content-Length: 63

    {
      "oldPassword" : "Opay@123",
      "newPassword" : "P@ssw0rd!"
    }


Parameters description
======================

.. list-table::
    :header-rows: 1

    * - Parameter
      - Type
      - Optional
      - Description
    * - oldPassword
      - string
      - false
      - The password you want to be changed.
    * - newPassword
      - string
      - false
      - The new password should fulfill requirements of a strong password which are: 1. It should be at least 8 characters long . It should have at least 1 lower case character, upper case, numeric digit (number), special characters. The allowed special chracters are ! @ # $ % ^ & + = _


Sample response
===============

.. code-block:: json

    {
      "code": "401",
      "description": "Failure to provide valid old Password",
      "body": null
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
      - string
      - false
      - 200: SUCCESS and 401 : FAILED
    * - description
      - string
      - false
      - Further explainations about the request.
    * - body
      - string
      - true
      - Containts additional data to be shared with the user. But it will be null for this request
