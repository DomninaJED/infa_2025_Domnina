import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

def draw_fon(surface, color1, color2, y):
    '''
    Рисование фона по 2м цветам
    color1 - цвет неба
    color2 - цвет земли
    y - координата y границы разделения неба и земли
    '''
    pygame.draw.rect(surface, color1, (0,0, 600, y))
    pygame.draw.rect(surface, color2, (0, y, 600, 600 - y))

draw_fon(screen, (0,255,255), (0,255,0), 500)

def draw_man(surface, head_color, body_color, x, y, scale):

    '''
    Рисование мужчины
    head_color - цвет головы
    body_color - цвет тела
    x, y - точка начала рисования 
    Берутся от верхнего левого угла эллипса тела
    scale - масштабирование
    '''
    
    # Изначальные координаты/вводные
    body = (120, 200, 110, 260)
    head = (175, 165, 50)
    lines = [
        [(205, 230), (290, 350)],
        [(140, 230), (65, 350)],   
        [(190, 440), (215, 550)],  
        [(150, 445), (120, 550)],  
        [(120, 550), (80, 550)],   
        [(215, 550), (255, 550)]   
    ]
    
    # Масштабируем 
    scaled_body = (x, y, body[2] * scale, body[3] * scale)
    
    scaled_head = (
        x + (head[0] - body[0]) * scale,  
        y + (head[1] - body[1]) * scale,
    )
    radius = head[2] * scale
    
    scaled_lines = []
    for line in lines:
        scaled_line = [
            (x + (point[0] - body[0]) * scale, y + (point[1] - body[1]) * scale) for point in line
        ]
        scaled_lines.append(scaled_line)
    
    # Рисуем 
    pygame.draw.ellipse(surface, body_color, scaled_body)
    pygame.draw.circle(surface, head_color, scaled_head, radius)  
    
    for line in scaled_lines:
        pygame.draw.aaline(surface, (0, 0, 0), line[0], line[1], 1)



def draw_woman(surface, head_color, body_color, x, y, scale):
    
    '''
    Рисование женщины
    head_color - цвет головы
    body_color - цвет тела
    start_x, start_y - точка начала рисования 
    Берутся от верхней точки платья
    scale - масштабирование

    '''
    
    # Изначальные координаты/вводные
    body = [(350, 450), (530, 450), (448, 200)]  # треугольник платья
    head = (448, 168, 50)
    lines = [
        [(520, 265), (580, 225)],
        [(453, 230), (520, 265)],   
        [(453, 450), (453, 550)],  
        [(432, 230), (290, 350)],  
        [(425, 450), (425, 550)],  
        [(400, 550), (425, 550)],   
        [(480, 550), (453, 550)]   
    ]
    
    # Масштабируем 
    scaled_body = [
        (x + (point[0] - body[2][0]) * scale, y + (point[1] - body[2][1]) * scale) for point in body
    ]
    
    scaled_head = (
        x + (head[0] - body[2][0]) * scale,  
        y + (head[1] - body[2][1]) * scale,
    )
    radius = head[2] * scale
    
    scaled_lines = []
    for line in lines:
        scaled_line = [
            (x + (point[0] - body[2][0]) * scale, y + (point[1] - body[2][1]) * scale) for point in line
        ]
        scaled_lines.append(scaled_line)
    
    # Рисуем 
    pygame.draw.polygon(surface, body_color, scaled_body)  # платье-треугольник
    pygame.draw.circle(surface, head_color, scaled_head, radius)  
    
    for line in scaled_lines:
        pygame.draw.aaline(surface, (0, 0, 0), line[0], line[1], 1)


def draw_icecream(surface, color1, color2, color3, color4, x, y, scale):
    '''
    Рисование мороженого
    color1 - цвет рожка
    color2, color3, color4 - цвета шариков
    x, y - точка начала рисования 
    Берутся от первого шарика
    scale - масштабирование
    '''
    
    # Изначальные координаты/вводные
    rog = [(65, 350), (85, 285), (15, 300)]  # треугольник рожка
    circles = [
        (33, 285, 18),  
        (65, 280, 18),  
        (48, 265, 18)   
    ]
    
    # Масштабируем
    scaled_rog = [
        (x + (point[0] - rog[1][0]) * scale, y + (point[1] - rog[1][1]) * scale) for point in rog
    ]
    
    scaled_circles = []
    for circle in circles:
        scaled_circle = (
            x + (circle[0] - rog[1][0]) * scale,  
            y + (circle[1] - rog[1][1]) * scale,
            circle[2] * scale
        )
        scaled_circles.append(scaled_circle)
    


    # Рисуем 
    pygame.draw.polygon(surface, color1, scaled_rog)  # рожок

    pygame.draw.circle(surface, color2, (scaled_circles[0][0], scaled_circles[0][1]), scaled_circles[0][2])  
    pygame.draw.circle(surface, color3, (scaled_circles[1][0], scaled_circles[1][1]), scaled_circles[1][2])  
    pygame.draw.circle(surface, color4, (scaled_circles[2][0], scaled_circles[2][1]), scaled_circles[2][2])



draw_woman(screen, (192,192,192), (255,0,255), 130, 150, 1.2)
draw_man(screen, (192,192,192), (125,125,125), 137, 178, 0.7)  
draw_icecream(screen, (225,225,0), (128,128,0), (255,0,0), (255,255,255), 300, 300, 2)



pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

