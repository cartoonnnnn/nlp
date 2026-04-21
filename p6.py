#lab 7
import numpy as np, tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Data
text = """I love natural language processing
deep learning is powerful
language models generate text
machine learning is amazing"""

# Tokenize + sequences
tok = Tokenizer(); tok.fit_on_texts([text])
seq = []
for l in text.split("\n"):
    t = tok.texts_to_sequences([l])[0]
    for i in range(1, len(t)):
        seq.append(t[:i+1])

# Prepare data
maxlen = max(len(s) for s in seq)
seq = pad_sequences(seq, maxlen=maxlen, padding='pre')
X, y = seq[:, :-1], tf.keras.utils.to_categorical(seq[:, -1], len(tok.word_index)+1)

# Model
model = Sequential([Embedding(len(tok.word_index)+1, 32, input_length=maxlen-1),
                    LSTM(64),
                    Dense(len(tok.word_index)+1, activation='softmax')])
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(X, y, epochs=200, verbose=1)
# Generate
s = "language models"
for _ in range(5):
    t = tok.texts_to_sequences([s])[0]
    t = pad_sequences([t], maxlen=maxlen-1, padding='pre')
    p = np.argmax(model.predict(t, verbose=0))
    for w,i in tok.word_index.items():
        if i == p:
            s += " " + w
            break

print(s)
