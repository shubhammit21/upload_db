from django.db import models


class Person(models.Model):
    Month = models.CharField(max_length=100, null=True)
    VENDOR_NAME = models.CharField(max_length=100, null=True)
    VENDOR_GSTIN = models.CharField(max_length=100, null=True)
    VENDOR_STATE_CODE = models.CharField(max_length=100, null=True)
    BRANCH_SOL_ID = models.CharField(max_length=100, null=True)
    BANK_GST_No = models.CharField(max_length=100, null=True)
    HSN = models.CharField(max_length=100, null=True)
    NATURE_OF_SERVICE = models.CharField(max_length=100, null=True)
    PL_CODE = models.CharField(max_length=100, null=True)
    PL_DESCRIPTION = models.CharField(max_length=100, null=True)
    DATE_OF_INVOICE = models.CharField(max_length=100, null=True)
    INVOICE_No = models.CharField(max_length=100, null=True)
    INVOICE_AMOUNT = models.FloatField(max_length=50, null=True)
    CGST = models.FloatField(max_length=50, null=True)
    SGST = models.FloatField(max_length=50, null=True)
    IGST = models.FloatField(max_length=50, null=True)
    TDS = models.CharField(max_length=50, null=True)
    TDS_SEC = models.CharField(max_length=100, null=True)
    TOTAL_AMOUNT = models.FloatField(max_length=20, null=True)
    TRAN_ID = models.CharField(max_length=100, null=True)
    VENPAY_ID = models.CharField(max_length=100, null=True)
    TRAN_DATE = models.CharField(max_length=100, null=True)