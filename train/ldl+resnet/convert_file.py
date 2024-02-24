import pandas as pd
import os 

# Load the Excel file
parent_path = os.path.dirname(os.getcwd())
rating_path = os.path.join(parent_path, "dataset", "SCUT-FBP5500_v2", "All_Ratings.xlsx")

xlsx_file = pd.ExcelFile(rating_path)

csv_dir = os.path.join(parent_path, "dataset", "SCUT-FBP5500_v2")

# Define the list of rating files
rating_files = ['female_white_images.csv',
                'female_yellow_images.csv',
                'male_white_images.csv',
                'male_yellow_images.csv',
                'remainder_images.csv']

# Iterate through each sheet in the Excel file and save it as a CSV file
for sheet_name, csv_file in zip(xlsx_file.sheet_names, rating_files):
    df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
    csv_path = os.path.join(csv_dir, csv_file)
    df.to_csv(csv_path, index=False)