from textblob import TextBlob 
from nltk.tokenize import TabTokenizer 
from textblob import Word

from textblob.sentiments import NaiveBayesAnalyzer

# text_blob_object = TextBlob("Tom is great!")
# print(text_blob_object.tags)


# tokenizer = TabTokenizer()
# text_blob_object = TextBlob("Tom is great! Liuna is even better.", tokenizer = tokenizer)
# print(text_blob_object.tokens)
# print(text_blob_object.words)
# print(text_blob_object.sentences)

# word = Word("equilibria")
# print(word.lemmatize())

# text_blob_object = TextBlob("Thiss is correcct senetenc.")
# print(text_blob_object.correct())
#corrects "correcct" to "correct" and "senetenc" to "sentence". "Thiss" was corrected to "Hiss" rather than "This".


text_blob_object = TextBlob("Tom is great! Liuna is even better.", analyzer = NaiveBayesAnalyzer())
print(text_blob_object.sentiment)
#This sentence is approximately 63% positive and 37% negative

text_blob_object = TextBlob("This program is amazing.", analyzer=NaiveBayesAnalyzer())
print(text_blob_object.sentiment)
#This sentence is approximately 67% positive and 33% negative.

text_blob_object = TextBlob("Baby Shark Do do.", analyzer = NaiveBayesAnalyzer())
print(text_blob_object.sentiment)



