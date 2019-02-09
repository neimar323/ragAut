from time import sleep
from imagesearch import *
import pyautogui
import datetime


tempoInicial = 0
tempoUsandoComida1 =  datetime.timedelta(0,1800)
tempoEmBatalha = datetime.timedelta(0)
ultimoTempoBatalha = None
tempoUsandoBuff_1 = datetime.timedelta(0,1)

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
def usaBuff_1():
    print('Usando Buff_1!')
    pyautogui.typewrite('QQ')
    return

def usaCallSpirits():
    print('Usando CallSpirits!')
    pyautogui.typewrite('Z')
    return

def verificaBuffComida():
    global tempoEmBatalha
    global tempoUsandoComida1
    if tempoEmBatalha > tempoUsandoComida1:
        usaComida1()
        tempoUsandoComida1 = tempoUsandoComida1 + datetime.timedelta(0,1800)

#usando pro bless
def verificaBuff_1():
    buff_1Path = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\bless.png'
    imgR = imagesearch(buff_1Path, 0.95)
    #se nao achou, entao tem q dar call
    if imgR is None:
        usaBuff_1()


def verificaTempoBatalha():
    global tempoInicial
    global ultimoTempoBatalha
    global tempoEmBatalha
    emBatalhaImgPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\emBatalha.png'
    imgR = imagesearch(emBatalhaImgPath, 0.2)
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

def verificaCallSpirits():
    callSpiritsPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\callSpirits.png'
    imgR = imagesearch(callSpiritsPath, 0.99)
    #se nao achou, entao tem q dar call
    if imgR is None:
        usaCallSpirits()

def mainMonk():
    global tempoInicial
    tempoInicial = datetime.datetime.now()
    while True:
        verificaJogoAtivo()
        #verificaVida()
        #verificaMana()
        verificaTempoBatalha()
        verificaTempoAtivo()
        #verificaBuffComida()
        verificaBuff_1()
        verificaCallSpirits()
        sleep(3)

def mainWiz():
    global tempoInicial
    tempoInicial = datetime.datetime.now()
    while True:
        verificaJogoAtivo()
        #verificaVida()
        #verificaMana()
        verificaTempoBatalha()
        verificaTempoAtivo()
        #verificaBuffComida()
        sleep(3)
#MAIN
mainMonk()