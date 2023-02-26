'''
Written in haste. 
There are two methods used for the timing, a standard sleep.time and 
WebDriver Wait method. The latter is more elegant but I haven't changed all the time.sleep(web_page_time) implementations.

Things to add or change. Slect only show 4 images on the main generator window.
Turn of the sound 
Image size, sampler and model on each run. ?Also inference steps and guidance scale? Latter more important
'''
# Import the pandas library
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import subprocess
import shlex
# delay time
web_page_time = 1
# processing time
process_time = 35

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
pd.options.mode.chained_assignment = None  

#  Set up the correct values
def set_up():
# Go to the settings and set up values
    settings_button = browser.find_element("id", "tab-settings")
    settings_button.click()
    time.sleep(web_page_time)
# Select the vram usage to low
    select = Select(browser.find_element("id",'vram_usage_level'))
    time.sleep(web_page_time)
    select.select_by_value('low')
    time.sleep(web_page_time)
# Turn on the auto save images toggle
    settings_save = browser.find_element(By.XPATH, '//*[@id="save_to_disk"]') 
    time.sleep(web_page_time)
# Select the auto save option
    if settings_save.is_selected() == False:
        #print("We have the settings save button")
        #print("Location: ", settings_save.location)
        browser.execute_script("arguments[0].click();", settings_save)

    time.sleep(web_page_time)

# Go to the main Generate window and set up the values
    settings_button = browser.find_element("id", "tab-main")
    settings_button.click()
    time.sleep(web_page_time)
 # select the prompt and clear it
    prompt_name = browser.find_element("id", "prompt")
    browser.find_element('id', "prompt").clear()
    time.sleep(web_page_time)
    print("Cleared")
# Add the negative prompt 
    prompt_clear = browser.find_element("id", "negative_prompt_handle")
    time.sleep(web_page_time)
    prompt_clear.click()
    prompt_name_negative = "worst quality, low quality, normal quality, low resolution), blurry, text, artist name, signature, multiple views, out of frame, thumbnail, preview, obscured, distorted, blurry, blurred, out of focus low-res, low resolution, bad quality, artifacts, low detail, no detail, corrupted"
    input = browser.find_element("id","negative_prompt")
    input.send_keys(prompt_name_negative)
    time.sleep(web_page_time)
# Select the model
    input = browser.find_element("id","editor-settings")
    time.sleep(web_page_time)
    input.click()
    time.sleep(web_page_time)
    settings_button2 = browser.find_element("id", "stable_diffusion_model")
    time.sleep(web_page_time)
# identify dropdown for model and select
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "stable_diffusion_model"))))
    select.select_by_visible_text("v1-5-pruned")
 # identify dropdown for sampler and select
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "sampler_name"))))
    select.select_by_visible_text("DPM++ 2m")
# Turn on fix faces toggle
    settings_save = browser.find_element(By.XPATH, '//*[@id="use_face_correction"]') 
    time.sleep(web_page_time)
    # Select the auto save option
    if settings_save.is_selected() == False:
        #print("We have the settings save button")
        #print("Location: ", settings_save.location)
        browser.execute_script("arguments[0].click();", settings_save)
# identify dropdown for image type and select
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "output_format"))))
    select.select_by_visible_text("jpeg")

# Set the image size width
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "width"))))
    select.select_by_visible_text("576")
# Set the image size height
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "height"))))
    select.select_by_visible_text("768 (*)")


# Main Body starts here
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("http://localhost:9000/")
browser.maximize_window()
# Run the set up function
set_up()

# Load the CSV file into a dataframe
df = pd.read_csv("/home/simonhyde/Documents/stable-diffusion-ui-linux/stable-diffusion-ui/Countries_and_Cities.csv",  engine ='python')

# Create a new column in the dataframe
df['Country_Capital_Model'] = ""
for col in df.columns:
    print(col)


count_row = df.shape[0]  # Gives number of rows
df['Country_Capital_Model'] = ""
print("Number of rows ",count_row)

#for model_image in range(count_row):
for model_image in range(count_row):
    print(model_image)
    prompt_name ="male traditional costume"
    print("Here", df.iloc[model_image,0], " ", df.iloc[model_image,1])
    prompt_name =  str(df.iloc[model_image,0]), str(df.iloc[model_image,1]) +" " +prompt_name 
    complete = ' '.join(prompt_name)
    print("Prompt is ", complete)
    df.at[model_image,'Title'] = complete
 # Finding the search field by id
    input = browser.find_element("id","prompt")
    input.send_keys(complete)
# click on the Make image button
    button = browser.find_element("id","makeImage")
    button.click()
# Wait for the image to be made which will be auto saved
    time.sleep(process_time)
    # Set only show 4 images only once
    if model_image == 1:
        input = browser.find_element("id","madrang-plugin-keep-max")
        input.clear()
        value_images = 4
        input.send_keys(value_images)
        time.sleep(web_page_time)
    else:
        pass
     # select the prompt and clear it
    #Clear the prompt window
    browser.find_element('id', "prompt").clear()
    time.sleep(web_page_time)
    print("Cleared")


# Add the get created images form the folder and add the file names to a new column called Images
subfolders = [ f.path for f in os.scandir('/home/simonhyde/Stable Diffusion UI/') if f.is_dir() ]
print("Folders are ", subfolders)
folder_to_look_in = max(subfolders,key=os.path.getctime)
print("Name of folder is", folder_to_look_in)


csv_files = [file for file in os.listdir(folder_to_look_in) if file.endswith('.jpeg')]
print("Unsorted list ",csv_files)
csv_files2 =sorted(csv_files)
print("Sorted list of pngs",csv_files2)
# Loop through the rows in the dataframe
row_number =0
for model_image in range(len(csv_files2)):   
    df.at[row_number,'Image'] = csv_files2[model_image]
    row_number += 1

df.to_csv("latest_csv_feed_list.csv", sep=',')
print("We have finished")
browser.close()
