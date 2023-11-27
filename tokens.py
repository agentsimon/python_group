
import time
from datetime import datetime
import pandas as pd
# importing openai module into your openai environment 
from openai import OpenAI
import tiktoken

row_number = 0
client = OpenAI(api_key='Your key')
# Load the CSV file into a dataframe
df = pd.read_csv("/home/simon/Documents/Python/prompts.csv",  engine ='python')


model="gpt-3.5-turbo-1106"
encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
encoding_name = "cl100k_base"
print("Starting")

# Create class that acts as a countdown
def get_prompt():
        global row_number
        # datetime object containing current date and time
        now = datetime.now()
        print("Running prompt")
        prompt  = "Describe rain in 2 sentences"
        print(prompt)
        encoding = tiktoken.get_encoding(encoding_name)
        num_tokens = len(encoding.encode(prompt))
        messages = [{"role":"user","content":prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.95
        )
        response = response.choices[0].message.content
        print(response)
        current_date = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
        df.loc[row_number, "Date"] = current_date
        df.loc[row_number, "Prompt"] = prompt
        df.loc[row_number, "Reply"] = response
        df.loc[row_number, "Tokens used"] = num_tokens
        df.to_csv("prompts.csv")
        row_number = row_number + 1
        print(row_number)

# Schedule the get_prompt function to run every 30 minutes
#schedule.every(10).minutes.do(get_prompt)

# Run the scheduled tasks
while True:
    if row_number < 10:
         print("Here")
         get_prompt()
         
    else:
         break
    print("Waiting")
    time.sleep(600)

        
    
