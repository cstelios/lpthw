class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def add_artist(self, artist_name):
        self.lyrics.append(artist_name)

happy_bday = Song(['Happy birthday to you',
                    'I don\'t want to get sued',
                    'So I\'ll stop right there.'])

bulls_on_parade = Song(["They rally arounf tha family",
                        "With pockets full of shells"])



happy_bday.sing_me_a_song()

happy_bday.add_artist("Stelios")

happy_bday.sing_me_a_song()

print()

kostis = happy_bday

kostis.sing_me_a_song()
kostis.add_artist("KOSTIS!!!")

happy_bday.sing_me_a_song()
#bulls_on_parade.sing_me_a_song()
