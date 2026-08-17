import string
file_name = input("Enter File Name: ")
content = input("Enter the contents: ")
with open(file_name, "w") as file:
    file.write(content)
file.close()
with open(file_name, "r") as file:
    text = file.read().lower()
file.close()
for ch in string.punctuation:
    text = text.replace(ch, " ")
words = text.split()
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
sorted_words = sorted(words_count.items(), key=lambda x:x[1], reverse = True)
for word, count in sorted_words:
    print(word, ":", count) 