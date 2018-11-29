import json
import os
import re
import dateutil.parser
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
import nltk
import markdown2
from bs4 import BeautifulSoup

nltk.download('punkt')
nltk.download('stopwords')

repos = ['react', 'angular', 'vue', 'backbone', 'ember.js', 'jquery']
fields = ['data', 'date']

for repo in repos:
    with open('%s_documents.json' % repo, 'r') as dirty:
        documents = json.loads(dirty.read())
        for document in documents:
            for field in list(document.keys()):
                if (field == 'data'):
                    text = markdown2.markdown(
                        document[field]) if document[field] is not None else ''
                    soup = BeautifulSoup(text, 'html.parser')
                    for tag in soup.find_all('code'):
                        tag.replaceWith('')
                    text = markdown2.markdown(soup.get_text())
                    text = re.sub('<[^<]+?>', '', text)
                    text = re.sub(r"http\S+", "", text)
                    tokens = word_tokenize(text)
                    tokens = [w.lower() for w in tokens]
                    table = str.maketrans('', '', string.punctuation)
                    stripped = [w.translate(table) for w in tokens]
                    words = [word for word in stripped if word.isalpha()]
                    stop_words = set(stopwords.words('english'))
                    words = [w for w in words if not w in stop_words]
                    document[field] = ' '.join(words)
                if field not in fields:
                    del document[field]
    with open('%s_documents_clean.json' % repo, 'w+') as clean:
        json.dump(documents, clean)
