import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords as spw
import sqlite3 
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import pandas as pd
sia = SentimentIntensityAnalyzer()

duolingo_review_texts = open("duolingoreviews.txt","r").read()
duolingo_review_texts = duolingo_review_texts.lower()
duolingo_review_texts = duolingo_review_texts.translate(str.maketrans("","",string.punctuation))
duolingo_review_texts = re.sub(r'\d+', '', duolingo_review_texts)
duolingo_review_texts = nltk.word_tokenize(duolingo_review_texts)

spw_words = spw.words("english")
processed_duolingo_text = [i for i in duolingo_review_texts if i not in spw_words]





dictionary_of_duolingo_tokens = {}

for i in processed_duolingo_text:
    dictionary_of_duolingo_tokens[str(i)] = sia.polarity_scores(i)

conn_duo = sqlite3.connect("duolingo_tokens.db")
cursor = conn_duo.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS duolingo_review_tokens (token TEXT,neu_score REAL,neg_score REAL,pos_score REAL,compound_score REAL)")
conn_duo.commit()


for value,key in dictionary_of_duolingo_tokens.items():
    if isinstance(value,int):
        continue
    else:
        sql_statement = f"INSERT INTO duolingo_review_tokens (token,neu_score,neg_score,pos_score,compound_score) VALUES('{value}',{dictionary_of_duolingo_tokens[value]['neu']},{dictionary_of_duolingo_tokens[value]['neg']},{dictionary_of_duolingo_tokens[value]['pos']},{dictionary_of_duolingo_tokens[value]['compound']})"
        cursor.execute(sql_statement)
        conn_duo.commit()

df_duolingo = pd.read_sql_query("SELECT * FROM duolingo_review_tokens ",conn_duo)



rosetta_stone_review_text = open("rosettastonereviews.txt","r").read()
rosetta_stone_review_text = rosetta_stone_review_text.lower()
rosetta_stone_review_text = rosetta_stone_review_text.translate(str.maketrans("","",string.punctuation))
rosetta_stone_review_text = re.sub(r'\d+', '', rosetta_stone_review_text)
rosetta_stone_review_text = nltk.word_tokenize(rosetta_stone_review_text)

processed_rosetta_stone_text = [i for i in rosetta_stone_review_text if i not in spw_words]

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
babbel_review_text = babbel_review_text.lower()
babbel_review_text = babbel_review_text.translate(str.maketrans("","",string.punctuation))
babbel_review_text = re.sub(r'\d+', '', babbel_review_text)
babbel_review_text = nltk.word_tokenize(babbel_review_text)

processed_babbel_review_text = [i for i in babbel_review_text if i not in spw_words]

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












