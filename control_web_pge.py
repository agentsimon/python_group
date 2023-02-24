import pandas as pd
import os
# Load the CSV file into a dataframe
df = pd.read_csv(r"/home/simonhyde/Documents/stable-diffusion-ui-linux/stable-diffusion-ui/male_items.csv",  engine ='python')

# Create a new column in the dataframe
df['Image'] = ""

# Change the folder name !!!
csv_files = [file for file in os.listdir('/home/simonhyde/Stable Diffusion UI/1677164210378') if file.endswith('.png')]
csv_files =csv_files.sort()
# Loop through the rows in the dataframe
row_number =0
for model_image in csv_files:   
    print(model_image)
    df.at[row_number,'Image'] = model_image
    row_number += 1

df.to_csv("finished_men.csv", sep=',')
