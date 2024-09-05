import unittest
import pandas as pd
import os
from etl_example1 import extract_data, transform_data, load_data

class TestEtlExample1Process(unittest.TestCase):
    def setUp(self):
        # Test the creation of a dataframe
        self.df = extract_data()
        
    def test_extract_data(self):
        df = extract_data()
        # Here we are testing the length of the dataframe (col)
        self.assertEqual(len(df), 5)
        # Here we are testing the existing of a dataframe
        self.assertIsInstance(self.df, pd.DataFrame)
        # Here we are testing the column names
        important_columns = ["name", "salary", "has_car"]
        for col in important_columns:
            self.assertIn(col, df.columns, f"Column '{col}' should be present")

    def test_transform_data(self):
        # Here we are testing the value of average salary and the filtered data
        avg_salary, filtered_data = transform_data(self.df)
        # Here we are testing the average salary
        self.assertAlmostEqual(avg_salary, 750)
        # Here we are testing the length of the filtered data
        decimalPlace = 2
        message = "Calculated Average Salary and Manual Average Salary are almost not equal."
        self.assertAlmostEqual(avg_salary, 750, decimalPlace, message)
        self.assertTrue((filtered_data['has_car'] == True).all())

    def test_load_data(self):
        avg_salary, filtered_data = transform_data(self.df)
        # Here we are testing the path of average salary and filtered data
        avg_salary_path, filtered_data_path = load_data(avg_salary, filtered_data)
        # Here we are testing the existence of the file
        self.assertTrue(os.path.exists(avg_salary_path))
        self.assertTrue(os.path.exists(filtered_data_path))
        # Check file content for avearge salary
        avg_salary_df = pd.read_csv(avg_salary_path)
        self.assertEqual(avg_salary_df.iloc[0]["average_salary"], avg_salary)
        # Check file content for filtered data
        filtered_data_df = pd.read_csv(filtered_data_path)
        self.assertEqual(len(filtered_data_df), 3)
        # Clean up files
        os.remove(avg_salary_path)
        os.remove(filtered_data_path)   

if __name__ == "__main__":
    unittest.main()

