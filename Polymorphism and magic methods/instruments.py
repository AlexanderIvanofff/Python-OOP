class Guitar:
    def play(self):
        print("playing the guitar")


def play_instrument(instruments):
    return instruments.play()


class Piano:
    def play(self):
        print("playing the piano")


guitar = Guitar()
play_instrument(guitar)

piano = Piano()
play_instrument(piano)
