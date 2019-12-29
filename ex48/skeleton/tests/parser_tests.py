from nose.tools import *
from ex48 import parser

test_input = '65 hey! Bear eat the honey 45 please'
test_sentence = parser.Sentence(test_input)

def test__init__():
    assert_equal(test_sentence.words_list, [('number', 65),
                                            ('error', 'hey!'),
                                            ('noun', 'bear'),
                                            ('verb', 'eat'),
                                            ('stop', 'the'),
                                            ('noun', 'honey'),
                                            ('number', 45),
                                            ('error', 'please')])


def test_skip():
    test_sentence.skip('number')
    assert_equal(test_sentence.words_list,[('error', 'hey!'),
                                           ('noun', 'bear'),
                                           ('verb', 'eat'),
                                           ('stop', 'the'),
                                           ('noun', 'honey'),
                                           ('error', 'please')])

    test_sentence.skip('error')
    assert_equal(test_sentence.words_list,[('noun', 'bear'),
                                           ('verb', 'eat'),
                                           ('stop', 'the'),
                                           ('noun', 'honey')])
    test_sentence.skip('stop')
    assert_equal(test_sentence.words_list,[('noun', 'bear'),
                                           ('verb', 'eat'),
                                           ('noun', 'honey')])

def test_peek():
    assert_equal(test_sentence.peek(), 'noun')
    assert_equal(parser.Sentence("").peek(), None)

def test_match():
    assert_equal(test_sentence.match('verb'), None)
    assert_equal(test_sentence.match('noun'), 'bear')
    assert_equal(test_sentence.words_list, [('verb', 'eat'),
                                            ('noun', 'honey')])
    assert_equal(parser.Sentence("").match('noun'), None)



def test_parse_subject():
    assert_equal(parser.Sentence('bear eat honey').parse_subject(), 'bear')
    assert_equal(parser.Sentence('eat honey').parse_subject(), 'player')
    #with assert_raises(parser.ParserError) as cm:
    #    parser.Sentence("").parse_subject()
    #ex = cm.exception
    #ok_(ex.error == 'Expected verb. Reached end of input')
