class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = 'MP4'

movie = Movie_MP4(r'C:\Users\yorkh\Documents\GitHub\protectu_python\app\main\videos\1.flv')
movie.play()