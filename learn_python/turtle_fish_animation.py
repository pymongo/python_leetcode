"""
python -m turtledemo
python -m turtledemo.clock
"""
import turtle  # 官方Demo: python -m turtledemo.clock
from time import strftime
import random

GRID_WIDTH = 60
ROWS = 10
FONT = ('Meiryo', 20, 'normal')


# 用turtle.turtles()检验是否销毁了对象
def draw_grid():
    """
    turtle这个库在函数内创建的turtle实例不会被销毁，所以代码容易写的变量名到处飞
    """
    t_row = turtle.clone()
    turtle.tracer(False)
    # 将光标移动到画板的左上角
    t_row.setpos(-5 * GRID_WIDTH, 5 * GRID_WIDTH)
    t_row.pendown()
    t_col = t_row.clone()
    t_col.right(90)
    for _ in range(ROWS):
        t_row.fd(GRID_WIDTH)
        t_clone = t_row.clone()
        t_clone.right(90)
        t_clone.fd(10 * GRID_WIDTH)

        t_col.fd(GRID_WIDTH)
        t_clone = t_col.clone()
        t_clone.left(90)
        t_clone.fd(10 * GRID_WIDTH)
    turtle.tracer(True)
    # 释放无用turtle对象内存
    del turtle.turtles()[1:]  # del c只会删除c本身


def init_time():
    t = turtle.clone()
    t.setpos(-5 * GRID_WIDTH, -5 * GRID_WIDTH - 45)
    t.write("当前时间:  ", move=True)
    return t.pos()


# def update_time():
#     # 实现动态显示的三种方法：
#     # 1. undo 2. 打印一段空格 3. clear(删除该对象所有笔迹)
#     turtle.tracer(False)
#     time_writer.clear()
#     time_writer.write(strftime('%H:%M:%S'))
#     turtle.tracer(True)
#     turtle.ontimer(update_time, 1000)


class Fish:
    # 考虑鱼在格子中间，故边界应该是 [-270, 270]
    boundary = [-((ROWS / 2) - 0.5) * GRID_WIDTH, ((ROWS / 2) - 0.5) * GRID_WIDTH]
    DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
    HEADING = (0, 180, 90, -90)

    def __init__(self):
        self.t = turtle.Turtle()
        self.t.penup()  # 不显示鱼🐟的移动路径
        self.t.showturtle()
        # self.t.speed('fast')
        self.x = Fish.boundary[0] + GRID_WIDTH * random.randint(0, ROWS - 1)
        self.y = Fish.boundary[0] + GRID_WIDTH * random.randint(0, ROWS - 1)

        # 隐藏从原点移动到随机位置的动画
        turtle.tracer(False)
        self.t.setpos(self.x, self.y)
        turtle.tracer(True)

    def move(self):
        # 只要if/while的每个分支都定义了的变量名，就能在外部作用域使用，例如这里的direction
        # 虽然带来方便，但是我认为这是Python不好的地方
        while True:
            direction = random.randint(0, 3)
            dx, dy = Fish.DIRECTIONS[direction]
            next_x, next_y = self.x + dx * GRID_WIDTH, self.y + dy * GRID_WIDTH
            if Fish.boundary[0] <= next_x <= Fish.boundary[1] and Fish.boundary[0] <= next_y <= Fish.boundary[1]:
                self.x, self.y = next_x, next_y
                break
        self.t.setheading(Fish.HEADING[direction])
        self.t.setpos(self.x, self.y)


def run_turtle_timer_event():
    """
    FIXME fishes变量名居然在别的地方定义，这是Python不太好的一个特点
    """
    try:
        for fish in fishes:
            fish.move()
        turtle.ontimer(run_turtle_timer_event, 500)
    except turtle.Terminator as err:
        print(err)


def setup():
    turtle.setworldcoordinates(-400, -400, 400, 400)

    # 设置turtle画板尺寸和窗口尺寸
    turtle.getscreen().screensize(GRID_WIDTH * 10, GRID_WIDTH * 10 + 90)  # get canvasSize: turtle.screensize()
    turtle.getscreen().setup(GRID_WIDTH * 10 + 120, GRID_WIDTH * 10 + 120)  # get windowSize: turtle.window_width()

    # 设置turtle光标默认属性
    turtle.speed('fast')
    turtle.penup()
    turtle.hideturtle()


# def main():
#     setup()
#     run_turtle_timer_event()


if __name__ == '__main__':
    setup()

    draw_grid()
    # pos = init_time()  # 传坐标 防"当前时间"被clear
    # 清理上面函数产生的turtle对象
    del turtle.turtles()[1:]
    # time_writer = turtle.clone()
    # time_writer.setpos(pos)

    fishes = []
    for _ in range(6):
        fishes.append(Fish())

    # 定时更新部分 https://zhuanlan.zhihu.com/p/32094690
    # 用死循环不断调用定时器会一直占用线程
    # 而且经实验，若死循环内除定时器外还有别的代码
    # 会导致定时器的间隔interval变大，比如设好1秒更新的时间加入鱼游动的代码后2秒才变一次
    #
    # 另外一种方法，就是在回调函数中，创建定时器并启动，形成递归调用

    # update_time()
    run_turtle_timer_event()

    turtle.mainloop()
