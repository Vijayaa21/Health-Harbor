import pandas as pd
from PIL import Image
import google.generativeai as genai

# Load your CSV file
df = pd.read_csv("Food X Drugs - Sheet1.csv")

def drug_name(image_file):
    # Configure Google API
    genai.configure(api_key='AIzaSyDbbIVTyxNOsfyM6vuE9uFa-LQ2yuyoaNY')

    # Open and process the uploaded image
    img = Image.open(image_file)

    # Initialize GenerativeModel
    model = genai.GenerativeModel('gemini-pro-vision')

    # Generate drug name from image
    response = model.generate_content(["What is the name of the drug (scientific) (salt name)? Answer only the drug name. ", img], stream=True)
    response.resolve()
    t = response.text.strip().replace(" ", "")

    # Find matching rows in the DataFrame
    matching_rows = df.loc[df['DRUG'] == t]

    # Extract good and bad items
    good_items = matching_rows['GOOD'].str.split(',').explode().str.strip().tolist()
    bad_items = matching_rows['BAD'].str.split(',').explode().str.strip().tolist()

    return good_items, bad_items
