from textblob import TextBlob 
from nltk.tokenize import TabTokenizer 
from textblob import Word


# text_blob_object = TextBlob("Tom is great!")
# print(text_blob_object.tags)


# tokenizer = TabTokenizer()
# text_blob_object = TextBlob("Tom is great! Liuna is even better.", tokenizer = tokenizer)
# print(text_blob_object.tokens)
# print(text_blob_object.words)
# print(text_blob_object.sentences)

word = Word("equilibria")
print(word.lemmatize())

text_blob_object = TextBlob("Thiss is correcct senetenc.")
print(text_blob_object.correct())
#corrects "correcct" to "correct" and "sentenc" to "sentence". "Thiss" was corrected to "Hiss" rather than "This".
