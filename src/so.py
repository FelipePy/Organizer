import os
import sys
import platform
from time import sleep


class So:

    def get_so(self):
        return platform.system()

    def question(self):
        while True:
            resposta = str(
                input("\033[31mTem certeza que deseja organizar na pasta root? [S/N]: \033[0m")).upper()
            if resposta == "S":
                return 0
            elif resposta == "N":
                print("\033[94mEncerrando...\n\033[0m")
                sleep(1.5)
                exit()
            else:
                print("\033[94mOpção incorreta!\033[0m")
                exit()

    def check_user_linux(self, directory):
        index_local = directory.rfind("/")
        user = os.path.join(os.path.expanduser("~")).strip()
        index_user = user.rfind("/")

        if user[index_user:] == directory[index_local:]:
            if self.question() == 0:
                return directory

    def check_user_windows(self): #TODO
        pass

    def get_directory(self):
        arguments = sys.argv
        so = self.get_so()
        directory = ""
        if len(arguments) < 2: # == 0
            directory = os.getcwd().strip()

            if so == "Linux":
                directory = self.check_user_linux(directory)

        elif len(arguments) > 2:
            while True:
                resposta = str(input("Deseja ver o modo de uso ? [S/N]: ")).upper()
                if resposta == "S":
                    print("\n\033[31mModo de uso -> python3 Organizacao.py [diretorio]\033[0;0m")
                    exit(0)
                elif resposta == "N":
                    print("\033[94mAté logo!\033[0m")
                    exit(0)
                else:
                    print("\033[94mOpção incorreta!\033[0m")
                    exit(0)

        else:
            directory = arguments[1]

        return directory