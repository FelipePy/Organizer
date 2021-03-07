from organizer import Organizer
from so import So


class Main:

    organizer = Organizer()
    so = So()
    directory = so.get_directory()
    try:
        organizer.organizer(directory)
    except:
        print("Algo deu errado, Tente novamente")
        print("Ou Contate-nos -> https://github.com/FelipePy/Organizer")
        exit(0)