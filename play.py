import winsound as ws

class Play:
    """A class to play sound effects asynchronously
    """

    def __init__(self, sound_effect: str):
        self.sound_effect = sound_effect
        self.is_playing = False

    def is_playing(self):
        return self.is_playing
    
    def play(self):
        if not self.is_playing:
            self.is_playing = True
            ws.PlaySound(self.sound_effect, ws.SND_ASYNC)
    
    def stop(self):
        if self.is_playing:
            self.is_playing = False
            ws.PlaySound(None, ws.SND_PURGE)