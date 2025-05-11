# 机器下棋
import random
from In_package import *


class AI:
    def __init__(self, line_points, chessman):
        self._line_points = line_points
        self._my = chessman
        self._opponent = BLACK_CHESSMAN if chessman == WHITE_CHESSMAN else WHITE_CHESSMAN  # 对手的棋子
        self._checkerboard = [[0] * line_points for _ in range(line_points)]

    def randDrop(self):  # 随机落子
        x = random.randint(8, 10)
        y = random.randint(8, 10)
        point = Point(x, y)
        self._checkerboard[point.Y][point.X] = self._my.Value
        return point

    def get_opponent_drop(self, point):
        self._checkerboard[point.Y][point.X] = self._opponent.Value

    def AI_drop(self):
        point = None
        score = 0
        for i in range(self._line_points):
            for j in range(self._line_points):
                if self._checkerboard[j][i] == 0:
                    _score = self._get_point_score(Point(i, j))
                    if _score > score:
                        score = _score
                        point = Point(i, j)
                    elif _score == score and _score > 0:
                        r = random.randint(0, 100)
                        if r % 2 == 0:
                            point = Point(i, j)
        self._checkerboard[point.Y][point.X] = self._my.Value  # 标记位置
        return point

    def _get_point_score(self, point):
        score = 0
        for os in offset:
            score += self._get_direction_score(point, os[0], os[1])
        return score

    def _get_direction_score(self, point, x_offset, y_offset):
        count = 0  # 落子处我方连续子数
        _count = 0  # 落子处对方连续子数
        space = None  # 我方连续子中有无空格
        _space = None  # 对方连续子中有无空格
        both = 0  # 我方连续子两端有无阻挡
        _both = 0  # 对方连续子两端有无阻挡
        # 如果是 1 表示是边上是我方子 2 表示敌方子
        flag = self._get_stone_color(point, x_offset, y_offset, True)
        if flag != 0:
            for step in range(1, 6):
                x = point.X + step * x_offset
                y = point.Y + step * y_offset
                if 0 <= x < self._line_points and 0 <= y < self._line_points:
                    if flag == 1:
                        if self._checkerboard[y][x] == self._my.Value:
                            count += 1
                            if space is False:
                                space = True
                        elif self._checkerboard[y][x] == self._opponent.Value:
                            _both += 1
                            break
                        else:
                            if space is None:
                                space = False
                            else:
                                break  # 遇到第二个空格退出
                    elif flag == 2:
                        if self._checkerboard[y][x] == self._my.Value:
                            _both += 1
                            break
                        elif self._checkerboard[y][x] == self._opponent.Value:
                            _count += 1
                            if _space is False:
                                _space = True
                        else:
                            if _space is None:
                                _space = False
                            else:
                                break
                else:
                    # 遇到边也就是阻挡
                    if flag == 1:
                        both += 1
                    elif flag == 2:
                        _both += 1
        if space is False:
            space = None
        if _space is False:
            _space = None
        _flag = self._get_stone_color(point, -x_offset, -y_offset, True)
        if _flag != 0:
            for step in range(1, 6):
                x = point.X - step * x_offset
                y = point.Y - step * y_offset
                if 0 <= x < self._line_points and 0 <= y < self._line_points:
                    if _flag == 1:
                        if self._checkerboard[y][x] == self._my.Value:
                            count += 1
                            if space is False:
                                space = True
                        elif self._checkerboard[y][x] == self._opponent.Value:
                            _both += 1
                            break
                        else:
                            if space is None:
                                space = False
                            else:
                                break  # 遇到第二个空格退出
                    elif _flag == 2:
                        if self._checkerboard[y][x] == self._my.Value:
                            _both += 1
                            break
                        elif self._checkerboard[y][x] == self._opponent.Value:
                            _count += 1
                            if _space is False:
                                _space = True
                        else:
                            if _space is None:
                                _space = False
                            else:
                                break
                else:
                    # 遇到边也就是阻挡
                    if _flag == 1:
                        both += 1
                    elif _flag == 2:
                        _both += 1
        # 评估棋格获胜分数。
        # 使计算机计算获胜分值越高的棋格，就能确定能让自己的棋子最有可能达成联机的位置，也就是最佳进攻位置，
        # 而一旦计算机能确定自己的最高分值的位置，计算机就具备了进攻能力。
        # 同理，计算机能计算出玩家的最大分值位置，并抢先玩家获得该位置，这样计算机就具有了防御的能力。
        # 在计算机下棋之前，会计算空白棋格上的获胜分数，根据分数高低获取最佳位置。
        # 计算机会将棋子下在获胜分数最高的地方。
        # 当已放置4颗棋子时，必须在第五个空棋格上设置绝对高的分值。也就是10000
        # 当获胜组合上有部分位置已被对手的棋格占据而无法连成五子时，获胜组合上空棋格的获胜分数会直接设置为0。（四颗棋子，你把中间断了）
        # 当有两组及其以上的获胜组合位置交叉时，对该位置的分数进行叠加，形成分数比周围位置明显高。（五子棋中三三相连）
        score = 0
        if count == 4:
            score = 10000
        elif _count == 4:
            score = 9000
        elif count == 3:
            if both == 0:
                score = 1000
            elif both == 1:
                score = 100
            else:
                score = 0
        elif _count == 3:
            if _both == 0:
                score = 900
            elif _both == 1:
                score = 90
            else:
                score = 0
        elif count == 2:
            if both == 0:
                score = 100
            elif both == 1:
                score = 10
            else:
                score = 0
        elif _count == 2:
            if _both == 0:
                score = 90
            elif _both == 1:
                score = 9
            else:
                score = 0
        elif count == 1:
            score = 10
        elif _count == 1:
            score = 9
        else:
            score = 0
        if space or _space:
            score /= 2
        return score

    # 判断指定位置处在指定方向上是我方子、对方子、空
    def _get_stone_color(self, point, x_offset, y_offset, next):
        x = point.X + x_offset
        y = point.Y + y_offset
        if 0 <= x < self._line_points and 0 <= y < self._line_points:
            if self._checkerboard[y][x] == self._my.Value:
                return 1
            elif self._checkerboard[y][x] == self._opponent.Value:
                return 2
            else:
                if next:
                    return self._get_stone_color(Point(x, y), x_offset, y_offset, False)
                else:
                    return 0
        else:
            return 0
