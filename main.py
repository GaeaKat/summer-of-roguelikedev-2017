import tdl
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

def main():
    console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Roguelike", fullscreen=False)
    console.draw_str(1, SCREEN_HEIGHT//2, 'Hi roguelikedev !')
    tdl.flush()
    tdl.event.keyWait()

if __name__ == "__main__":
    main()
