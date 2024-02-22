import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Tokenize and preprocess text
text = "This is a sample sentence for NLP."
tokens = word_tokenize(text)
cleaned_tokens = [token for token in tokens if token.lower() not in stopwords.words('english')]

# Perform NLP tasks
# Example: Calculate word frequency
word_freq = nltk.FreqDist(cleaned_tokens)
print(word_freq.most_common(5))
