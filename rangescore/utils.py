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
    data = re.sub(r'\b[A-Z]\w+\b', '', data)
    # remove puncutation
    data = re.sub(r'[.,/;:''"]', '', data)
    return lem_text(data)

def percentiles(text):
    words = process_text(text)
    d = fl.reindex(words)['index'].fillna(0)
    result = ""
    for value in [0.8, 0.9, 0.97]:
        result += (str(int(100 * value)) 
            + "th-percentile vocabulary size for this text is " 
            + str(int(d.quantile(value)))) + "\n"
    return result