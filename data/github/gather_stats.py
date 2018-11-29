import json
import dateutil.parser

repos = ['react', 'angular', 'vue', 'backbone', 'ember.js', 'jquery']


def get_wc(text, prev_words):
    words = {} if prev_words is None else prev_words
    for word in text.split(' '):
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1
    return words


def get_date(date_str):
    date = dateutil.parser.parse(date_str)
    return date.strftime('%Y-%m')


for repo in repos:
    with open('%s_documents_clean.json' % repo, 'r') as f:
        stats = {}
        documents = json.loads(f.read())
        for document in documents:
            date = get_date(document['date'])
            prev_words = None
            if date not in stats:
                stats[date] = {}
            else:
                prev_words = stats[date]['wc']
            stats[date]['wc'] = get_wc(document['data'], prev_words)

    word_count = {}
    for (date, wc) in stats.items():
      words = []
      for (word, count) in wc['wc'].items():
        words.append({
          'value': count,
          'text': word
        })
      words = sorted(words, key=lambda word: word['value'], reverse=True)
      words = words[:10]
      word_count[date] = words

    with open('%s_words.json' % repo, 'w+') as f:
        json.dump(word_count, f)
