import os
from so import So

class Organizer:

    def __init__(self):
        self.audios_ext = ['.mp3', '.wav', '.wma', '.ogg', '.aiff', '.pcm', '.flac']
        self.videos_ext = ['.mp4', '.m4v', '.mov', '.avi', '.mov', '.mpg', '.mpeg', '.wmv']
        self.images_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.exif', '.raw']
        self.documents_ext = ['.txt', '.log', '.pdf', '.docx', '.pptx', '.word', '.xlsx', '.ppt', '.psd', '.cdr', '.ai']
        self.programs_ext = ['.exe', '.py', '.c', '.cpp', '.js', '.zip', '.rar', '.bin', '.sh', '.ini', '.jar', '.java',
                         '.jav',
                         '.izh', '.msi']
        self.so = So()
        print("TESTE")

    def organizer(self, directory):
        aud = [0, "audios"]
        img = [0, "imagens"]
        vid = [0, "videos"]
        doc = [0, "documentos"]
        pro = [0, "programas"]
        out = [0, "outros"]
        abrev = [aud, img, vid, doc, pro, out]
        folders = ["audios", "imagens", "videos", "documentos", "programas", "outros"]
        formats = [self.audios_ext, self.images_ext, self.videos_ext, self.documents_ext, self.programs_ext]

        counter = 0
        archives_names = os.listdir(directory)

        for archive in archives_names:
            new_folder = os.path.join(directory, folders[0])
            if os.path.isfile(os.path.join(directory, archive)):
                counter += 1
                count = 0
                extension = self.get_extension(archive)

                for format in formats:
                    if extension in format:
                        new_folder = os.path.join(directory, folders[count])
                        if folders[count] == abrev[count][1]:
                            self.create_folder(new_folder)
                            abrev[count][0] += 1
                            break

                    count += 1
                    if folders[count] == "outros":
                        self.create_folder(new_folder)
                        out[0] += 1
                    new_folder = os.path.join(directory, folders[-1])

                old = os.path.join(directory, archive)
                new = os.path.join(new_folder, archive)
                os.rename(old, new)

                index = new_folder.rfind('/')
                print(f"Moveu o \033[33m{archive}\033[0m de", directory, "->", new_folder[index:])

        print(f"\n\nSistema Operacional -> {self.so.get_so()}")
        print(f"\033[34mTotal de arquivos organizados -> \033[0m\033[31m{counter}\033[0m")
        for abv in abrev:
            if abv[0] > 0:
                print(abv[1], "->", abv[0])


    def create_folder(self, folder):
        folder = os.path.join(folder)
        if not os.path.isdir(folder):
            os.mkdir(folder)
            print(f"Pasta criada -> {folder}")

    def check_arguments(self):
        print("Verificou os argumentos")
        pass

    def get_extension(self, archive):
        index = archive.rfind('.')
        return archive[index:]