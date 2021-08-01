import re
import pandas as pd
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
fl = pd.read_csv("freqlists/ru.csv", index_col=0)
fl = fl.reset_index().set_index("Lemma")

def lemmatize(word):
    return morph.parse(word)[0].normal_form

def lem_text(text):
    return [lemmatize(word) for word in text.split() if word]

def remove_yo(s):
    return s.replace("ё", "е")

def process_text(data):
    data = re.sub(r'\n+', ' ', data)
    # remove capitalized words (assumed to be names)
    data = re.sub(r'[ЁА-Я][ёа-яЁА-Я]+', '', data)
    # remove latin
    data = re.sub(r'[a-zA-Z]', '', data)
    # remove puncutation
    data = re.sub(r'_[.,/;:''"]', '', data)
    return lem_text(data)

def coverages(text):
    words = process_text(text)
    d = fl.reindex(words)['index'].fillna(0)
    info = []
    for lvl in [500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000,
    12000, 15000, 20000, 25000, 30000, 40000, 50000]:
        info.append({"level":str(lvl), "coverage": len(d[d<=lvl])/len(d)})
    return {"data": info}
