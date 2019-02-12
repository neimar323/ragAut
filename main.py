from time import sleep
from imagesearch import *
from regionRag import *
import pyautogui
import datetime


tempoInicial = 0
tempoUsandoComida1 = datetime.timedelta(0,1800)
tempoEmBatalha = datetime.timedelta(0)
ultimoTempoBatalha = None
tempoUsandoBuff_1 = datetime.timedelta(0,1)
regionBuff = None
tempoMapa = datetime.timedelta(0,1)
tempoDecorrido = datetime.timedelta(0,1)
def verificaJogoAtivo():
    ragImagPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\ragnarok.png'
    imgR = imagesearch(ragImagPath)
    if imgR is None:
        sleep(5)
        print('Ragnarok nao ativo')
        verificaJogoAtivo()
    else:
        posicionaVerificacaoDeBuffs()
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
    global temp
    global tempoUsandoComida1
    if tempoDecorrido > tempoUsandoComida1:
        usaComida1()
        tempoUsandoComida1 = tempoUsandoComida1 + datetime.timedelta(0,1800)

#usando pro bless
def verificaBuff_1():
    global regionBuff
    buff_1Path = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\bless.png'
    #imgR = imagesearch(buff_1Path, 0.7)
    imgR = imagesearchareaRag(buff_1Path, regionBuff, precision=0.8)
    buff_1HalfoPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\blessHalf.png'
    #imgR2 = imagesearch(buff_1HalfoPath, 0.7)
    imgR2 = imagesearchareaRag(buff_1HalfoPath, regionBuff, precision=0.8)
    #se nao achou, entao tem q dar call
    if imgR is None:
        if imgR2 is None:
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
    global regionBuff
    callSpiritsPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\callSpirits.png'
    imgR = imagesearch(callSpiritsPath, 0.7)
    imgR = imagesearchareaRag(callSpiritsPath, regionBuff, precision=0.9)
    #se nao achou, entao tem q dar call
    if imgR is None:
        usaCallSpirits()

def posicionaVerificacaoDeBuffs():
    bandeiraLvlPath = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\bandeiraLvl.png'
    imgR = imagesearch(bandeiraLvlPath, 0.7)
    #se nao achou, entao tem q dar call
    if imgR is not None:
        global regionBuff
        #depois de debugar umas 10 vezes cheguei nessa regiao
        regionBuff = RegionRag(imgR[0]-30, imgR[1]+30, imgR[0] + 80, imgR[1] + 130)
        #imagesearchareaRag(bandeiraLvlPath, regionBuff, precision=0.8)

def imagesearchareaRag(image, regionRag, precision=0.8, im=None):
    return imagesearcharea(image, regionRag.x1, regionRag.y1, regionRag.x2, regionRag.y2, precision, im)


def irPosicaoMapa(tempoSegundos,x,y):
    global tempoMapa
    global tempoDecorrido
    tempoDatetime = datetime.timedelta(0, tempoSegundos)

    if tempoMapa+tempoDatetime < tempoDecorrido:
        print('Reposicionando')
        pyautogui.typewrite('M')
        tempoMapa = tempoDecorrido
        sleep(1)
        mundo = r'C:\Users\Neimar\PycharmProjects\ragAutomation\imagens\mundo.png'
        imgR = imagesearch(mundo, 0.7)
        if imgR is not None:
            if imgR[0] != -1:
                pyautogui.click(imgR[0]+x, imgR[1]+y)
                pyautogui.typewrite('M')

def mainMonk():
    global tempoInicial
    tempoInicial = datetime.datetime.now()
    while True:
        verificaJogoAtivo()
        #verificaVida()
        #verificaMana()
        verificaTempoBatalha()
        verificaTempoAtivo()
        verificaBuffComida()
        verificaBuff_1()
        verificaCallSpirits()
        irPosicaoMapa(300, 150, -60)
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
        verificaBuffComida()
        #irPosicaoMapa(600,175, -215)

        sleep(3)
#MAIN
mainMonk()


#spots
#irPosicaoMapa(120, 200, -215) #prontera north spot dustness 2
#irPosicaoMapa(120, 175, -215) #prontera north spot dustness 1
#irPosicaoMapa(50, 150, -60)  #anthell escadaZ