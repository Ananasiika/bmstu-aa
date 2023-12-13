import spacy
import sys

# Загрузка языковой модели Spacy для русского языка
nlp = spacy.load("ru_core_news_sm")


with open(sys.argv[1], "r") as file:
	while (1):
		sentence = file.readline()
		if (len(sentence) == 0):
			break
		doc = nlp(sentence)

		# Построение дерева синтаксических зависимостей
		dependency_tree = []
		for token in doc:
			dependency_tree.append(token.text + " " + token.dep_ + " " + token.head.text)

		with open(sys.argv[2], "a") as file_output:
			file_output.write("\n".join(dependency_tree))
			file_output.write("\n\n")

