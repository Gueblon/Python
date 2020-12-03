# В cmd апгрейднуть pip и установить pygame
# python -m pip install --upgrade pip
# python -m pip install -U pygame --user

#-----------------------------------------
# Создаем игру и окно
import pygame #импортирование модуля pygame
pygame.init() #инициализация модуля
screen = pygame.display.set_mode((813,411)) #задание размера окна
# нужно ли задавать Surface?
pygame.display.set_caption("Играйся со мной") #заголовок окна

#-----------------------------------------
# Класс создания анимации.
class Animation:
    def __init__(self, sprites = None, time = 100):
        self.sprites = sprites
        self.time = time # время жизни каждого кадра
        self.work_time = 0 # счетчик времени
        self.skip_frame = 0 # сколько кадров нужно пропустить
        self.frame = 0 # номер показываемого кадра
    def update(self, dt): #функция получения времени с помощью комнады pygame.time.Clock()
        self.work_time += dt # прибовляем это время к счетчику, чтобы узнать сколько кадров нужно пропустить
        self.skip_frame = self.work_time // self.time # вычисляем сколько кадров нужно пропустить
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time # чтобы не потерять милисекунды сохраняем остаток от деления
            self.frame += self.skip_frame # прибавляем количество кадров, которые надо пропустить
            if self.frame >= len(self.sprites): # сверяем число текущих кадров
                self.frame = 0
    def get_sprite(self):
        return self.sprites[self.frame]
time = 180
#Загружаем изображения с раскадровкой
walk = pygame.image.load('Sprites/1 Woodcutter/Woodcutter_walk.png').convert_alpha()
jump = pygame.image.load('Sprites/1 Woodcutter/Woodcutter_jump.png').convert_alpha()
anim = [] # контейнер для нарезки кадров
anim.append(walk.subsurface((0,0,48,48)))
anim.append(walk.subsurface((48,0,48,48)))
anim.append(walk.subsurface((96,0,48,48)))
anim.append(walk.subsurface((144,0,48,48)))
anim.append(walk.subsurface((192,0,48,48)))
anim.append(walk.subsurface((240,0,48,48)))
anim2 = []
anim2.append(jump.subsurface((0,0,48,48)))
anim2.append(jump.subsurface((48,0,48,48)))
anim2.append(jump.subsurface((96,0,48,48)))
anim2.append(jump.subsurface((144,0,48,48)))
anim2.append(jump.subsurface((192,0,48,48)))
anim2.append(jump.subsurface((240,0,48,48)))
#создаём кадровую ленту
Woodcutter_walk = Animation (anim, time)
Woodcutter_jump = Animation (anim2, time)
clock = pygame.time.Clock() # это должно вызвать тик
dt = 0
bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('Sprites/1 Woodcutter/Woodcutter.png')

#-----------------------------------------
# определяем переменные
x = 50 # координаты начального положения игрока
y = 250 # координаты начального положения игрока
width = 48 # ширина спрайта
height = 48 # высота спрайта
speed = 5
isJump = False
jumpCount = 10
left = False
right = False
animCount = 0
walk = False

def drawWindow ():
    global animCount
    screen.blit(bg, (0, 0)) # заполнение экрана фоном
    if animCount +1 >= 30:
        animCount = 0
    if walk:
        Woodcutter_walk.update(dt)
        screen.blit(Woodcutter_walk.get_sprite(), (x, y)) # отрисовка идущего
        pygame.display.flip()
        animCount += 1
    elif isJump:
        Woodcutter_jump.update(dt)
        screen.blit(Woodcutter_jump.get_sprite(), (x, y)) # отрисовка прыгающего
        pygame.display.flip()
        animCount += 1
    else:
        screen.blit(playerStand, (x, y)) # отрисовка стоящего

    pygame.display.update()

#-----------------------------------------
# в игре должен быть один основной цикл, чтобы игра не закрывалось
running = True
while running:
    pygame.time.delay(50) # количество милисекунд через которые повторяется данный цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed() # нажатие клавиш
    if keys[pygame.K_LEFT] and x > 0 - width: # задание размера поля в котором движется объект
        x -= speed
        walk = True
    elif keys[pygame.K_RIGHT] and x < 813: # задание размера поля в котором движется объект
        x += speed
        walk = True
    else:
        left =  False
        right = False
        walk = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_UP] and y > 0 - height + 280: # задание размера поля в котором движется объект
            y -= speed
            walk = True
        if keys[pygame.K_DOWN] and y < 411: # задание размера поля в котором движется объект
            y += speed
            walk = True
        if keys[pygame.K_SPACE]:
            isJump = True
            walk = False
    else:
        if jumpCount >= -10:
            if jumpCount < 0: # чтобы падал с ускорением
                y += (jumpCount ** 2) // 10
            else: # чтобы прыгал с замедлением
                y -= (jumpCount ** 2) // 10
            jumpCount -= 1
            walk = False
        else:
            isJump = False
            jumpCount = 10
    drawWindow ()
    dt = clock.tick(40) # частота не более чем указано кадров в секунду
pygame.quit()
