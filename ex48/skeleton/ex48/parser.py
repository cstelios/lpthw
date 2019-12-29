from ex48 import lexicon

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, input):
        self.words_list = lexicon.scan(input)
        self.subject = ""
        self.verb = ""
        self.object = ""


    def peek(self):
        if self.words_list:
            return self.words_list[0][0]
        else:
            return None


    def match(self, expected_category):
        if self.words_list:
            if self.words_list[0][0] == expected_category:
                word = self.words_list.pop(0)
                return word[1]
            else:
                return None
        else:
            return None


    def skip(self, skipped_category):
        if self.words_list:
            useful_words = []
            for word in self.words_list:
                if word[0] != skipped_category:
                    useful_words.append(word)
                else:
                    pass

            self.words_list = useful_words


    def parse_subject(self):
        if self.words_list:
            if self.peek() == 'noun':
                return self.match('noun')
            elif self.peek() == 'verb':
                return 'player'
            else:
                raise ParserError(f'Expected noun or verb before: {self.words_list[0]}.')
        else:
            raise ParserError('Expected noun or verb. Reached end of input')

    def parse_verb(self):
        if self.words_list:
            if self.peek() == 'verb':
                return self.match('verb')
            else:
                raise ParserError(f'Expected verb before: {self.words_list[0]}.')
        else:
            raise ParserError('Expected verb. Reached end of input')


    def parse_object(self):
        if self.words_list:
            if self.peek() == 'noun':
                return self.match('noun')
            else:
                raise ParserError(f'Expected noun before: {self.words_list[0]}.')
        else:
            raise ParserError('Expected noun. Reached end of input')


    def built_sentence(self):
        self.skip('stop')
        self.skip('error')
        self.subject = self.parse_subject()
        self.verb = self.parse_verb()
        self.object = self.parse_object()
        print(f'Subject: {self.subject}, Verb: {self.verb}, Object: {self.object}')
