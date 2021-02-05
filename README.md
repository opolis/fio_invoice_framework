# Fio Invoice Framework
ETHDenver 2021 framework for the FIO Invoice Integration Bounty with Opolis

## Goal
The goal of this project is to integrate the `fio_invoice_framework.models.Invoice` model  with the [FIO Request network](https://fioprotocol.io/).
- Pay payroll invoices, as issued by Opolis, with crypto from a member’s LLC to an Opolis FIO Address in DAI, USDT, or USDC
- Give the Opolis platform the ability to issue a FIO Request for an invoice to be paid in DAI, USDT, or USDC by a Member LLC
 

## Models
Below are the stripped down versions of Opolis's database models. Please use these models as guidelines for building
the project, however, do not feel restricted by these models. Feel free to add more Models or fields to existing models if needed. 
 
> `django.contrib.auth.models.User`

This is django's default User model. You can find more details [here](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#user-model).
All auth data related to Opolis's members is stored in this model.

> `fio_invoice_framework.models.MemberLLC`

This models contains the [LLC](https://en.wikipedia.org/wiki/Limited_liability_company) data of registered users. This model has the following fields:

- `user`: foreignkey to `django.contrib.auth.models.User`. This is the owner of the LLC.
- `name`: Legal name of the LLC.
- `created_at`: The time when the instance was created.
- `updated_at`: The time when the instance was modified.

> `fio_invoice_framework.models.Payment`


This model contains all payment related information for an invoice. This model has the following fields:

- `status`: This indicates the status of the invoice. The payment could be in the either of these state: Pending, Failed, Completed.
- `type`: Payment can of the following type: ACH, Crypto, Cheque.
- `amount`: The amount paid. 
- `currency`: The currency of the payment.
- `exchange_rate_in_usd`: Exchange rate in USD when the payment was made.
- `external_unique_id`: A unique identifier for the payment made. eg. This could be transaction hash when making payments in crypto.
- `created_at`: The time when the instance was created.
- `updated_at`: The time when the instance was modified.


> `fio_invoice_framework.models.Invoice`

This model contains all invoice related information for a MemberLLC
- `member_llc`: Foreign key to `fio_invoice_framework.models.MemberLLC` for whom the Invoice was issued. 
- `status`: Indicates the current status of the invoice.
- `type`: Invoice can be of type Payroll or Bonus. 
- `payment_amount`: The invoice amount.
- `due_date`: Invoice due date.
- `payment`: This is a ManyToManyField to `fio_invoice_framework.models.Payment`. The invoice amount could be split into several payments.
- `created_at`: The time when the instance was created.
- `updated_at`: The time when the instance was modified.

## Installation and setup
 a. clone the repo `https://github.com/opolis/fio_invoice_framework/`
 > git clone https://github.com/opolis/fio_invoice_framework.git
 
 b. install the requirements in a virtualenv
 > pip install -e .
 
 c. run the migrations
 > python manage.py migrate

##Deliverables:
- Fork and add support for the above features to the specified repository

- Update the Readme with a brief explanation of your solution, and any additional documentation you wish to provide

- Write tests as needed to show your system is functional

- Only applications written in Python and Django will be considered

- Include failure states and status tracking of the invoice and their payments

##Resources:

- https://developers.fioprotocol.io/

- https://developers.fioprotocol.io/api/api-spec

- https://github.com/fioprotocol/fiosdk_typescript
