# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])



# Вывести количество букв а в слове
word = 'Архангельск'.lower()
for i in word:
    if i == 'а':
        sum_a = word.count(i)
print(sum_a)


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
sum_vowel = 0
for i in word:
    if i in vowel:
        sum_vowel = sum_vowel + 1
print(sum_vowel)

    




# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'.split(' ')
print(len(sentence))



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
for i in words:
    print(i[0])



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'.split(' ')
length_of_word = 0
for each_word in sentence:
    length_of_word = length_of_word + len(each_word)

print(length_of_word/len(sentence))
