from ex48 import lexicon
from sys import argv

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, input):
        self.input = lexicon.scan(input)

    def remove_unwanted(self):
        # Removes word with category 'stop' or 'error'
        new_input = []

        for item in self.input:
            if item[0] not in ['stop', 'error']:
                new_input.append(item)
            else:
                pass

        if new_input:
            self.input = new_input

    def subject(self):
        for item in self.input:
            if item[0] == 'noun':
                subject = item[1]
                break
            elif category == 'verb':
                subject = 'player'
                break

        return subject


    def verb(self):
        for item in self.input:
            if item[0] == 'verb':
                verb = item[1]
                break
            else:
                verb = None
                if item is self.input[-1]:
                    raise ParserError('No verb found.')

        return verb


    def object(self):
        for item in self.input:
            if item[0] in ['direction', 'noun']:
                if item[1] == self.subject():
                    pass
                else:
                    object = item[1]
                    break
            else:
                object = None
                if item is self.input[-1]:
                    raise ParserError('No object found.')

        return object

    def assemble(self):
        self.remove_unwanted()
        subject = self.subject()
        verb = self.verb()
        object = self.object()

        print(f'subject: {subject}, verb: {verb}, object: {object}' )

#script, input = argv
#print('\n' * 20)
#scoot = Sentence(input)
#scoot.assemble()
