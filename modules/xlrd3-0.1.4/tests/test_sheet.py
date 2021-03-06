#!/usr/bin/env python
# Author:  mozman <mozman@gmx.at>
# Purpose: test sheet functions
# Created: 03.12.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

import sys
import os
import unittest

import xlrd3

def from_tests_dir(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

SHEETINDEX = 0
NROWS = 15
NCOLS = 13

ROW_ERR = NROWS + 10
COL_ERR = NCOLS + 10

class TestSheet(unittest.TestCase):
    book = xlrd3.open_workbook(from_tests_dir('profiles.xls'), formatting_info=True)
    sheetnames = ['PROFILEDEF', 'AXISDEF', 'TRAVERSALCHAINAGE', 'AXISDATUMLEVELS', 'PROFILELEVELS']

    def check_sheet_function(self, function):
        self.assertTrue(function(0, 0))
        self.assertTrue(function(NROWS-1, NCOLS-1))

    def check_sheet_function_index_error(self, function):
        self.assertRaises(IndexError, function, ROW_ERR, 0)
        self.assertRaises(IndexError, function, 0, COL_ERR)

    def check_col_slice(self, col_function):
        _slice = col_function(0, 2, NROWS-2)
        self.assertEqual(len(_slice), NROWS-4)

    def check_row_slice(self, row_function):
        _slice = row_function(0, 2, NCOLS-2)
        self.assertEqual(len(_slice), NCOLS-4)

    def test_nrows(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.assertEqual(sheet.nrows, NROWS)

    def test_ncols(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.assertEqual(sheet.ncols, NCOLS)

    def test_cell(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.assertNotEqual(xlrd3.empty_cell, sheet.cell(0, 0))
        self.assertNotEqual(xlrd3.empty_cell, sheet.cell(NROWS-1, NCOLS-1))

    def test_cell_error(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_sheet_function_index_error(sheet.cell)

    def test_cell_type(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_sheet_function(sheet.cell_type)

    def test_cell_type_error(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_sheet_function_index_error(sheet.cell_type)

    def test_cell_value(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_sheet_function(sheet.cell_value)

    def test_cell_value_error(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_sheet_function_index_error(sheet.cell_value)

    def test_cell_xf_index(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_sheet_function(sheet.cell_xf_index)

    def test_cell_xf_index_error(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_sheet_function_index_error(sheet.cell_xf_index)

    def test_col(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        col = sheet.col(0)
        self.assertEqual(len(col), NROWS)

    def test_row(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        row = sheet.row(0)
        self.assertEqual(len(row), NCOLS)

    def test_col_slice(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_col_slice(sheet.col_slice)

    def test_col_types(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_col_slice(sheet.col_types)

    def test_col_values(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_col_slice(sheet.col_values)

    def test_row_slice(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_row_slice(sheet.row_slice)

    def test_row_types(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_row_slice(sheet.col_types)

    def test_row_values(self):
        sheet = self.book.sheet_by_index(SHEETINDEX)
        self.check_col_slice(sheet.row_values)

if __name__=='__main__':
    unittest.main()