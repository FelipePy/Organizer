#!/usr/bin/env python
# -- coding: utf-8 --

from time import sleep
import os
import sys
import platform

# Listas dos arquivos de cada pasta
audios_ext = ['.mp3', '.wav', '.wma', '.ogg', '.aiff', '.pcm', '.flac']
videos_ext = ['.mp4', '.m4v', '.mov', '.avi', '.mov', '.mpg', '.mpeg', '.wmv']
imagens_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.psd', '.exif', '.raw']
documentos_ext = ['.txt', '.log', '.pdf', '.docx', '.pptx', '.word', '.xlsx', '.ppt', '.psd', '.cdr', '.ai']
programas_ext = ['.exe', '.py', '.c', '.cpp', '.js', '.zip', '.rar', '.bin', '.sh', '.ini', '.jar', '.java', '.jav',
                 '.izh', '.msi']

local = ""
def criar_pasta(pasta):
    if not os.path.isdir(os.path.join(pasta)):
        os.mkdir(os.path.join(pasta))

def organizar(diretorio):
    aud = [0, "audios"]
    img = [0, "imagens"]
    vid = [0, "videos"]
    doc = [0, "documentos"]
    pro = [0, "programas"]
    out = [0, "outros"]
    abrev = [aud, img, vid, doc, pro, out]
    pastas = ["audios", "imagens", "videos", "documentos", "programas", "outros"]
    formatos = [audios_ext, imagens_ext, videos_ext, documentos_ext, programas_ext]

    contador = 0
    nomes_arquivos = os.listdir(diretorio)

    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            contador += 1
            cont = 0
            extensao = str.lower(pegar_extensao(arquivo))

            for formato in formatos:
                if extensao in formato:
                    nova_pasta = os.path.join(diretorio, pastas[cont]) 

                    if pastas[cont] == abrev[cont][1]:
                        abrev[cont][0] += 1
                        
                    criar_pasta(nova_pasta)
                    break
                
                cont += 1
                if pastas[cont] == "outros":
                    criar_pasta(nova_pasta)
                    out[0] += 1
                nova_pasta = os.path.join(diretorio, pastas[-1])

            velho = os.path.join(diretorio, arquivo)

            novo = os.path.join(nova_pasta, arquivo)

            os.rename(velho, novo)

            print(f"Moveu o \033[33m{arquivo}\033[0m de", diretorio, "->", nova_pasta)

    print(f"\n\nSistema Operacional -> {pegar_so()}")
    print(f"\033[34mTotal de arquivos organizados -> \033[0m\033[31m{contador}\033[0m")
    conta = 0
    for abv in abrev:
        if abv[0] > 0:
            print(abv[1], "->", abv[0]) 

def verificar_argumentos():
    if len(sys.argv) < 2:
        return 0
    elif len(sys.argv) > 2:
        while True:
            resposta = str(input("Deseja ver o modo de uso ? [S/N]: ")).upper()
            if resposta == "S":
                print("\n\033[31mModo de uso -> python3 Organizacao.py [diretorio]\033[0;0m")
                break
            elif resposta == "N":
                print("\033[94mAté logo!\033[0m")
                break
            else:
                print("\033[94mOpção incorreta!\033[0m")

            return 1
    else:
        return sys.argv[1]


def pegar_so():
    return platform.system()


def verificar_usuario_linux():
    index_local = local.rfind("/")
    usuario = os.path.join(os.path.expanduser("~")).strip()
    index_usuario = usuario.rfind("/")

    if usuario[index_usuario:] == local[index_local:]:
        pergunta()


def verificar_usuario_windows():
    usuario = os.path.join(os.path.expanduser("~")).strip()
    if usuario[1:] == local[1:]:
        pergunta()


def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]


def pergunta():
    while True:
        resposta = str(
            input("\033[31mTem certeza que deseja organizar na pasta root? [S/N]: \033[0m")).upper()
        if resposta == "S":
            organizar(local)
            break
        elif resposta == "N":
            print("\033[94mEncerrando...\n\033[0m")
            sleep(1.5)
            break
        else:
            print("\033[94mOpção incorreta!\033[0m")
    exit()


if __name__ == '__main__':
    local = verificar_argumentos()
    sistema_operacional = pegar_so()
    if local == 0:
        local = os.getcwd().strip()
        if sistema_operacional == "Linux":
            verificar_usuario_linux()

        elif sistema_operacional == "Windows":
            verificar_usuario_windows()

        organizar(local)

    elif local == 1:
        exit()

    else:
        try:
            organizar(local)
        except ValueError:
            print("\033[31mAção inesperada ou diretório inexistente!\033[0m")
