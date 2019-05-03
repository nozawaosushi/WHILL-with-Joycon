import whillpy
import whill_data
import pygame
from pygame.locals import *
import time

def main() :
    whill = whillpy.connect(port='/dev/tty.UC-232AC')
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print ('joystick start')

    pygame.init()

    x, y = 0, 0
    while True:
         # コントローラーの操作を取得
        eventlist = pygame.event.get()

        # イベント処理
        for e in eventlist:
            if e.type == QUIT:
                return

            if e.type == pygame.locals.JOYAXISMOTION:
                x, y = joystick0.get_axis(0), joystick0.get_axis(1)
                print ('axis x:' + str(x) + ' axis y:' + str(y))
            elif e.type == pygame.locals.JOYHATMOTION:
                x, y = joystick0.get_hat(0)
                print ('hat x:' + str(x) + ' hat y:' + str(y))
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                print ('button:' + str(e.button))

        #whill_data.Joy(int(x*50), int(-y*50))
        whill.move(straight=int(-x * 20), turn=int(y * 30))
        time.sleep(0.01)

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print ('joystickが見つかりませんでした。')
