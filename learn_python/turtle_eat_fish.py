import turtle  # 官方Demo: python -m turtledemo.clock
from time import strftime
from random import randint, choice

GRID_WIDTH = 60
ROWS = 10
FONT = ('Meiryo', 20, 'normal')

# 设置turtle画板尺寸和窗口尺寸
turtle.screensize(GRID_WIDTH*10, GRID_WIDTH*10+90)  # get canvasSize: turtle.screensize()
turtle.setup(GRID_WIDTH*10+120, GRID_WIDTH*10+120)  # get windowSize: turtle.window_width()
turtle.title("Turtle Eat Fish Animation")

turtle.tracer(False)

# 设置turtle光标默认属性
turtle.speed('fast')
turtle.penup()
turtle.hideturtle()

# 用turtle.turtles()检验是否销毁了对象
def draw_grid():
    t_row = turtle.clone()
    turtle.tracer(False)
    # 将光标移动到画板的左上角
    t_row.setpos(-5*GRID_WIDTH, 5*GRID_WIDTH)
    t_row.pendown()
    t_col = t_row.clone()
    t_col.right(90)
    for i in range(ROWS):
        t_row.fd(GRID_WIDTH)
        t_clone = t_row.clone()
        t_clone.right(90)
        t_clone.fd(10*GRID_WIDTH)

        t_col.fd(GRID_WIDTH)
        t_clone = t_col.clone()
        t_clone.left(90)
        t_clone.fd(10*GRID_WIDTH)
    turtle.tracer(True)
    # 释放无用turtle对象内存
    del turtle.turtles()[1:]  # del c只会删除c本身


def init_time():
    t = turtle.clone()
    t.setpos(-5*GRID_WIDTH, -5*GRID_WIDTH-45)
    t.write("当前时间:  ", move=True, font=FONT)
    return t.pos()


def update_time():
    # 实现动态显示的三种方法：
    # 1. undo 2. 打印一段空格 3. clear(删除该对象所有笔迹)
    turtle.tracer(False)
    time_writer.clear()
    time_writer.write(strftime('%H:%M:%S'), font=FONT)
    turtle.tracer(True)
    turtle.ontimer(update_time, 1000)


class Fish:
    # static
    fish_template = turtle.clone()
    fish_template.showturtle()
    # 考虑鱼在格子中间，故边界应该是 [-270, 270]
    boundary = [-((ROWS/2)-0.5)*GRID_WIDTH, ((ROWS/2)-0.5)*GRID_WIDTH]

    def __init__(self):
        self.t = Fish.fish_template.clone()
        self.x = Fish.boundary[0] + GRID_WIDTH*randint(0, ROWS-1)
        self.y = Fish.boundary[0] + GRID_WIDTH*randint(0, ROWS-1)
        self.t.setpos(self.x, self.y)

    def move(self):
        choice_list = ['x + 1', 'x - 1', 'y + 1', 'y - 1']
        if self.x == Fish.boundary[1]: choice_list.remove('x + 1')
        if self.x == Fish.boundary[0]: choice_list.remove('x - 1')
        if self.y == Fish.boundary[1]: choice_list.remove('y + 1')
        if self.y == Fish.boundary[0]: choice_list.remove('y - 1')
        choose = choice(choice_list)
        if choose == 'x + 1':  self.x += GRID_WIDTH; self.t.setheading(0)
        if choose == 'x - 1':  self.x -= GRID_WIDTH; self.t.setheading(180)
        if choose == 'y + 1':  self.y += GRID_WIDTH; self.t.setheading(90)
        if choose == 'y - 1':  self.y -= GRID_WIDTH; self.t.setheading(-90)
        self.t.setpos(self.x, self.y)

def update_fish():
    turtle.tracer(True)
    for fish in fishs:
        fish.move()
    turtle.ontimer(update_fish, 500)


try:
    draw_grid()
    pos = init_time()  # 传坐标 防"当前时间"被clear
    # 清理上面函数产生的turtle对象
    del turtle.turtles()[1:]
    time_writer = turtle.clone()
    time_writer.setpos(pos)

    fishs = []
    for i in range(6):
        fishs.append(Fish())
    Fish.fish_template.hideturtle()

    # 定时更新部分 https://zhuanlan.zhihu.com/p/32094690
    # 用死循环不断调用定时器会一直占用线程
    # 而且经实验，若死循环内除定时器外还有别的代码
    # 会导致定时器的间隔interval变大，比如设好1秒更新的时间加入鱼游动的代码后2秒才变一次
    #
    # 另外一种方法，就是在回调函数中，创建定时器并启动，形成递归调用

    update_time()
    update_fish()

    turtle.done()  # 等同于mainloop()
except turtle.Terminator:
    pass
