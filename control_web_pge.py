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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time
import os
import subprocess
import shlex

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Start time is ", current_time)
# delay time
web_page_time = 1
# processing time
process_time = 35

# Put the prompt here as prompt name
prompt_name =""
fine_tune =""
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
# Turn of the meta data saving 
    select = Select(browser.find_element("id", 'metadata_output_format'))
    time.sleep(web_page_time)
    select.select_by_value('none')
    time.sleep(web_page_time)
# Turn on the auto save images toggle
    settings_save = browser.find_element(By.XPATH, '//*[@id="save_to_disk"]') 
    time.sleep(web_page_time)
# Select the auto save option
    if settings_save.is_selected() == False:
        browser.execute_script("arguments[0].click();", settings_save)
    time.sleep(web_page_time)
# Turn off the sound toggle
    settings_save = browser.find_element(By.XPATH, '//*[@id="sound_toggle"]') 
    time.sleep(web_page_time)
# Select the auto save option
    if settings_save.is_selected() == True:
        print("Here in the sound")
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
    prompt_name_negative = "hat,wand, fuuin no tsue, holding, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, bad feet"
    input = browser.find_element("id","negative_prompt")
    input.send_keys(prompt_name_negative)
    time.sleep(web_page_time)
# Select the model
    input = browser.find_element("id","editor-settings")
    time.sleep(web_page_time)
    input.click()
    time.sleep(web_page_time)
# identify Model dropdown for model and select V1-5-pruned
    pick_model = browser.find_element("id", "stable_diffusion_model")
    time.sleep(web_page_time)
    pick_model.click()
    options = browser.find_elements(By.XPATH, "//li[@style='display: list-item;']")
    for option in options:
        if option.text == "v1-5-pruned":
            option.click()
            break
# identify VAE Model dropdown for model and select V1-5-pruned
    pick_model = browser.find_element("id", "vae_model")
    time.sleep(web_page_time)
    pick_model.click()
    options = browser.find_elements(By.XPATH, "//li[@style='display: list-item;']")
    for option in options:
        if option.text == "euler_a":
            option.click()
            break
 
# Turn on fix faces toggle
    settings_save = browser.find_element(By.XPATH, '//*[@id="editor-settings-entries"]/div[2]/ul/li[3]/div[1]/label') 
    settings_save.click()
    time.sleep(web_page_time)

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
df = pd.read_csv("/home/simon/Documents/Python/scrape/Countries_and_Cities.csv",  engine ='python')

# Create a new column in the dataframe
df['Country_Capital_Model'] = ""
for col in df.columns:
    print(col)


count_row = df.shape[0]  # Gives number of rows
df['Country_Capital_Model'] = ""
print("Number of rows ",count_row)

print("The prompt is ", prompt_name)
time.sleep(3)
file_name = prompt_name
for model_image in range(count_row):
    print(model_image)
    print("Here", df.iloc[model_image,0], " ", df.iloc[model_image,1])
    prompt_name2 =  str(df.iloc[model_image,0]), str(df.iloc[model_image,1]) +" " +prompt_name 
    complete = ' '.join(prompt_name2)  
    print("Prompt is ", complete)
# Add the name of the prompt to the column Title
    df.at[model_image,'Title'] = complete
 # Finding the search field by id
    input = browser.find_element("id","prompt")
    input.send_keys(complete)
# click on the Make image button
    button = browser.find_element("id","makeImage")
    button.click()
# Wait for the image to be made which will be auto saved
    time.sleep(process_time)
     # select the prompt and clear it
    #Clear the prompt window
    browser.find_element('id', "prompt").clear()
    time.sleep(web_page_time)
    print("Cleared")


# AFind the colder with the images in
subfolders = [ f.path for f in os.scandir('/home/simon/Stable Diffusion UI') if f.is_dir() ]
print("Folders are ", subfolders)
folder_to_look_in = max(subfolders,key=os.path.getctime)
print("Name of folder is", folder_to_look_in)

# Get the files in the folder
csv_files = [file for file in os.listdir(folder_to_look_in) if file.endswith('.jpeg')]
csv_files2 =sorted(csv_files)
print("Sorted list of files",csv_files2)
# Loop through the rows in the dataframe and add the file names to the column called Image
row_number =0
for model_image in range(len(csv_files2)):   
    df.at[row_number,'Image'] = csv_files2[model_image]
    row_number += 1

# Save the csv file
file_name = file_name +".csv"
df.to_csv(file_name, sep=',')
print("We have finished ", file_name)
current_time = now.strftime("%H:%M:%S")
print("End time is ", current_time)
browser.close()
