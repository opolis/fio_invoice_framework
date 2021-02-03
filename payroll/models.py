from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Payment(BaseModel):

    PAYMENT_STATUS_PENDING = 'PENDING'
    PAYMENT_STATUS_FAILED = 'FAILED'
    PAYMENT_STATUS_COMPLETED = 'COMPLETED'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
        (PAYMENT_STATUS_COMPLETED, 'Completed'),
    ]

    PAYMENT_TYPE_DWOLLA_ACH = 'ACH'
    PAYMENT_TYPE_CRYPTO = 'CRYPTO'
    PAYMENT_TYPE_CHEQUE = 'CHEQUE'
    PAYMENT_TYPE_CHOICES = [
        (PAYMENT_TYPE_DWOLLA_ACH, 'ACH'),
        (PAYMENT_TYPE_CRYPTO, 'ETH'),
        (PAYMENT_TYPE_CHEQUE, 'Cheque'),
    ]
    PAYMENT_CURRENCY_TYPE_USD = 'USD'
    PAYMENT_CURRENCY_TYPE_ETH = 'ETH'
    PAYMENT_CURRENCY_TYPE_DAI = 'DAI'
    PAYMENT_CURRENCY_TYPE_BTC = 'BTC'

    PAYMENT_CURRENCY_TYPES = [
        (PAYMENT_CURRENCY_TYPE_USD, 'USD'),
        (PAYMENT_CURRENCY_TYPE_ETH, 'ETH'),
        (PAYMENT_CURRENCY_TYPE_DAI, 'DAI'),
        (PAYMENT_CURRENCY_TYPE_BTC, 'BTC'),
    ]

    status = models.CharField(null=True, blank=True, max_length=25, choices=PAYMENT_STATUS_CHOICES)
    payment_type = models.CharField(max_length=100, choices=PAYMENT_TYPE_CHOICES, null=True, blank=True)
    amount = models.DecimalField(null=True, blank=True, decimal_places=20, max_digits=40, default=None)
    currency = models.CharField(null=True, max_length=10, choices=PAYMENT_CURRENCY_TYPES)

    # external tx id like tx_hash
    external_unique_id = models.CharField(max_length=200, null=True)

    timestamp_created = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)


class Payroll(BaseModel):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='payroll')

    STATUS_PENDING = 'STATUS_PENDING'
    STATUS_PAYMENT_SCHEDULED = 'STATUS_PAYMENT_SCHEDULED'
    STATUS_PAYMENT_PENDING = 'STATUS_PAYMENT_PENDING'
    STATUS_FAILED = 'STATUS_FAILED'
    STATUS_COMPLETED = 'STATUS_COMPLETED'
    STATUS_CANCELLED = 'STATUS_CANCELLED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PAYMENT_PENDING, 'Payment Pending'),
        (STATUS_PAYMENT_SCHEDULED, 'Payment Scheduled'),
        (STATUS_FAILED, 'Failed'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    TYPE_PAYROLL = 'TYPE_PAYROLL'
    TYPE_BONUS = 'TYPE_BONUS'

    TYPE_CHOICES = [
        (TYPE_PAYROLL, 'Payroll'),
        (TYPE_BONUS, 'Bonus'),
    ]

    status = models.CharField(null=True, blank=True, max_length=25, choices=STATUS_CHOICES)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES, default=TYPE_PAYROLL)
    payment_amount = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=14, default=None)
    due_date = models.DateTimeField(null=True, blank=True)

    # an invoice could be split into multiple payments
    payment = models.ManyToManyField(Payment)
