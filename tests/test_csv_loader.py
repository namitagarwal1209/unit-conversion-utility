"""
Tests csv_loader -> csv file loading + conversion graph creation.
Temporary CSV files are used so tests do not modify the real units.csv file.

"""

import unittest
import tempfile
import os

from csv_loader import load_csv


class TestCSVLoader(unittest.TestCase):

    #craeting temp csv files for tests
    def create_temp_csv(self, content):

        temp_file = tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            newline=""
        )

        temp_file.write(content)
        temp_file.close()

        return temp_file.name
    
    #TEST 1
    def test_forward_and_reverse_conversion(self):

        csv_content = (
            "SourceUnit,TargetUnit,Factor\n"
            "meter,feet,3.28084\n"
        )

        file_path = self.create_temp_csv(csv_content)

        try:
            graph = load_csv(file_path) #create graph

            self.assertAlmostEqual(graph["meter"]["feet"],3.28084) #test forward conversion

            self.assertAlmostEqual(graph["feet"]["meter"],1 / 3.28084) #test reverse conversion

        finally:
            os.remove(file_path) #remove the temp csv file that was created to test

    #TEST 2
    def test_invalid_factor(self):

        csv_content = (
            "SourceUnit,TargetUnit,Factor\n"
            "meter,feet,hello\n"
        )

        file_path = self.create_temp_csv(csv_content)

        try:
            with self.assertRaises(ValueError):
                load_csv(file_path)

        finally:
            os.remove(file_path)


    #TEST 3
    def test_zero_factor(self):

        csv_content = (
            "SourceUnit,TargetUnit,Factor\n"
            "meter,feet,0\n"
        )

        file_path = self.create_temp_csv(csv_content)

        try:
            with self.assertRaises(ValueError):
                load_csv(file_path)

        finally:
            os.remove(file_path)