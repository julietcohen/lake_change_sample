# identify, document, and remove rows with an Na value in any column in lake change input data
# and save the cleaned files to a new directory
# using conda env perm_ground

import geopandas as gpd
import pandas as pd
from pathlib import Path
import os

# collect all lake_change.gpkg filepaths in Ingmar's data
base_dir = Path('/home/pdg/data/nitze_lake_change/data_2022-11-04/lake_change_GD/')
filename = 'lake_change.gpkg'
# To define each .gpkg file within each subdir as a string representation with forward slashes,
# use as_posix()
# The ** represents that any subdir string can be present between the base_dir and the filename
input = [p.as_posix() for p in base_dir.glob('**/' + filename)]
print(f"Collected {len(input)} lake_change.gpkg filepaths.")

# import each filepath as a gdf
# document which rows have Na (as a separate csv for each input gpkg)
# drop any row with an Na value is any column
# next step: also drop any rows with inf values!
# for test runs, try 1 file:
input_subset = input[0:1]

for path in input_subset:
    print(f"Checking file {path}.")
    gdf = gpd.read_file(path)

    # first identify any rows with NA to document which are dropped
    drop_na_rows = []
    for index, row in gdf.iterrows():
        if row.isnull().any():
            drop_na_rows.append(row)
    # convert the list of rows to a dataframe
    drop_na_df = pd.DataFrame(drop_na_rows)

    # hard-code the start of the path to directory for the cleaned data
    filepath_start = "/home/jcohen/lake_change_GD_workflow/workflow_cleaned/invalid_data_documentation/"
    # next, pull the last couple parts of filepath to ID which lake_change.gpkg
    # is being processed, following Ingmar's directory hierarchy
    directory, filename = os.path.split(path)
    filepath_sections = directory.split(os.sep)
    relevant_sections = filepath_sections[-2:]
    partial_filepath = relevant_sections[0] + "/" + relevant_sections[1]
    full_filepath = filepath_start + partial_filepath + "/drop_na_rows.csv"
    # make the subdirectories if they do not yet exist
    directory_path = os.path.dirname(full_filepath)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    # save the df of rows with NA values as a csv
    drop_na_df.to_csv(full_filepath, index = False)
    print(f"Saved rows with NA for lake change GDF:\n{path}\nto file:\n{full_filepath}")

    # drop the rows with Na in any column
    gdf.dropna(axis = 0, inplace = True)

    # save cleaned lake change file to new directory
    # (we are not overwriting the original lake change file)
    # hard-code the start of the path to directory for the cleaned data
    filepath_start = "/home/jcohen/lake_change_GD_workflow/workflow_cleaned/cleaned_files/"
    # next, pull the last couple parts of filepath to ID which lake_change.gpkg
    # is being processed, following Ingmar's directory hierarchy
    directory, filename = os.path.split(path)
    filepath_sections = directory.split(os.sep)
    relevant_sections = filepath_sections[-2:] + ['lake_change_cleaned_na.gpkg']
    filepath_end = relevant_sections[0] + "/" + relevant_sections[1] + "/" + relevant_sections[2]
    full_filepath = filepath_start + filepath_end
    print(f"Saving file to {full_filepath}")
    # make the subdirectories if they do not yet exist
    directory_path = os.path.dirname(full_filepath)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    gdf.to_file(full_filepath, driver = "GPKG") 

print(f"Cleaning complete.")


