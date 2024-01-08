#from nltk.tokenize import word_tokenize
from khmernltk import word_tokenize


# tokens = word_tokenize("Hello, the quick brown fox.")
# print(tokens)



tokens = word_tokenize("ក្រោយចេញពីសាលា ខ្ញុំទៅហាត់ប្រដាល់ថៃ។ ខ្ញុំរីករាយនឹងកីឡានេះណាស់។")
print(tokens)



file = open('output.txt', 'w', encoding='utf8') 
for tok in tokens:
    file.write(tok + "\n")

file.close()