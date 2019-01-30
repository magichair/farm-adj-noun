import json
import random
import requests

def clean(l):
  l = list(set(l))
  random.shuffle(l)
  return l

def good_word(w):
  return w.isalpha() and w[-1:] is not 's' and ' ' not in w

def get_words_by(words, part):
  typed_words = [a['word'].lower() for a in words if 'tags' in a and part in a['tags'] and good_word(a['word'])]
  return clean(typed_words)

def get_words_from_datamuse(topic_string, limit=1000):
  req = requests.get('https://api.datamuse.com/words?topics=%s&max=%d' % (topic_string, limit))
  if req.status_code == 200:
    return req.json()
  return {}

def main():
  words = get_words_from_datamuse('farming', 500) + \
          get_words_from_datamuse('truck', 500) + \
          get_words_from_datamuse('agriculture', 500) + \
          get_words_from_datamuse('vegetable', 500) + \
          get_words_from_datamuse('corn', 100) + \
          get_words_from_datamuse('soy', 100) + \
          get_words_from_datamuse('wheat', 100) + \
          get_words_from_datamuse('cotton', 100) + \
          get_words_from_datamuse('rice', 100)

  print(json.dumps({
      'nouns': get_words_by(words, 'n'),
      'adjs': get_words_by(words, 'adj')
    }))

main()
