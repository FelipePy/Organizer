from organizer import Organizer
from so import So



class Main:


    organizer = Organizer()
    so = So()
    directory = so.get_directory()
    organizer.organize(directory)