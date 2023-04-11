#	Organizer
[![NPM](https://img.shields.io/github/license/FelipePy/Organizer)](https://github.com/FelipePy/Organizer/blob/master/LICENSE)

## Como instalar no Ubuntu
1. Clone o repositório
> git clone https://github.com/FelipePy/Organizer.git
Ou baixe o projeto diretamente
[DOWNLOAD](https://github.com/FelipePy/Organizer.git)

2. Desencriptar o arquivo

3. Mova a pasta para sua pasta pessoal

> mv Organizer ~/.Organizer

4. Dentro da pasta Organizer, mova o arquivo Organizer para um diretório de execução\
> mv Organizer /usr/bin/Organizer

5. Abra o arquivo\
> sudo vim /usr/bin/Organizer

5.1 Configure a variável "DIR" apontando para a pasta principal\
```
#!/bin/bash

 -> DIR="/home/user/.Organizer/"

cat $DIR"Banner.txt"
/usr/bin/env python3 $DIR"src/"main.py $1
```

6. De permissão de execução para o script\
> sudo chmod +x /usr/bin/Organizer

## Execução do script
### Há duas maneiras de executar o script

1. Entre no diretório a ser organizado e utilize o comando ```Organizer```

1.1 Utilize o comando Organizer --diretorio para organizar outro diretório
> Organizer ~/Downloads

## Observação: Muito cuidado, executar o comando em algum diretório delicado, pode danificar o sistema.
