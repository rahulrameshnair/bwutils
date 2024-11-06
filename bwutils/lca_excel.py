"""
lca_excel.py

This module provides functions for exporting Life Cycle Assessment (LCA) calculation results
to an Excel format, with each result from an impact categort stored in a separate sheet, which is
a recurring theme in lca-related calculations.

Functions:
    - clean_sheet_name(name, max_length=30): Cleans and truncates sheet names for Excel compatibility.
    - result_to_excel(results, methods_of_interest, filename): Exports LCA results to an Excel file 
      with a final sheet summarizing impact assessment methods.

Dependencies:
    - pandas
    - openpyxl (since pandas does not automatically install this)

"""

import re
import os
import pandas as pd


def clean_sheet_name(name, max_length=30):
    """Cleans and truncates a sheet name to make it compatible with Excel's requirements.

    This function removes invalid characters, trims leading and trailing underscores,
    and ensures that the name does not exceed the specified maximum length.

    Args:
        name (str): The original sheet name that may contain invalid characters.
        max_length (int): Maximum allowed length for the sheet name. Defaults to 30.

    Returns:
        str: A cleaned and truncated version of the sheet name, compatible with Excel.
    """
    # Remove invalid characters and trim whitespace, quotes, and brackets
    name = re.sub(
        r"[\\/*?:\[\]']", "_", name
    )  # Replace invalid characters with underscores
    name = re.sub(r"[(),]", "", name)  # Remove parentheses and commas
    name = name.strip("_")  # Remove leading/trailing underscores
    return name[:max_length]  # Ensure the name does not exceed the maximum length


def result_to_excel(results, methods_of_interest, filename):
    """Exports LCA calculation results to an Excel file, with each result in a separate sheet.

    This function takes a dictionary of LCA calculation results, each associated with a specific
    impact assessment method, and writes them to separate sheets in an Excel file. Additionally,
    it creates a final sheet with details of the impact assessment methods such as
    method names, impact categories, and units.

    Args:
        results (dict): A dictionary where keys are method names (or other identifiers) and
            values are pandas DataFrames containing LCA results for each method.
        methods_of_interest (list of tuples): A list of tuples, each containing:
            - Method Name (str): The name of the impact assessment method.
            - Impact Category (str): The impact category associated with the method.
            - Unit (str): The unit of measurement for the impact category.
        filename (str): The path where the Excel file should be saved.

    Returns:
        str: The absolute path to the saved Excel file.

    """
    impact_assessment_methods_df = pd.DataFrame(
        methods_of_interest,
        columns=["Method Name", "Impact category (i.e sheet name here)", "Unit"],
    )
    with pd.ExcelWriter(filename) as writer:
        for method, df in results.items():
            sheet_name = clean_sheet_name(str(method))
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        # Add impact assessment methods as the final sheet
        impact_assessment_methods_df.to_excel(
            writer, sheet_name="IA Methods", index=False
        )
    file_path = os.path.abspath(filename)
    print(f"Results written to {file_path}")
