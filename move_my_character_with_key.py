from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('sonic.png')


def handle_events():
    global running, dir_x, dir_y, motion, x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                dir_y += 1
                motion = 2
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                motion = 3
            elif event.key == SDLK_RIGHT:
                dir_x += 1
                motion = 2
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                motion = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x = 0
                motion = 1
            elif event.key == SDLK_LEFT:
                dir_x = 0
                motion = 4
            elif event.key == SDLK_UP:
                dir_y = 0
                motion = 1
            elif event.key == SDLK_DOWN:
                dir_y = 0
                motion = 4


running = True
dir_x = 0
dir_y = 0
x = 800 // 2
y = 600/2
frame = 0
motion = 1

while running:
    clear_canvas()
    background.draw(400, 300)
    if (motion == 1):
        character.clip_draw(0 + (frame * 32), 90, 32, 45, x, y, 100, 100)
    elif (motion == 2):
        character.clip_draw(0 + (frame * 42), 0, 42, 45, x, y, 100, 100)
    elif (motion == 3):
        character.clip_composite_draw(0 + (frame * 42), 0, 42, 45, 0, 'h', x, y, 100, 100)
    elif (motion == 4):
        character.clip_composite_draw(0 + (frame * 32), 90, 32, 45, 0, 'h',x, y, 100, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if(dir_x > 0):
        if(x > 800):
            dir_x = 0
    if (dir_x < 0):
        if (x < 0):
            dir_x = 0
    if (dir_y > 0):
        if (y > 600):
            dir_y = 0
    if (dir_y < 0):
        if (y < 0):
            dir_y = 0
    x += dir_x * 10
    y += dir_y * 10
    delay(0.1)

close_canvas()

