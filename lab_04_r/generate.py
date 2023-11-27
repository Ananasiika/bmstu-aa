import random
import string
import codecs
import os
import sys

# Создаем файлы в указанной директории
directory = './src/data/'
os.makedirs(directory, exist_ok=True)

# Список слов на русском языке для генерации текста
russian_words = ['я', 'ты', 'он', 'она', 'мы', 'вы', 'они', 'книга', 'рука', 'дом', 'дерево', 'солнце', 'земля', 'вода', 'огонь', 'ветер', 'море', 'гора', 'цветок', 'снег', 'дождь', 'небо', 'воздух', 'трава', 'лес', 'поле', 'звезда', 'луна', 'звук', 'шум', 'тишина', 'радость', 'горе', 'любовь', 'ненависть', 'счастье', 'болезнь', 'здоровье', 'успех', 'поражение', 'дружба', 'вражда', 'игра', 'танец', 'песня', 'музыка', 'искусство', 'творчество', 'работа', 'отдых', 'занятие', 'учеба', 'конфликт', 'мир', 'война', 'память', 'забывчивость', 'мечта', 'реальность', 'фантазия', 'природа', 'город', 'страна', 'мироздание', 'наука', 'исследование', 'открытие', 'изобретение', 'технология', 'история', 'культура', 'социальное', 'экономика', 'политика', 'философия', 'религия', 'семья', 'дружба', 'любовь', 'отношения', 'развлечение', 'путешествие', 'отпуск', 'событие', 'праздник', 'проблема', 'решение', 'вопрос', ',', '.', '?', '!', '\n']


def create_file_with_text(file_name, size_in_kb):
    text = ''
    while sys.getsizeof(text) < size_in_kb*1024:
        word = random.choice(russian_words)
        text += word + ' '
    with codecs.open(file_name, 'w', 'utf-8') as file:
        file.write(text)

for size_in_kb in range(100, 1001, 100):
    file_name = f'{directory}/input_{size_in_kb}kb.txt'
    create_file_with_text(file_name, size_in_kb)
    print(f'Файл {file_name} успешно создан.')

