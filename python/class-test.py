# 定义测试npc
test = None


# hook必须暴露在外，曲折实现封装
def init(c):
    global test
    # 实例化
    test = Entity(c)

def interact(c):
    global test
    test.interact()

def timer(c):
    global test
    # print(dir(c))
    # 将触发timerEvent的timerId传给test
    test.timer(c.id)

def target(c):
    global test
    test.target()

def targetLost(c):
    global test
    test.targetLost()


class Entity:
    # 定义Timer
    Timer = None
    # 将自己定义的timer封装成字典
    timers = {}
    # 封装的customnpc接口
    c = None

    def __init__(self, c):
        self.c = c
        self.c.npc.say("Initialized!")
        self.timer_init()

    def interact(self):
        self.c.npc.say("FAQ!")

    def timer(self, timer_id):
        if timer_id == self.timers['timer1'][0]:
            self.c.npc.say("Raging!")
            self.Timer.start(*self.timers['timer2'])
            # do something

        if timer_id == self.timers['timer2'][0]:
            self.c.npc.say("Stop raging")
            self.Timer.start(*self.timers['timer1'])
            # do something

    def target(self):
        self.Timer.start(*self.timers['timer1'])

    def targetLost(self):
        self.Timer.clear()

    def timer_init(self):
        # 获取接口的Timer
        self.Timer = self.c.npc.getTimers()
        # 封装为字典，第一个参数为timerId，第二个为持续时间，第三个为是否循环
        self.timers['timer1'] = [1, 48, False]
        self.timers['timer2'] = [2, 48, False]

    # 调试函数
    def show(self):
        print(dir(self.c.npc))

    def timer_test(self):
        self.c.npc.say('timer test')
        self.Timer.start(*self.timers['timer1'])

