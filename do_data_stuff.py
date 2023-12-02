

# Python program to generate WordCloud
 
# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
 
comment_words = ''
# Reads 'prompts.csv' file 
df = pd.read_csv(r"/home/simon/Documents/Python/prompts.csv", encoding ="latin-1")

print('uuuuu')
print(df)
row_number = len(df)
print("Number of rows ", row_number)
print('hhhhh')
print(df)
i = 0
while i < row_number:
    sentence = df.at[i, "Reply"]
    print('iiiiii')
    print(i)
    comment_words = comment_words +sentence
    print(comment_words)
    i += 1 


df2 = df.copy()
df2
# Use DataFrame.loc[] & DataFrame.sum() Method
#Rename column Tokens used
df2.rename(columns={"Tokens used": "Tokens_used"})

total_tokens = df2["Tokens used"].sum
#print("Total number of tokens used ",total_tokens)
print("Total number of words ",len(comment_words))
print("Number of instances of 'the' ",comment_words.count("the"))
print("Number of instances of 'rain' ",comment_words.count("rain"))
print("Number of instances of 'raindrops' ",comment_words.count("raindrops"))
print("After deletion")

# Remove selected words from the list comment_words
unwanted_words = ["The","of","and","an","a","on","the"]

sentence_list = comment_words.split()
for word in unwanted_words:
    for delete_word in sentence_list:
        if delete_word == word:
            sentence_list.remove(delete_word)

#print(len(sentence_list), "Sentence with words removed", sentence_list)
print("Number of instances of 'the' ",sentence_list.count("the"))
print("Number of instances of 'rain' ",sentence_list.count("rain"))
print("Number of instances of 'raindrops' ",sentence_list.count("raindrops"))
#print(comment_words)
# plot the WordCloud image                       
""" plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show() """