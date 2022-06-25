#This file contains lists of verbs, adjectives, etc.
import random

verbs1 = ['run','call','jump','fight', 'fly', 'sing', 'dig', 'cook', 'dance', 'go', 'pet', 'jog', 'grow', 'write', 'swim', 'know', 'look', 'use', 'call', 'pay', 'bounce', 'hop', 'hitch-hike', 'brag', 'high-five', 'zig-zag']
adjectives1 = ['tall', 'short', 'moist', 'beautiful', 'kind', 'bewildered', 'awful', 'good', 'bad', 'clumsy', 'delightful', 'enthusiastic', 'glamorous', 'funny', 'funky', 'crazy', 'bright', 'careful', 'charming', 'adorable', 'facetious', 'expensive', 'tantalizing', 'grotesque', 'amiable', 'drunk', 'bumfuzzel', 'cattywhampus', 'lollygag']
ad_verbs1 = ['lively', 'gratefully', 'youthfully', 'innocently', 'gently', 'loudly', 'boldly', 'elegantly', 'dreamily', 'daintily', 'awkwardly', 'madly', 'greedily', 'joyously', 'eagerly', 'quickly', 'quietly', 'hungrily', 'loosely',  'madly', 'evily', 'maliciously', 'cruelly']
nouns1 = ['cat','cow', 'frog', 'butt', 'mouthwash','balloon', 'park', 'milkshake','baseball', 'tiger', 'flower', 'jungle','man', 'woman', 'dog', 'ankle', 'slide', 'tree', 'house', 'hood', 'hill', 'swingset', 'flap', 'nook']
p_verbs1 = ['ran', 'cried', 'laughed', 'danced', 'yelled', 'slept', 'dreamed', 'played', 'dug', 'swam', 'wrote', 'grew', 'flew', 'fought', 'thought', 'used', 'knew', 'went', 'sang', 'died', 'dyed', 'drove', 'typed', 'farted', 'plucked', 'rammed', 'dwaddled']

# get random words (we are using functions for each word type to ensure that a new random word gets chosen each time):

def verb():
  return random.choice(verbs1)
def ad_verb():
  return random.choice(ad_verbs1)
def adjective():
  return random.choice(adjectives1)
def noun():
  return random.choice(nouns1)
def p_verb():
  return random.choice(p_verbs1)
  #these functions will just return a random adjective, verb, noun, or past tense verb from the list above