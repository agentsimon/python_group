'''
Written in haste. 
There are two methods used for the timing, a standard sleep.time and 
WebDriver Wait method. The latter is more elegant but I haven't changed all the time.sleep(web_page_time) implementations.

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

#time.sleep(10)
# delay time
web_page_time = 2
# processing time
process_time = 40

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
pd.options.mode.chained_assignment = None  

# default='warn'# Set up the correct values
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
        print("We have the settings save button")
        print("Location: ", settings_save.location)
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
# Select the model
    input = browser.find_element("id","editor-settings")
    time.sleep(web_page_time)
    input.click()
    time.sleep(web_page_time)
    settings_button2 = browser.find_element("id", "stable_diffusion_model")
    time.sleep(web_page_time)
# identify dropdown for model and select
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "stable_diffusion_model"))))
    select.select_by_visible_text("sd-v1-4")
 # identify dropdown for sampler and select
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "sampler_name"))))
    select.select_by_visible_text("Euler")
# identify dropdown for image type and select
    select = Select(WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.ID, "output_format"))))
    select.select_by_visible_text("png")
# Select the fix face button use_face_correction
# Turn on the auto save images toggle
    settings_face = browser.find_element(By.XPATH, '//*[@id="use_face_correction"]')
    if settings_face.is_selected() == False:
        print("We have the settings face correction")
        print("Location: ", settings_face.location)
        browser.execute_script("arguments[0].click();", settings_face)


# Main Body starts here
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("http://localhost:9000/")
browser.maximize_window()
# Run the set up function
set_up()

prompt_name ="walking the streets of Hanoi"
prompt_name = prompt_name + " 2023"
print("Prompt is ", prompt_name)
 # Finding the search field by id
input = browser.find_element("id","prompt")
input.send_keys(prompt_name)
# clicking on the Make image button
button = browser.find_element("id","makeImage")
button.click()
# Wait for the image to be made which will be auto saved
time.sleep(process_time)
print("We have finished")
browser.close()
