#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	python ==> 케라스딥러닝강화학습 p199, skipgrams keras 모델에서 가중치를 추출하는 코드
'''

from __future__ import division, print_function
from keras.layers import  Merge
from keras.models import Sequential
from keras.layers.core import Dense, Reshape
from keras.layers.embeddings import Embedding
import keras.backend as K

import numpy as np

# ed: 모든 데이터를 생략없이 출력하도록 해주는 코드
np.set_printoptions(threshold=np.nan)

vocab_size = 5000
embed_size = 300

word_model = Sequential()
word_model.add(Embedding(vocab_size, embed_size,
                         embeddings_initializer="glorot_uniform",
                         input_length=1))

word_model.add(Reshape((embed_size,)))


context_model = Sequential()
context_model.add(Embedding(vocab_size, embed_size,
                            embeddings_initializer="glorot_uniform",
                            input_length=1))

context_model.add(Reshape((embed_size,)))


model = Sequential()
model.add(Merge([word_model, context_model], mode="dot", dot_axes=0))
model.add(Dense(1, kernel_initializer="glorot_uniform", activation="sigmoid"))

model.compile(loss='mean_squared_error', optimizer='adam')


# ed: 학습된 모델에서 가중치를 추출하는 코드
merge_layer = model.layers[0]
word_model = merge_layer.layers[0]
word_embed_layer = word_model.layers[0]
weights = word_embed_layer.get_weights()[0]

# weights = model.layers[0].get_weights()[0]
print(weights.shape) 			# [5000 x 300]
print(weights)
