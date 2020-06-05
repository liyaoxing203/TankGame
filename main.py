import pygame,sys
from util.local import *
from pygame.locals import *

def start():
    pygame.init()

    #显示窗口
    window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))


    pygame.display.set_caption('坦克大战')
    iconImage=pygame.image.load('./img/camp.gif')
    
    while True:
        window.blit

        #处理事件
        eventList = pygame.event.get()

        for event in eventList:
            if event.type == QUIT:
                # 退出界面
                pygame.quit()
                # python 程序退出
                sys.exit()




if __name__ == '__main__':
    start()