#	Organizer
[![NPM](https://img.shields.io/github/license/FelipePy/Organizer)](https://github.com/FelipePy/Organizer/blob/master/LICENSE)

### Linguagem
 - Python

### Saída
![WhatsApp Image 2021-04-28 at 18 27 57](https://user-images.githubusercontent.com/60964439/116474909-7d1f0600-a84f-11eb-8256-6cd6101a969f.jpeg)

## Como instalar no Ubuntu
1. Clone o repositório
> git clone https://github.com/FelipePy/Organizer.git
Ou baixe o projeto diretamente
[DOWNLOAD](https://github.com/FelipePy/Organizer.git)

2. Desencriptar o arquivo

3. Mova a pasta para onde deseja deixar o script

> mv Organizer ~/.Organizer

4. Dentro da pasta Organizer, mova o arquivo Organizer para um diretório de execução\
```mv Organizer /usr/bin/Organizer```

5. Abra o arquivo\
> sudo vim /usr/bin/Organizer

5.1 Altere o caminho do arquivo mudando a variável "DIR" para o diretório onde deixará os arquivos do script\
```
#!/bin/bash

 -> DIR="/home/user/.Organizer/"

cat $DIR"Banner.txt"
/usr/bin/env python3 $DIR"src/"main.py $1
```

6. De permissão de execução para o script\
> sudo chmod +x /usr/bin/Organizer

# Execução do script
### Há duas maneiras de executar o script

1. Entre no diretório a ser organizado e utilize o comando ```Organizer```

1.1 Utilize o comando Organizer --diretorio para organizar outro diretório
> Organizer ~/Downloads

## Observação: Muito cuidado, executar o comando em algum diretório delicado, pode danificar o sistema.
