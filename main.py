import tdl
from GameObject import GameObject
from Map import Map, Wall

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2
MAP_WIDTH = 80
MAP_HEIGHT = 45
map=Map(MAP_WIDTH,MAP_HEIGHT)


player = GameObject(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, '@', (255,255,255))
npc = GameObject(SCREEN_WIDTH//2 - 5, SCREEN_HEIGHT//2, '@', (255,255,0))


def handle_keys():
    global player, map

    user_input = tdl.event.key_wait()
    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle fullscreen
        tdl.set_fullscreen(not tdl.get_fullscreen())

    elif user_input.key == 'ESCAPE':
        return True  # exit game
    # movement keys
    if user_input.key == 'UP':
        map.moveobject((player.x,player.y),(player.x,player.y-1))

    elif user_input.key == 'DOWN':
        map.moveobject((player.x, player.y), (player.x, player.y + 1))

    elif user_input.key == 'LEFT':
        map.moveobject((player.x, player.y), (player.x-1, player.y ))

    elif user_input.key == 'RIGHT':
        map.moveobject((player.x, player.y), (player.x + 1, player.y))


def main():
    tdl.set_font('fonts\\arial10x10.png', greyscale=True, altLayout=True)
    root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)
    con = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    map.floor[30][22]=Wall()
    map.floor[50][22] = Wall()
    map.addobject(player)
    map.addobject(npc)
    map.sync()
    while not tdl.event.is_window_closed():
        map.render(con)
        root.blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)
        tdl.flush()

        # handle keys and exit game if needed
        exit_game = handle_keys()
        if exit_game:
            break


if __name__ == "__main__":
    main()
