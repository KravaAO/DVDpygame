from pygame import *

init()
font.init()

size = 1000, 600
window = display.set_mode(size)
clock = time.Clock()  # для фпс та затримки у грі

rect = Rect(500, 300, 70, 70)  # стоврення прямокутника x, y, ширина, висота
ramka = Rect(200, 100, 700, 350)


RED = (255, 0, 0)

ft = font.Font(None, 30)  # стоврення шрифта яким ми будемо писати
dvd = ft.render('DVD', True, (0, 0, 0))  # створення текста


def update():
    keys = key.get_pressed()  # отримати нажаті клавіши
    if keys[K_d]:
        rect.x += 5
    if keys[K_a]:
        rect.x -= 5

dx = 4
dy = 4
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    window.fill((255, 255, 255))

    draw.rect(window, RED, rect)  # малювання прямокутника
    window.blit(dvd, (rect.x + 12, rect.y + 26))

    draw.rect(window, (0, 0, 0), ramka, 10)

    rect.x += dx
    rect.y += dy

    if rect.x <= 200 or rect.x >= 830:
        dx *= -1
    if rect.y <= 100 or rect.y >= 450 - 70:
        dy *= -1


    display.update()
    clock.tick(60)
