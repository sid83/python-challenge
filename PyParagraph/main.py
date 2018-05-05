import re
import os
# text file to open
file=os.path.join("raw_data","paragraph_1.txt")

# Open txt file
with open(file,'r',encoding="UTF-8") as text:
    print(text)
    # assigning as an object of text.read class
    lines=text.read()
# Counting Words
words=lines.split()
no_of_words=len(words) 

# Counting no of periods for sentence count
no_of_sent=lines.count('.')

# Average Letter Count
lettercount=0
for word in words:
    lettercount+=len(word)
av_letter_count=lettercount/no_of_words

# Average Sentence Length
av_sent_len=no_of_words/no_of_sent    

# printing paragraph analysis
print(f'Paragraph Analysis')
print("-"*40)
print(f"Approximate Word Count: {no_of_words}")
print(f'Approximate Sentence Count: {no_of_sent}')
print(f'Average Letter Count: {av_letter_count}')
print(f'Average Sentence Length: {av_sent_len}')