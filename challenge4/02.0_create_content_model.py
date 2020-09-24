import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from top2vec import Top2Vec

content = pd.read_csv('../data/content-clean.csv')
documents = content['text'].values.tolist()
model = Top2Vec(documents, workers = 8)
model.save("content-model.bin")
