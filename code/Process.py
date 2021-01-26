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

    (ml, evaluationData, rankings) = LoadMovieLensData()

    evaluator = Evaluator(evaluationData, rankings)

    UserKNN = KNNBasic(sim_options={'name': 'cosine', 'user_based': True})
    evaluator.AddAlgorithm(UserKNN, "User KNN")

    res = evaluator.SampleTopNRecs(ml, testSubject=user_id)
    return res 
