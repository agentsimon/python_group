

# Python program to generate WordCloud
 
# importing all necessary modules
#from wordcloud import WordCloud, STOPWORDS
#import matplotlib.pyplot as plt
import pandas as pd
 
comment_words = ''
# Reads 'prompts.csv' file 
df = pd.read_csv(r"D:\PythonLearning\python_group-main\prompts.csv", encoding ="latin-1")

print('uuuuu')
print(df)
row_number = len(df)
print("Number of rows ", row_number)
print('hhhhh')
#print(df)
i = 0
while i < row_number:
    sentence = df.at[i, "Reply"]
    comment_words = comment_words +sentence
    #print(comment_words)
    i += 1 


df2 = df.copy()
#df2
# Use DataFrame.loc[] & DataFrame.sum() Method
#Rename column Tokens used
df2.rename(columns={"Tokens used": "Tokens_used"})

total_tokens = df2["Tokens used"].sum
#print("Total number of tokens used ",total_tokens)


# Remove selected words from the list comment_words
unwanted_words = ["The","of","and","an","a","on","the"]
#print("this is comment words: ", comment_words)
removed = comment_words.replace('.', ' ')
removed2 = removed.replace(',', ' ')
sentence_list = removed2.split()
print("Total number of words ",len(sentence_list))
print("Total number of words ",len(sentence_list))
print("Number of instances of 'the' ",sentence_list.count("the"))
print("Number of instances of 'rain' ",sentence_list.count("rain"))
print("Number of instances of 'raindrops' ",sentence_list.count("raindrops"))
print("Number of instances of 'Rain' ",sentence_list.count("Rain"))
print("After deletion")
print('check')
#print(sentence_list)
for word in unwanted_words:
    for delete_word in sentence_list:
        if delete_word == word:
            sentence_list.remove(delete_word)
print("after ")
#print(sentence_list)
#print(len(sentence_list), "Sentence with words removed", sentence_list)
print("Number of instances of 'the' ",sentence_list.count("the"))
print("Number of instances of 'rain' ",sentence_list.count("rain"))
print("Number of instances of 'raindrops' ",sentence_list.count("raindrops"))
print("Number of instances of 'Rain' ",sentence_list.count("Rain"))


# counting the number of individual words in the sentence_list


dict_of_words = {}

print(sentence_list[0])
count = 0
while count < len(sentence_list):
     name_of_word = sentence_list[count]
     #print(name_of_word)
     number_of_count = sentence_list.count(name_of_word)
     dict_of_words[name_of_word] = number_of_count
     count += 1

print("dict o.............................")
print(len(dict_of_words))


# for w in sorted(dict_of_words, key=dict_of_words.get, reverse=False):
#     print(w, dict_of_words[w])



#print(comment_words)
# plot the WordCloud image                       
""" plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show() """
