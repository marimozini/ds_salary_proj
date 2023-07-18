# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:40:35 2023

@author: marim
"""

#import glassdoor_scraper as gs
import glassdoor_sc_medium as gs
import pandas as pd
path = "C:/Users/marim/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)

