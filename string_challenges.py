# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
len_a = word.lower().count('а')
print(len_a)

# Вывести количество гласных букв в слове
vowels = 'аеёиоуыэюя'
word = 'Архангельск'

word = word.lower()
num_vowels = sum(1 for letter in word if letter in vowels)
print(num_vowels)
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split(' ')))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
for word in words:
    print(word[0])

list(print(word[0]) for word in words)

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
mean = sum(len(word) for word in words)/len(words)
print(mean)
# ???