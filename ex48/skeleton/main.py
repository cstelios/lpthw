from ex48 import lexicon
from ex48 import parser

test = parser.Sentence('64 hey! Bear eat the honey please')
print(test.words_list)
test.skip('number')
print(test.words_list)
