# В cmd апгрейднуть pip и установить pygame
# python -m pip install --upgrade pip
# python -m pip install -U pygame --user

#-----------------------------------------
# Создаем игру и окно
import pygame #импортирование модуля pygame
pygame.init() #инициализация модуля
screen = pygame.display.set_mode((813,411)) #задание размера экрана
pygame.display.set_caption("Играйся со мной") #заголовок окна


#-----------------------------------------
# Определение объекта спрайта игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
    # Вызвать конструктор родительского класса (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/1 Woodcutter/Woodcutter_walk.png')
        self.rect = self.image.get_rect()
        self.rect.center = (50, 200)

    def update(self):
        self.rect.x += 5
        if self.rect.left > 813:
            self.rect.right = 0



##Класс создания анимаций
class Animation:
    # sprite это содержание кадры, time время каждого кадра
    def _init_(self, sprites = None, time = 100):
        self.sprites = sprites
        self.time = time
        #счетчик времени
        self.work_time = 0
        #СКОЛЬКО кадров нужно пропустить
        self.skip_frame = 0
        #номер кадр, который показываем
        self.flame = 0
        #функция получения времени с помощью комнады pygame.time.Clock()
    def update(self, dt):
        #прибовляем это время к счетчику, чтобы узнать сколько кадров нужно пропустить
        self.work_time +=dt
        #вычесляем сколько кадров нужно пролестнуть
        self.skip_frame = self.work_time/ self.time
        if self.skip_frame >0:
            self.work_time = self.work_time % self.time
            #прибавляем количество кадров, которе надо пролистнуть
            self.frame +=self.skip_frame
            #проверяем не больше ли текущих кадров, чем есть вообще
            if self.frame >=len(self.sprites):
                self.frame = 0
    def get_sprite(self):
        return self.sprites[self.frame]
##Загружаем изображение с раскадровкой
sprite = pygame.image.load('Sprites/1 Woodcutter/Woodcutter_walk.png').convert_alpha()
                    #вырезаем кадры"
#контейнер для кадров будущей анимаций
anim = []:
anim.append(sprite.subsurface((0,0,40,40)))
anim.append(sprite.subsurface((40,0,40,40)))
anim.append(sprite.subsurface((60,0,40,40)))
anim.append(sprite.subsurface((40,0,40,40)))
#создаём кадровую ленту
time=180
target = Animation(anim, time)
#-----------------------------------------
# загрузка спрайтов

walk = pygame.image.load('Sprites/1 Woodcutter/Woodcutter_walk.png')
jump = pygame.image.load('Sprites/1 Woodcutter/Woodcutter_jump.png')
bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('Sprites/1 Woodcutter/Woodcutter.png')

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
        screen.blit(walk, (x, y)) # отрисовка идущего
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
#        walk = True
    elif keys[pygame.K_RIGHT] and x < 813: # задание размера поля в котором движется объект
        x += speed
#        walk = True
    else:
        left =  False
        right = False
#        walk = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_UP] and y > 0 - height + 280: # задание размера поля в котором движется объект
            y -= speed
        if keys[pygame.K_DOWN] and y < 411: # задание размера поля в котором движется объект
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0: # чтобы падал с ускорением
                y += (jumpCount ** 2) / 8
            else: # чтобы прыгал с замедлением
                y -= (jumpCount ** 2) / 8
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow ()
    all_sprites.update()
    all_sprites.draw(screen)
pygame.quit()
