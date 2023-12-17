import spacy
import pymorphy2
nlp = spacy.load('ru_core_news_sm')
morph = pymorphy2.MorphAnalyzer()
with open('input.txt', 'r') as file:
    text = file.read()                                      #-1
punctuation_marks = ['.', '!', '?']                         #1
sentences = []                                              #2
current_sentence = ''                                       #3
for char in text:                                           #4               
    if char not in punctuation_marks:                       #5      
        current_sentence += char                            #6
    if char in punctuation_marks:                           #7
        current_sentence = current_sentence.strip()         #8
        sentences.append(current_sentence)                  #9
        current_sentence = ''                               #10
if current_sentence.strip() != '':                          #11
    sentences.append(current_sentence.strip())              #12
for sentence in sentences:                                  #13
    doc = nlp(sentence)                                     #14
    for token in doc:                                       #15
        analyzed_token = morph.parse(token.text)[0]         #16
        print(f'Token: {token.text}\t| Lemma: {analyzed_token.normal_form}\t| POS: {analyzed_token.tag.POS}')
