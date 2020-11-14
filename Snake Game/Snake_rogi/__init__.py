import sys
import pygame
import random

def show_score(pontuacao,screen):
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    pontos = fonte.render(f"{pontuacao}",True,(255, 255, 255),(0, 0, 0))
    screen.blit(pontos,(20,20))

def survival():
    score = 0
    tempo = 0
    fps = pygame.time.Clock()
    class snake:
        def __init__(self, cor, vel, larg, comp):
            self.cor = cor
            self.vel = vel
            self.larg = larg
            self.comp = comp

    x = random.randrange(50, 860, 10)
    y = random.randrange(50, 560, 10)

    serpente = snake((200, 0, 200), 10, 10, 10)
    cobra = [[x,y]] #minha maior vigarice

    class borda:
        def __init__(self, x, y, largura, comprimento):
            self.x = x #5
            self.y = y #5
            self.largura = largura #5
            self.comprimento = comprimento #890
            self.cor = (255, 255, 255) #RGB

    borda_cima = borda(5, 5, 5, 890) #Borda
    borda_baixo = borda(5, 590, 5, 890) #Borda
    borda_direita = borda(890, 5, 590, 5) #Borda
    borda_esquerda = borda(5, 5, 590, 5) #Borda

    class comida:
        x = random.randrange(20,880, 10)
        y = random.randrange(20,580, 10)
        largura = 10
        comprimento = 10
        cor = (0,255,0) #RGB

    cima = (0, -1)
    baixo = (0, 1)
    direita = (1, 0)
    esquerda = (-1, 0)

    mov = random.choice([cima, baixo, direita, esquerda])

    pygame.init()
    tela = pygame.display.set_mode((900, 600)) #Resolução da tela
    pygame.display.set_caption("Snake") #Nome da janela
    pygame.mouse.set_visible(0) #Oculta o mouse

    aberto = True
    while aberto:
        if len(cobra)<=10:
            fps.tick(10)
        elif len(cobra)<=20:
            fps.tick(len(cobra))
        else:
            fps.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Checa se o usuário fechou o jogo
                aberto = False
                break

            elif event.type == pygame.KEYDOWN: #checa os controles
                if event.key == pygame.K_w and not mov == baixo:
                    mov = cima
                elif event.key == pygame.K_s and not mov == cima:
                    mov = baixo
                elif event.key == pygame.K_a and not mov == direita:
                    mov = esquerda
                elif event.key == pygame.K_d and not mov == esquerda:
                    mov = direita
                elif event.key == pygame.K_ESCAPE:
                    tela.fill((0,0,0))
                    return


        if len(cobra)>1: #Colisão com a própria cobra
            for i in range(1,len(cobra)-1):
                if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
                    cobra = [[0,0]]
                    cobra[0][0] = random.randrange(50,850,10)
                    cobra[0][1] = random.randrange(50,550,10)
                    break 




        for i in range(len(cobra) - 1, 0, -1): #faz as "curvas" da cobra(unico motivo por eu ter refeito o código inteiro foi procurar algo pra resolver isso.......
            cobra[i] = (cobra[i-1][0], cobra[i-1][1])

        cobra[0][0] += mov[0]*serpente.vel
        cobra[0][1] += mov[1]*serpente.vel



        tela.fill((0, 0, 0)) #preenche de preto

        show_score(score,tela)

        pygame.draw.rect(tela, comida.cor,(comida.x, comida.y, comida.comprimento, comida.largura))#Comida
        if cobra[0][0] == comida.x and cobra[0][1] == comida.y:
            comida.x = random.randrange(20,880, 10)
            comida.y = random.randrange(20,580, 10)
            if len(cobra)>=3:
                cobra.pop()
                cobra.pop()
            score += 10
        if cobra[0][0] >= 890 or cobra[0][0] < 10 or cobra[0][1] >= 590 or cobra[0][1] < 10: #checa colisões com as bordas
            cobra[0][0] = random.randrange(50,850,10)
            cobra[0][1] = random.randrange(50,550,10)
            for i in range(len(cobra)-1):
                cobra.pop()
            score = 0   #Verificar arquivo de pontos, quando este for criado

        tempo += 0.1
        if tempo >= 2.5:
            cobra.append([990 ,660])
            cobra.append([1000,700])
            tempo = 0
        for i in range(len(cobra)):  #Desenhar a cobra com base no comprimento(número de tuplas)
            pygame.draw.rect(tela, serpente.cor, (cobra[i][0], cobra[i][1], serpente.comp, serpente.larg))

        pygame.draw.rect(tela, borda_cima.cor, (borda_cima.x, borda_cima.y, borda_cima.comprimento, borda_cima.largura)) #Bordas
        pygame.draw.rect(tela, borda_baixo.cor, (borda_baixo.x, borda_baixo.y, borda_baixo.comprimento, borda_baixo.largura))
        pygame.draw.rect(tela, borda_esquerda.cor, (borda_esquerda.x, borda_esquerda.y, borda_esquerda.comprimento, borda_esquerda.largura))
        pygame.draw.rect(tela, borda_direita.cor, (borda_direita.x, borda_direita.y, borda_direita.comprimento, borda_direita.largura))
        pygame.display.update()

    pygame.quit()
    sys.exit()

