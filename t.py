#!/usr/bin/env python

import Levenshtein
import numpy as np

import os
import sys
import pathlib
import itertools
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
import scipy.cluster.hierarchy as hcl
from scipy.spatial.distance import squareform
from pprint import pprint

datafile = pathlib.Path('./data.txt')
data = datafile.read_text().splitlines()
data = [x.strip() for x in data]
data = set(data)

d = [{'x1':x1, 'x2':x2, 'dist':Levenshtein.distance(x1, x2)} for x1,x2 in itertools.product(data, data)]
dist_df = pd.DataFrame(d)

print(dist_df)

dist_df_piv = dist_df.pivot('x1', 'x2', 'dist').fillna(0)

print(dist_df_piv)

print(dist_df_piv.as_matrix())

dist_df = dist_df_piv.as_matrix()

print(squareform(dist_df))
print(linkage(squareform(dist_df)))
