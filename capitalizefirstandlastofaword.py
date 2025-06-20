def capitalize_first_last(word):
    if len(word)==1:
        return word.upper()
    return word[0].upper()+word[1:-1]+word[-1].upper()
text=input("Enter the text:")
words=text.split()
new_words=[]
for word in words:
    new_word=capitalize_first_last(word)
    new_words.append(new_word)
result=' '.join(new_words)
print("Modified text:",result)