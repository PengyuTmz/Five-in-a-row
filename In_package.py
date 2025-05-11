from collections import namedtuple
import pygame
# 画棋盘
SIZE = 30  # 棋盘每个点时间的间隔
Line_Points = 19  # 棋盘每行/每列点数
Outer_Width = 20  # 棋盘外宽度
Border_Width = 4  # 边框宽度
Inside_Width = 4  # 边框跟实际的棋盘之间的间隔
Border_Length = SIZE * (Line_Points - 1) + Inside_Width * 2 + Border_Width  # 边框线的长度
Start_X = Start_Y = Outer_Width + int(Border_Width / 2) + Inside_Width  # 网格线起点（左上角）坐标
SCREEN_HEIGHT = SIZE * (Line_Points - 1) + Outer_Width * 2 + Border_Width + Inside_Width * 2  # 游戏屏幕的高
SCREEN_WIDTH = SCREEN_HEIGHT + 200  # 游戏屏幕的宽
Stone_Radius = SIZE // 2 - 3  # 棋子半径 12
Stone_Radius2 = SIZE // 2 + 3 # 18 放提示栏
Checkerboard_Color = (247, 230, 208)  # 棋盘颜色，RGB值
BLACK_COLOR = (0, 0, 0)   #黑棋颜色
WHITE_COLOR = (255, 255, 255)   #白棋颜色
RED_COLOR = (200, 30, 30)
BLUE_COLOR = (30, 30, 200)
RED = (255, 0, 0)
RIGHT_INFO_POS_X = SCREEN_HEIGHT + Stone_Radius2 * 2 + 10
Chessman = namedtuple('Chessman', 'Name Value Color')
Point = namedtuple('Point', 'X Y')
BLACK_CHESSMAN = Chessman('黑子', 1, (45, 45, 45))
WHITE_CHESSMAN = Chessman('白子', 2, (219, 219, 219))
offset = [(1, 0), (0, 1), (1, 1), (1, -1)] # - | / \
pygame.init()
# 加载标记位图片
image = pygame.image.load("timg.png")
font1 = pygame.font.SysFont('SimHei', 32)  # 字体：黑体，32号
font2 = pygame.font.SysFont('SimHei', 72)  # 字体：黑体，72号
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 游戏屏幕的高，宽

# print(SCREEN_WIDTH, SCREEN_HEIGHT)