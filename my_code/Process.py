# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 08:30:01 2021

@author: Ngoc Anh
"""
from .MovieLens import MovieLens
from surprise import KNNBasic
from surprise import NormalPredictor
from .Evaluator import Evaluator

import random
import numpy as np


def LoadMovieLensData():
    ml = MovieLens()
    print("Loading movie ratings...")
    data = ml.loadMovieLensLatestSmall()
    print("\nComputing movie popularity ranks so we can measure novelty later...")
    rankings = ml.getPopularityRanks()
    return (ml, data, rankings)


def RecommendMovie(user_id):
    # user_id = input((" UserID "))
    np.random.seed(0)
    random.seed(0)

    # Load up common data set for the recommender algorithms
    (ml, evaluationData, rankings) = LoadMovieLensData()


    # Construct an Evaluator to, you know, evaluate them
    evaluator = Evaluator(evaluationData, rankings)


    # User-based KNN
    UserKNN = KNNBasic(sim_options = {'name': 'cosine', 'user_based': True})
    evaluator.AddAlgorithm(UserKNN, "User KNN")

    # Item-based KNN
    #ItemKNN = KNNBasic(sim_options = {'name': 'cosine', 'user_based': False})
    #evaluator.AddAlgorithm(ItemKNN, "Item KNN")

    # Just make random recommendations
    #Random = NormalPredictor()
    #evaluator.AddAlgorithm(Random, "Random")

    # Fight!
    evaluator.Evaluate(False)

    res = evaluator.SampleTopNRecs(ml, testSubject=user_ID)
    return res 
