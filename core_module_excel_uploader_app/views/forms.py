""" Excel Uploader forms
"""
from django import forms


class ExcelUploaderForm(forms.Form):
    """Excel Uploader Form"""

    file = forms.FileField(label="Select Excel File")
