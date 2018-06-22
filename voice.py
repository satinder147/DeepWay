from pygame import mixer
class Voice:
    def right(self):
        mixer.init()
        mixer.music.load('right.mp3')
        mixer.music.play()
    def left(self):
        mixer.init()
        mixer.music.load('left.mp3')
        mixer.music.play()
    def stop_left(self):
        mixer.init()
        mixer.music.load('stop_left.mp3')
        mixer.music.play()
    def stop_right(self):
        mixer.init()
        mixer.music.load('stop_right.mp3')
        mixer.music.play()
    def peopleOnRight(self):
        mixer.init()
        mixer.music.load('face_right.mp3')
        mixer.music.play()
    def peopleOnLeft(self):
        mixer.init()
        mixer.music.load('face_left.mp3')
        mixer.music.play()
        
