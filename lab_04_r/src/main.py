import argparse
import spacy

# Загрузка языковой модели Spacy для русского языка
nlp = spacy.load("ru_core_news_sm")

# Парсинг аргументов командной строки
parser = argparse.ArgumentParser(description='Анализ текста и сохранение результатов')
parser.add_argument('input_file', help='Путь к файлу для анализа')
parser.add_argument('output_file', help='Путь к файлу для результата')
args = parser.parse_args()

# Чтение текста из входного файла
with open(args.input_file, 'r') as file:
    text = file.read()

# Обработка текста
doc = nlp(text)
# spacy.displacy.serve(doc, style='dep')
# Построение дерева синтаксических зависимостей
with open(args.output_file, 'a', encoding="utf-8") as file:
    for token in doc:
        file.write(token.text + " " + token.dep_ + " " + token.head.text + '\n')
