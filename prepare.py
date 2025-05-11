#准备工作
from In_package import *
import pygame.gfxdraw

class Prepare:
    def __init__(self):
        pass
    # 画棋盘
    def draw_checkerboard(self,screen):
        screen.fill(Checkerboard_Color)  # 填充棋盘背景色
        # 画棋盘网格线外的边框
        pygame.draw.rect(screen, BLACK_COLOR, (Outer_Width, Outer_Width, Border_Length, Border_Length), Border_Width)
        for i in range(19):  # 画网格线
            pygame.draw.line(screen, BLACK_COLOR, (26, 26 + 30 * i), (26 + 30 * 18, 26 + 30 * i), 1)
        for j in range(19):
            pygame.draw.line(screen, BLACK_COLOR, (26 + 30 * j, 26), (26 + 30 * j, 26 + 30 * 18), 1)
        for i in (3, 9, 15):  # 画星位和天元
            for j in (3, 9, 15):
                if i == j == 9:
                    radius = 5
                else:
                    radius = 3  # i,j逻辑上的横纵坐标
                pygame.gfxdraw.aacircle(screen, 26 + 30 * i, 26 + 30 * j, radius, BLACK_COLOR)
                pygame.gfxdraw.filled_circle(screen, 26 + 30 * i, 26 + 30 * j, radius, BLACK_COLOR)

    # 画棋子  #这个只是放在提示栏旁边的棋子
    def draw_chessman_pos(self,screen, pos, stone_color):
        pygame.gfxdraw.aacircle(screen, pos[0], pos[1], Stone_Radius2, stone_color)
        pygame.gfxdraw.filled_circle(screen, pos[0], pos[1], Stone_Radius2, stone_color)

    # 画棋盘上已有的棋子  #游戏中画的棋子
    def _draw_chessman(self,screen, point, stone_color, flag):
        pygame.gfxdraw.aacircle(screen, 26 + 30 * point.X, 26 + 30 * point.Y, Stone_Radius, stone_color)
        pygame.gfxdraw.filled_circle(screen, 26 + 30 * point.X, 26 + 30 * point.Y, Stone_Radius, stone_color)
        if flag:  # 标记当前最新新棋子就行，就不用管是黑棋还是白棋
            screen.blit(image, [16 + 30 * point.X, 10 + 30 * point.Y])

    def draw_all(self,checkerboard, AI_x, AI_y):  # 每次都要重新画一次
        for i, row in enumerate(checkerboard.checkerboard):  # 画棋盘上已有的棋子  因为下一次刷新一次，
            for j, cell in enumerate(row):
                if cell == BLACK_CHESSMAN.Value:
                    if j == AI_x and i == AI_y:  # 增加标记位
                        flag = 1
                    else:
                        flag = 0

                    self._draw_chessman(screen, Point(j, i), BLACK_CHESSMAN.Color, flag)
                elif cell == WHITE_CHESSMAN.Value:
                    if j == AI_x and i == AI_y:  # 增加标记位
                        flag = 1
                    else:
                        flag = 0
                    self._draw_chessman(screen, Point(j, i), WHITE_CHESSMAN.Color, flag)

    # 文本信息提示

    def print_text(self,screen, font, x, y, text, fcolor=(255, 255, 255)):
        imgText = font.render(text, True, fcolor)
        screen.blit(imgText, (x, y))

    def draw_left_info_begin(self,screen, font):  # 右侧信息提示
        self.print_text(screen, font, 324, 170, '五子棋', BLUE_COLOR)
        self.print_text(screen, font, 310, 270, '人人对战', BLUE_COLOR)
        self.print_text(screen, font, 310, 370, '人机对战', BLUE_COLOR)

    def draw_left_info_every(self,screen, font):  # 人人对战
        self.print_text(screen, font, 610, 50, '当前状态', BLUE_COLOR)
        # print_text(screen, font, 630, 270, '悔棋', BLUE_COLOR)
        self.print_text(screen, font, 610, 333, '重新开始', BLUE_COLOR)
        self.print_text(screen, font, 600, 400, '回到主界面', BLUE_COLOR)

    def draw_left_info_computer(self,screen, font, first):  # 人机对战 #左边文字显示
        self.draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, Start_X + Stone_Radius2), WHITE_CHESSMAN.Color)
        self.draw_chessman_pos(screen, (SCREEN_HEIGHT + Stone_Radius2, Start_X + Stone_Radius2 * 4), BLACK_CHESSMAN.Color)
        if first == "me":  # 没有选棋，默认白棋先下
            self.print_text(screen, font, 638, 29, '电脑', BLUE_COLOR)
            self.print_text(screen, font, 638, 83, '玩家', BLUE_COLOR)
        else:
            self.print_text(screen, font, 638, 29, '玩家', BLUE_COLOR)
            self.print_text(screen, font, 638, 83, '电脑', BLUE_COLOR)
        self.print_text(screen, font, 610, 333, '重新开始', BLUE_COLOR)
        self.print_text(screen, font, 600, 400, '回到主界面', BLUE_COLOR)  ##r


    # 根据鼠标点击位置，返回游戏区坐标 物理->逻辑
    def get_clickpoint(self,click_pos):
        pos_x = click_pos[0] - Start_X
        pos_y = click_pos[1] - Start_Y
        if pos_x < -Inside_Width or pos_y < -Inside_Width:
            return None
        x = pos_x // SIZE
        y = pos_y // SIZE
        if pos_x % SIZE > Stone_Radius:
            x += 1
        if pos_y % SIZE > Stone_Radius:
            y += 1
        if x >= Line_Points or y >= Line_Points:
            return None
        return Point(x, y)

    # 提示当前是谁下棋 ，人人对战时需要
    def remind_chess(self,cur_runner):

        if cur_runner == BLACK_CHESSMAN:
            pygame.draw.rect(screen, Checkerboard_Color, [630, 100, 150, 50])  # 先把上一次的类容用一个矩形覆盖
            # print_text(screen, font1, 630, 100, '黑子', BLUE_COLOR)
            self.draw_chessman_pos(screen, (660, 140), BLACK_CHESSMAN.Color)
        else:
            pygame.draw.rect(screen, Checkerboard_Color, [630, 100, 150, 50])
            # print_text(screen, font1, 630, 100, '白子', BLUE_COLOR)
            self.draw_chessman_pos(screen, (660, 140), WHITE_CHESSMAN.Color)

    # 黑白棋轮流下
    def get_next(self,cur_runner):
        if cur_runner == BLACK_CHESSMAN:
            return WHITE_CHESSMAN
        else:
            return BLACK_CHESSMAN
