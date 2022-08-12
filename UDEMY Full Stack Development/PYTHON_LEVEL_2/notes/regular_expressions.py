import re

patterns = ['term1', 'term2']

text = 'This is a string with term1 :D'

for pattern in patterns:
    print("I'm searching for: " + pattern)
    if re.search(pattern, text):
        print('MATCH')
    else:
        print("no match!")

match = re.search('term1', text) # re.search return a special class with several class attributes
print((match.start())) # outputs what index the match appears

# splitting strings

split_term = '@'
email = 'Jherrera2@mail.fresnostate.edu'

outPut = re.split(split_term, email)

print(outPut) # outputs 

# re.findall

print(re.findall('match', 'test phrase match in middle and match and match'))

# metric character syntax

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
test_patters = ['sd*'] # find s with 0 or more d's
test_patters = ['sd+'] # find s with 1 or more d's
test_patters = ['sd?'] # find s with 0 or 1 d's
test_patters = ['sd{3}'] # find s with literally any amount i put
test_patters = ['sd{1,3}'] # find s with literally any amount i put, and other ones
test_patters = ['s[sd]+'] # find s with 1 or more s OR d's
multi_re_find(test_patters, test_phrase)

# EXCLUSION:

testie = 'wow punctuation! take it out now ;-;? ok. 12312247435'
patterns = ['[^!.?]+'] # exclude (^) one or more of these punc things
patterns = ['[a-z]+'] # all lowercase 
patterns = [r'\d+'] # only digits

multi_re_find(patterns, testie)

# HOW TO GOOGLE:
# re module?
# google REGULAR EXPRESSIONS