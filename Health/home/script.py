import pandas as pd
from PIL import Image
import google.generativeai as genai

# Load your CSV file
df = pd.read_csv("Food X Drugs - Sheet1.csv")

def drug_name(image):
    import google.generativeai as genai



    genai.configure(api_key='AIzaSyDbbIVTyxNOsfyM6vuE9uFa-LQ2yuyoaNY')

    

    import PIL.Image

    img = PIL.Image.open(image)
    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content(["what is the name of drug(scientific)(salt name)? Answer only drug name. ", img], stream=True)
    response.resolve()
    t = response.text
    t=t.replace(" ","")
    
    return [t]

def get_dietd(drug):
    good = []
    bad = []
    for n in drug:
        matching_rows = df.loc[df['DRUG'] == n]
        good_items = matching_rows['GOOD'].str.split(',').explode().str.strip().tolist()
        bad_items = matching_rows['BAD'].str.split(',').explode().str.strip().tolist()
        good.extend(good_items)
        bad.extend(bad_items)
        
    good_set = set(good)
    new= []
    
    for i in good_set:
        new.append([good.count(i),i])
        
    new.sort(reverse=True)
    good = []
    
    for i in new:
        good.append(i[1])
    
    bad_set = set(bad)
    new= []
    
    for i in bad_set:
        new.append([bad.count(i),i])
        
    new.sort(reverse=True)
    bad = []
    
    for i in new:
        bad.append(i[1])
    
    temp_good= good[:]
    
    for i in good:
        if i in bad:
            bad.remove(i)
            temp_good.remove(i)
        
    good = temp_good[:]
    
    return good,bad