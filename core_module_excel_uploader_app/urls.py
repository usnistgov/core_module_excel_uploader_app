""" Url router for the excel uploader module
"""

from django.urls import re_path

from core_module_excel_uploader_app.views.views import ExcelUploaderModule

urlpatterns = [
    re_path(
        r"module-excel-uploader",
        ExcelUploaderModule.as_view(),
        name="core_module_excel_uploader_view",
    ),
]
