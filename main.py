from time import sleep
from imagesearch import *
import pyautogui
import datetime


tempoInicial = 0
tempoUsandoComida1 =  datetime.timedelta(0,1800)
tempoEmBatalha = datetime.timedelta(0)
ultimoTempoBatalha = None

def verificaJogoAtivo():
    ragImagPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\ragnarok.png'
    imgR = imagesearch(ragImagPath)
    if imgR is None:
        sleep(5)
        print('Ragnarok nao ativo')
        verificaJogoAtivo()
    else:
        return

def verificaVida():
    vidaImgPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\vida.png'
    imgR = imagesearch(vidaImgPath, 0.98)
    #imgR = imagesearcharea(vidaImgPath,120, 0, 270, 200, precision=0.98, im=None)
    if imgR is not None:
        usaPoteVida()
    else:
        print('Vida OK')
    return

def verificaMana():
    manaImgPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\mana.png'
    imgR = imagesearch(manaImgPath, 0.98)
    #imgR = imagesearcharea(manaImgPath,120, 0, 270, 200, precision=0.98, im=None)
    if imgR is not None:
        usaPoteMana()
    else:
        print('Mana OK')
    return

def usaPoteVida():
    print('Potando Vida')
    pyautogui.typewrite('C')
    return

def usaPoteMana():
    print('Potando Mana')
    pyautogui.typewrite('V')
    return

def usaComida1():
    print('Usando comida1!')
    #pyautogui.typewrite('V')
    return

def verificaBuffComida():
    global tempoEmBatalha
    global tempoUsandoComida1
    if tempoEmBatalha > tempoUsandoComida1:
        usaComida1()
        tempoUsandoComida1 = tempoUsandoComida1 + datetime.timedelta(0,1800)


def verificaTempoBatalha():
    global tempoInicial
    global ultimoTempoBatalha
    global tempoEmBatalha
    emBatalhaImgPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\emBatalha.png'
    imgR = imagesearch(emBatalhaImgPath, 0.9)
    if imgR is not None:
        if ultimoTempoBatalha is not None:
            tempoEmBatalha = tempoEmBatalha + (datetime.datetime.now() - ultimoTempoBatalha)
            print('Em batalha! '+ str(tempoEmBatalha))

        ultimoTempoBatalha = datetime.datetime.now()
    else:
        print('Não está em batalha?!?!')
        ultimoTempoBatalha = None
    return

def verificaTempoAtivo():
    global tempoInicial
    global tempoDecorrido
    tempoAgora = datetime.datetime.now()
    tempoDecorrido = tempoAgora - tempoInicial
    print('Tempo decorrido: ' + str(tempoDecorrido))

def main():
    global tempoInicial
    tempoInicial = datetime.datetime.now()
    while True:
        verificaJogoAtivo()
        verificaVida()
        verificaMana()
        verificaTempoBatalha()
        verificaTempoAtivo()
        verificaBuffComida()
        sleep(3)
#MAIN
main()