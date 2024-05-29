import re

from nltk.corpus import stopwords

# re: For text processing using regular expressions.<br>
# nltk.corpus.stopwords: To remove common Arabic stopwords from the text.<br>



# Define Arabic stopwords
stop_words = set(stopwords.words('arabic'))

# Function to clean text
def clean_text(text):
    # Remove diacritics and tatweel
    text = re.sub('[\u0617-\u061A\u064B-\u0652\u0670\u0674\u06D4\u06D6-\u06ED]', '', text)
    # Remove non-Arabic characters and digits
    text = re.sub('[^\u0600-\u06FF\u0750-\u077F\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub(r'\s+', ' ', text)
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

