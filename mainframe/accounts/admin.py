from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'Month', 'VENDOR_NAME', 'VENDOR_GSTIN', 'VENDOR_STATE_CODE', 'BRANCH_SOL_ID', 'BANK_GST_No', 'HSN',
        'NATURE_OF_SERVICE', 'PL_CODE', 'PL_DESCRIPTION', 'DATE_OF_INVOICE', 'INVOICE_No',
        'INVOICE_AMOUNT', 'CGST', 'SGST', 'IGST', 'TDS', 'TDS_SEC', 'TOTAL_AMOUNT', 'TRAN_ID', 'VENPAY_ID', 'TRAN_DATE')