import spacy
from spacy_download import load_spacy
from spacy import displacy
import os

# Read the file

file1 = open("output.txt","r")
text = file1.read()
file1.close()

nlp = load_spacy('en_core_web_sm')

# Create an nlp object
doc = nlp(text)
# print(doc)
displacy.render(doc,style='ent',jupyter=True)


# # Iterate over the tokens
# for token in doc:
#     # Print the token and its part-of-speech tag
#     print(token.text, "-->", token.pos_)

# Text and label of named entity span
print([(ent.text, ent.label_) for ent in doc.ents])
# [('Larry Page', 'PERSON'), ('Google', 'ORG')]

