#Напишите программу, удаляющую из текста все слова, содержащие ""абв""
my_text = 'В этом абв , текстеабв тексте нетабв нет трёх бкувабв букв абв А - Б - В"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)
