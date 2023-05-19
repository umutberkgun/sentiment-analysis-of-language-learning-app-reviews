import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as spw
import sqlite3 
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import pandas as pd
sia = SentimentIntensityAnalyzer()

def process(text): #removing stopwords,punctuations, numbers etc.
    text = text.lower()
    text = text.translate(str.maketrans("","",string.punctuation))
    text = re.sub(r'\d+', '', text)
    text_tokens = nltk.word_tokenize(text)
    spw_words = spw.words("english")
    processed_text = [i for i in text_tokens if i not in spw_words]
    return processed_text



duolingo_review_texts = open("duolingoreviews.txt","r").read()
processed_duolingo_text = process(duolingo_review_texts)

dictionary_of_duolingo_tokens = {} #used dictionary to store both the token and the sentiment

for i in processed_duolingo_text:
    dictionary_of_duolingo_tokens[str(i)] = sia.polarity_scores(i)

conn_duo = sqlite3.connect("duolingo_tokens.db") #utilized sqlite3 to store the data
cursor = conn_duo.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS duolingo_review_tokens (token TEXT,neu_score REAL,neg_score REAL,pos_score REAL,compound_score REAL)")
conn_duo.commit()


for value,key in dictionary_of_duolingo_tokens.items():
    if isinstance(value,int): #I don't need numbers
        continue
    else:
        sql_statement = f"INSERT INTO duolingo_review_tokens (token,neu_score,neg_score,pos_score,compound_score) VALUES('{value}',{dictionary_of_duolingo_tokens[value]['neu']},{dictionary_of_duolingo_tokens[value]['neg']},{dictionary_of_duolingo_tokens[value]['pos']},{dictionary_of_duolingo_tokens[value]['compound']})"
        cursor.execute(sql_statement)
        conn_duo.commit()

df_duolingo = pd.read_sql_query("SELECT * FROM duolingo_review_tokens ",conn_duo)
print(df_duolingo)#to check if everything works


rosetta_stone_review_text = open("rosettastonereviews.txt","r").read()
processed_rosetta_stone_text = process(rosetta_stone_review_text)
dictionary_of_rosetta_stone_tokens = {}


for i in processed_rosetta_stone_text:
    dictionary_of_rosetta_stone_tokens[str(i)]= sia.polarity_scores(i)

conn_rosetta_stone = sqlite3.connect("rosetta_stone_tokens.db")
cursor2 = conn_rosetta_stone.cursor()

cursor2.execute("CREATE TABLE IF NOT EXISTS rosetta_stone_review_tokens (token TEXT,neu_score REAL, neg_score REAL, pos_score REAL, compound_score REAL)")
conn_rosetta_stone.commit()


for value,key in dictionary_of_rosetta_stone_tokens.items():
    if isinstance(value,int):
        continue
    else:
        sql_query = f"INSERT INTO rosetta_stone_review_tokens (token,neu_score,neg_score,pos_score,compound_score) VALUES('{value}',{dictionary_of_rosetta_stone_tokens[value]['neu']},{dictionary_of_rosetta_stone_tokens[value]['neg']},{dictionary_of_rosetta_stone_tokens[value]['pos']},{dictionary_of_rosetta_stone_tokens[value]['compound']})"
        cursor2.execute(sql_query)
        conn_rosetta_stone.commit()

df_rosetta_stone = pd.read_sql_query("SELECT * FROM rosetta_stone_review_tokens",conn_rosetta_stone)



babbel_review_text = open("babbelreviews.txt","r").read()
processed_babbel_review_text = process(babbel_review_text)

dictionary_of_babbel_tokens = {}

for i in processed_babbel_review_text:
    dictionary_of_babbel_tokens[str(i)] = sia.polarity_scores(i)

conn_babbel = sqlite3.connect("babbel_tokens.db")
cursor3 = conn_babbel.cursor()

cursor3.execute("CREATE TABLE IF NOT EXISTS babbel_review_tokens (token TEXT,neu_score REAL, neg_score REAL, pos_score REAL, compound_score REAL)")
conn_babbel.commit()

for value,key in dictionary_of_babbel_tokens.items():
    if isinstance(value,int):
        continue
    else:
        sql_query = f"INSERT INTO babbel_review_tokens (token,neu_score,neg_score,pos_score,compound_score) VALUES('{value}',{dictionary_of_babbel_tokens[value]['neu']},{dictionary_of_babbel_tokens[value]['neg']},{dictionary_of_babbel_tokens[value]['pos']},{dictionary_of_babbel_tokens[value]['compound']})"
        cursor3.execute(sql_query)
        conn_babbel.commit()

df_babbel = pd.read_sql_query("SELECT * FROM babbel_review_tokens",conn_babbel)
print(df_babbel)













