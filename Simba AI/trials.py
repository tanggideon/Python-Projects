import json
from tkinter import *
from tkinter.messagebox import showinfo, askyesno, showerror
from tkinter import ttk
import numpy as np
from tensorflow import keras
from PIL import ImageTk, Image
from sklearn.preprocessing import LabelEncoder
import random
import pickle
import openai
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
import psycopg2
from nltk.classify.util import accuracy as nltk_accuracy

def sentiment_analyzer(reviews):
    # Load the reviews from the corpus
    fileids_pos = movie_reviews.fileids('pos')
    fileids_neg = movie_reviews.fileids('neg')
    # Extract the features from the reviews
    features_pos = [(dict([(word, True) for word in
                           movie_reviews.words(fileids=[f])]), 'Positive') for f in fileids_pos]
    features_neg = [(dict([(word, True) for word in
                           movie_reviews.words(fileids=[f])]), 'Negative') for f in fileids_neg]
    # Define the train and test split (80% and 20%)
    threshold = 0.8
    num_pos = int(threshold * len(features_pos))
    num_neg = int(threshold * len(features_neg))
    # Create training and training datasets
    features_train = features_pos[:num_pos] + features_neg[:num_neg]
    features_test = features_pos[num_pos:] + features_neg[num_neg:]
    # Print the number of datapoints used
    print('\nNumber of training datapoints:', len(features_train))
    print('Number of test datapoints:', len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)
    print('\nAccuracy of the classifier:', nltk_accuracy(classifier,
                                                         features_test))
    # Test input movie reviews
    input_reviews = reviews.strip()
    input_reviews = reviews.split("\n")
    analysis = []
    print("\nMovie review predictions:")
    for review in input_reviews:
        probabilities = classifier.prob_classify((dict([(word, True) for word
                                                        in review.split()])))
        # Pick the maximum value
        predicted_sentiment = probabilities.max()
        analyzed = (review, predicted_sentiment,
                    round(probabilities.prob(predicted_sentiment), 2))
        analysis.append(analyzed)

    return analysis