def singleplayer():
    score = 0
    fps = pygame.time.Clock()
    class snake:
        def __init__(self, cor, vel, larg, comp):
            self.cor = cor
            self.vel = vel
            self.larg = larg
            self.comp = comp

    x = random.randrange(50, 860, 10)
    y = random.randrange(50, 560, 10)

    serpente = snake((200, 0, 200), 10, 10, 10)
    cobra = [[x,y]] #minha maior vigarice

    class borda:
        def __init__(self, x, y, largura, comprimento):
            self.x = x #5
            self.y = y #5
            self.largura = largura #5
            self.comprimento = comprimento #890
            self.cor = (255, 255, 255) #RGB

    borda_cima = borda(5, 5, 5, 890) #Borda
    borda_baixo = borda(5, 590, 5, 890) #Borda
    borda_direita = borda(890, 5, 590, 5) #Borda
    borda_esquerda = borda(5, 5, 590, 5) #Borda

    class comida:
        x = random.randrange(20,880, 10)
        y = random.randrange(20,580, 10)
        largura = 10
        comprimento = 10
        cor = (0,255,0) #RGB

    cima = (0, -1)
    baixo = (0, 1)
    direita = (1, 0)
    esquerda = (-1, 0)

    mov = random.choice([cima, baixo, direita, esquerda])

    pygame.init()
    tela = pygame.display.set_mode((900, 600)) #Resolução da tela
    pygame.display.set_caption("Snake") #Nome da janela
    pygame.mouse.set_visible(0) #Oculta o mouse

    aberto = True
    while aberto:
        if len(cobra)<=10:
            fps.tick(10)
        elif len(cobra)<=20:
            fps.tick(len(cobra))
        else:
            fps.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Checa se o usuário fechou o jogo
                aberto = False
                break

            elif event.type == pygame.KEYDOWN: #checa os controles
                if event.key == pygame.K_w and not mov == baixo:
                    mov = cima
                elif event.key == pygame.K_s and not mov == cima:
                    mov = baixo
                elif event.key == pygame.K_a and not mov == direita:
                    mov = esquerda
                elif event.key == pygame.K_d and not mov == esquerda:
                    mov = direita
                elif event.key == pygame.K_ESCAPE:
                    tela.fill((0,0,0))
                    return


        if len(cobra)>1:
            for i in range(1,len(cobra)-1):
                if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
                    cobra = [[0,0]]
                    cobra[0][0] = random.randrange(50,850,10)
                    cobra[0][1] = random.randrange(50,550,10)
                    score = 0
                    break 




        for i in range(len(cobra) - 1, 0, -1): #faz as "curvas" da cobra(unico motivo por eu ter refeito o código inteiro foi procurar algo pra resolver isso.......
            cobra[i] = (cobra[i-1][0], cobra[i-1][1])

        cobra[0][0] += mov[0]*serpente.vel
        cobra[0][1] += mov[1]*serpente.vel



        tela.fill((0, 0, 0)) #preenche de preto
        
        show_score(score,tela)

        pygame.draw.rect(tela, comida.cor,(comida.x, comida.y, comida.comprimento, comida.largura))#Comida
        if cobra[0][0] == comida.x and cobra[0][1] == comida.y:
            comida.x = random.randrange(20,880, 10)
            comida.y = random.randrange(20,580, 10)
            cobra.append([cobra[-1][0] ,cobra[-1][1]])
            score += 10

        if cobra[0][0] >= 890 or cobra[0][0] < 10 or cobra[0][1] >= 590 or cobra[0][1] < 10: #checa colisões com as bordas
            cobra[0][0] = random.randrange(50,850,10)
            cobra[0][1] = random.randrange(50,550,10)
            for i in range(len(cobra)-1):
                cobra.pop()
            score = 0

        for i in range(len(cobra)):  #Desenhar a cobra com base no comprimento(número de tuplas)
            pygame.draw.rect(tela, serpente.cor, (cobra[i][0], cobra[i][1], serpente.comp, serpente.larg))

        pygame.draw.rect(tela, borda_cima.cor, (borda_cima.x, borda_cima.y, borda_cima.comprimento, borda_cima.largura)) #Bordas
        pygame.draw.rect(tela, borda_baixo.cor, (borda_baixo.x, borda_baixo.y, borda_baixo.comprimento, borda_baixo.largura))
        pygame.draw.rect(tela, borda_esquerda.cor, (borda_esquerda.x, borda_esquerda.y, borda_esquerda.comprimento, borda_esquerda.largura))
        pygame.draw.rect(tela, borda_direita.cor, (borda_direita.x, borda_direita.y, borda_direita.comprimento, borda_direita.largura))
        pygame.display.update()
    
    pygame.quit()
    sys.exit()

def menu():
    

    pygame.init()
    pygame.display.set_caption("Snake")
    tela = pygame.display.set_mode((900, 600))
    font2 = pygame.font.Font("freesansbold.ttf", 20)
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render('Snake, the Game', True, (255,255,255), (0,0,0)) 
    single = font2.render("Singleplayer",True,(200,0,200),(0,0,0))
    survive = font2.render("Survival mode",True,(0,200,200),(0,0,0))


    while True:
        pygame.mouse.set_visible(1)

        tela.blit(text,(340,40)) 
        
        tela.blit(single,(340,250))

        tela.blit(survive,(340,300))



        ("Snake main menu", font, (255, 255, 255), tela, 450, 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(340,465) and pos[1] in range(250,265):
                    singleplayer()
                elif pos[0] in range(340, 480) and pos[1] in range(300, 315):
                    survival()
        

        pygame.display.update()

menu()
