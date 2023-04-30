cnt = 0
rageFlag = False
rageThreshold = 4
rageDuration = 4


def rage(testnpc):
    global cnt
    cnt += 1
    if cnt >= rageThreshold:
        testnpc.npc.say("Raging!!!")
    if cnt >= rageThreshold + rageDuration:
        testnpc.npc.say("Stop raging")
        cnt = 0

def tick(testnpc):
    global cnt, rageFlag
    testnpc.npc.say(str(cnt))
    if rageFlag == 1:
        rage(testnpc)


def target(testnpc):
    global cnt, rageFlag
    cnt = 0
    testnpc.npc.say("FAQ!")
    rageFlag = True


def targetLost(testnpc):
    global rageFlag
    testnpc.npc.say("Lost")
    rageFlag = False

