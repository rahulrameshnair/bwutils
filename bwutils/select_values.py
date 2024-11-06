"""
select_values.py

This module provides some functions for LCA workflows in Jupyter notebook
which require numerous user inputs such as selecting or changing impact assessment methods.

"""

import ipywidgets as widgets
from IPython.display import display
import os


def result_folders(folder_path, result_direcs):
    """Creates folders for storing results if they do not already exist.

    Args:
        folder_path (str): The base folder path where result directories should be created.
        In Windows, use double backslash to enter the path. Eg. "D:\\test"
        result_direcs (list of str): A list of folder/directory names to create within the base folder.
    Prints:
        str: A message indicating the location of folders that were created.
    """

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Base folder created at: {os.path.abspath(folder_path)}")
    else:
        print(f"Base folder already exists at: {os.path.abspath(folder_path)}")
        # creates directories for storing results with in the base folder.
    for direc in result_direcs:
        sub_folder_path = os.path.join(folder_path, direc)
        if not os.path.exists(sub_folder_path):
            os.mkdir(sub_folder_path)
            print(f"Subfolder created at: {os.path.abspath(sub_folder_path)}")
        else:
            print(f"Subfolder already exists at: {os.path.abspath(sub_folder_path)}")


def single_select_dropdown(names):
    """Creates a single-selection dropdown widget for users to select an option.

    Args:
        names (list of str): A list of names/options to be displayed in the dropdown.

    Returns:
        dict: A dictionary containing the selected value with the key 'value'.
    """

    if not names:
        raise ValueError("The 'names' list cannot be empty.")

    dropdown = widgets.Dropdown(
        options=names,
        value=names[0],  # Default value
        description="Assessment methodology:",
        disabled=False,
    )

    # Display the dropdown widget
    display(dropdown)

    # Variable to store the selected value
    selected_value = {"value": dropdown.value}

    # Function to update the selected value
    def on_change(change):
        selected_value["value"] = change["new"]
        print(f"You selected: {selected_value['value']}")

    # Attach the function to the dropdown
    dropdown.observe(on_change, names="value")

    return selected_value


def multi_select_dropdown(names):
    """Creates a multi-selection dropdown widget for users to select multiple options.

    Args:
        names (list of str): A list of names/options to be displayed in the multi-select widget.

    Returns:
        dict: A dictionary containing the selected values with the key 'values'.
    """

    if not names:
        raise ValueError("The 'names' list cannot be empty.")

    height_of_each_dropdown_item = (
        20  # sets a default height in pixel for dropdown items
    )
    dropdown_box_height = (
        len(names) * height_of_each_dropdown_item + 20
    )  # estimates the total height of the drop down window based on the total number of items.
    multi_select = widgets.SelectMultiple(
        options=names,
        value=[],  # Default value, an empty list
        description="Impact Categories:",
        disabled=False,
        layout=widgets.Layout(width="100%", height=f"{dropdown_box_height}px"),
    )

    # Display the multiple selection widget
    display(multi_select)

    # Variable to store the selected values
    selected_values = {"values": multi_select.value}

    # Function to update the selected values
    def on_change_multiple_selection(change):
        selected_values["values"] = list(change["new"])
        print(f"You selected: {selected_values['values']}")

    # Attach the function to the multiple selection widget
    multi_select.observe(on_change_multiple_selection, names="value")

    return selected_values
