# -*- coding: utf-8 -*-
"""
Created on Mon Jun  11:39:57 2020

@author: lim
"""
from nltk.stem import WordNetLemmatizer 
import nltk
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer() 




def process_sentence(sentence):
    text = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(text)
    
        
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    lemmatized_sentence=[]
    for x in tags:
        tag = x[1][0].upper()
        value = tag_dict.get(tag, wordnet.NOUN)
        lemmatized_sentence.append(lemmatizer.lemmatize(x[0],value))
    return lemmatized_sentence  
    # print( lemmatized_sentence)
    
# sentence ='Amazing'
# print(process_sentence(sentence))

# if "is" in process_sentence(sentence):
#     print("ok")
# else:
#     print(":(")