import spacy
import pymorphy2
import networkx as nx
import matplotlib.pyplot as plt

nlp = spacy.load('ru_core_news_sm')
morph = pymorphy2.MorphAnalyzer()

with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)

tree = []
for token in doc:
    if token.dep_ != 'punct' and token.dep_ != 'ROOT':
        tree.append((token.head.text, token.text, token.dep_))

pairs = []
for token in doc:
    parsed_token = morph.parse(token.text)[0]
    lemma = parsed_token.normal_form
    pos = parsed_token.tag.POS
    if pos and (lemma, pos) not in pairs:
        pairs.append((lemma, pos))

G = nx.DiGraph()

for token in pairs:
    G.add_node(token[0], label=f"{token[0]} ({token[1]})")

edge_labels = {}

for i in range(len(tree)):
    parsed_token = morph.parse(tree[i][0])[0]
    child = parsed_token.normal_form
    parsed_token = morph.parse(tree[i][1])[0]
    parent = parsed_token.normal_form
    if (child, parent) not in edge_labels:
        edge_labels[(child, parent)] = 1
    else:
        edge_labels[(child, parent)] += 1

for edge in edge_labels:
    G.add_edge(edge[0], edge[1])

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, labels=nx.get_node_attributes(G, 'label'), node_color='lightblue', node_size=2000, arrows=False)
nx.draw_networkx_edge_labels(G, nx.spring_layout(G, seed=42), edge_labels=edge_labels)
plt.show()
