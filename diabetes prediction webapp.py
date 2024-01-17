# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:37:46 2024

@author: shreyanshi
"""

import numpy as np
import pickle
import streamlit


# loading the saved model
loaded_model = pickle.load(open('C:/Users/dassh/Desktop/diabetes pred/trained_model.sav', 'rb'))
