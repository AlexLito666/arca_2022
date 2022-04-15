import pygame
pygame.init()
 
back = (200, 255, 255) #цвет фона (background)

mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()
 
 
#флаг окончания игры
game = True
#класс из предыдущего проекта
class Sprite():
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(filename)

    def fill(self):
        pygame.draw.rect(mw, back, self.rect)
    
    def draw(self):
       mw.blit(self.image, (self.rect.x, self.rect.y))
 
 
#создание мяча и платформы   
ball = Sprite('ball.png', 160, 200, 50, 50)
platform = Sprite('platform.png', 200, 300, 100, 30)
 
#создание врагов
start_x = 5 #координаты создания первого монстра
start_y = 5
count = 9 #количество монстров в верхнем ряду
monsters = [] #список для хранения объектов-монстров
for j in range(3): #цикл по столбцам
    y = start_y + (55 * j) #координата монстра в каждом след. столбце будет смещена на 55 пикселей по y
    x = start_x + (27.5 * j) #и 27.5 по x
    for i in range (count):#цикл по рядам (строкам) создаёт в строке количество монстров, равное count
        d = Sprite('enemy.png', x, y, 50, 50) #создаём монстра
        monsters.append(d) #добавляем в список
        x = x + 55 #увеличиваем координату следующего монстра
    count = count - 1  #для следующего ряда уменьшаем кол-во монстров


dy = 3
dx = 3
while game:
    ball.fill()
    platform.fill()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        platform.rect.x-=5
    if keys[pygame.K_RIGHT]:
        platform.rect.x+=5
    


    ball.rect.x += 3
    ball.rect.y -= 3

    #если мяч достигает границ экрана, меняем направление его движения
    if  ball.rect.y < 0:
        dy *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        dx *= -1

    #если мяч коснулся ракетки, меняем направление движения
    if ball.rect.colliderect(platform.rect):
        dy *= -1


    #отрисовываем всех монстров из списка
    for m in monsters:
        m.draw()
    
    platform.draw()
    ball.draw()
    
    pygame.display.update()
    
    clock.tick(40)
