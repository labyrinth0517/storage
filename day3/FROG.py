# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
print("一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？")
print("尝试解决问题：")
FROG = -20
Day = 1
while FROG < 0:
    FROG = FROG + 3
    Day = Day + 1
    # print("白天爬上去：", FROG)
    if FROG >= 0:
        print("出来了:)")
        break
    FROG = FROG - 2
    # print("晚上下滑：", FROG)
print("小青蛙，第", Day, "天白天可以出来")
