from textblob import TextBlob 
from textblob.sentiments import NaiveBayesAnalyzer
import pandas as pd
import numpy as np 

dataset = pd.read_csv("airbnb-reviews-part-3.csv")

comments = dataset.iloc[0:500,5].values

print(comments)