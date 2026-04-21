#lab 4
import requests, re, nltk
from nltk.util import ngrams
from collections import Counter

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Example
w = "This is an example corpus to find ngrams from text".split()

print("Unigrams:"); [print(i) for i in w]
print("\nBigrams:"); [print(i) for i in ngrams(w,2)]
print("\nTrigrams:"); [print(i) for i in ngrams(w,3)]   # ✅ fixed

# Real data
t = requests.get("https://www.gutenberg.org/files/1342/1342-0.txt").text.lower()
tok = nltk.word_tokenize(t)

c = [re.sub(r'[^\w\s]','',x) for x in tok if re.sub(r'[^\w\s]','',x) and not re.sub(r'[^\w\s]','',x).isdigit()]

u,b,tr = c, list(ngrams(c,2)), list(ngrams(c,3))
uf,bf,tf = Counter(u), Counter(b), Counter(tr)

print(f"Total tokens: {len(c)}")
print(f"Unique unigrams: {len(uf)}")
print(f"Unique bigrams: {len(bf)}")
print(f"Unique trigrams: {len(tf)}")

print("\nTop 20 Unigrams:")
for i,j in uf.most_common(20):
    print(f"{i}: {j}")

print("\nTop 20 Bigrams:")
for i,j in bf.most_common(20):
    print(f"{i}: {j}")

print("\nTop 20 Trigrams:")
for i,j in tf.most_common(20):
    print(f"{i}: {j}")
