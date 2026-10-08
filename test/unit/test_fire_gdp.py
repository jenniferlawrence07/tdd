import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src")
    )
)

import fire_gdp  # noqa: E402


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        header = ["Country", "1990", "1991"]
        result = fire_gdp.get_column_index(header, "1990")
        self.assertEqual(result, 1)

    def test_name_absent(self):
        header = ["Country", "1990", "1991"]
        result = fire_gdp.get_column_index(header, "2000")
        self.assertIsNone(result)

    def test_empty_header(self):
        header = []
        result = fire_gdp.get_column_index(header, "1990")
        self.assertIsNone(result)


class TestGetData(unittest.TestCase):

    def test_get_all_rows(self):
        file_name = os.path.join(
            os.path.dirname(__file__),
            "../data/test_co2.csv"
        )

        rows = fire_gdp.get_data(file_name)

        self.assertEqual(len(rows), 4)
        self.assertEqual(rows[0], ["Brazil", "2004", "14437.5351"])

    def test_query_rows(self):
        file_name = os.path.join(
            os.path.dirname(__file__),
            "../data/test_co2.csv"
        )

        rows = fire_gdp.get_data(
            file_name,
            query_column=0,
            query_value="Brazil"
        )

        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0][0], "Brazil")

    def test_return_header(self):
        file_name = os.path.join(
            os.path.dirname(__file__),
            "../data/test_co2.csv"
        )

        header, rows = fire_gdp.get_data(
            file_name,
            return_header=True
        )

        self.assertEqual(
            header,
            ["Area", "Year", "Forest fires"]
        )
        self.assertEqual(len(rows), 4)


class TestGetFireGdpYearData(unittest.TestCase):

    def test_matching_years(self):
        co2_file = os.path.join(
            os.path.dirname(__file__),
            "../data/test_co2.csv"
        )
        gdp_file = os.path.join(
            os.path.dirname(__file__),
            "../data/test_gdp.csv"
        )

        result = fire_gdp.get_fire_gdp_year_data(
            co2_file,
            gdp_file,
            "Brazil"
        )

        expected = [
            [2004, 14437.5351, 1957751.20],
            [2005, 18253.5232, 2170584.50],
            [2006, 8342.4547, 2409449.90]
        ]

        self.assertEqual(result, expected)

    def test_missing_values_are_skipped(self):
        co2_file = os.path.join(
            os.path.dirname(__file__),
            "../data/test_co2.csv"
        )
        gdp_file = os.path.join(
            os.path.dirname(__file__),
            "../data/test_gdp.csv"
        )

        result = fire_gdp.get_fire_gdp_year_data(
            co2_file,
            gdp_file,
            "Afghanistan"
        )

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
