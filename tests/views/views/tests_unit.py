""" Unit tests for core_module_excel_uploader_app views.
"""
from unittest import TestCase

from core_module_excel_uploader_app.views.views import ExcelUploaderModule


class TestExcelUploaderModuleIsTableValid(TestCase):
    """Unit tests for `TestExcelUploaderModule.is_table_valid` method."""

    def test_is_table_valid_without_name_returns_false(self):
        """test_is_table_valid_without_name_returns_false"""
        excel_uploader_module = ExcelUploaderModule()
        is_valid = excel_uploader_module.is_table_valid(None, {})
        self.assertFalse(is_valid)

    def test_is_table_valid_with_bad_table_type_returns_false(self):
        """test_is_table_valid_with_bad_table_type_returns_false"""
        excel_uploader_module = ExcelUploaderModule()
        is_valid = excel_uploader_module.is_table_valid("name", "table")
        self.assertFalse(is_valid)

    def test_is_table_valid_with_incorrect_keys_returns_false(self):
        """test_is_table_valid_with_missing_key_returns_false"""
        excel_uploader_module = ExcelUploaderModule()
        is_valid = excel_uploader_module.is_table_valid(
            "name", {"headers": [], "val": []}
        )
        self.assertFalse(is_valid)

    def test_is_table_valid_with_correct_keys_returns_true(self):
        """test_is_table_valid_with_correct_keys_returns_true"""
        excel_uploader_module = ExcelUploaderModule()
        is_valid = excel_uploader_module.is_table_valid(
            "name", {"headers": [], "values": []}
        )
        self.assertTrue(is_valid)
