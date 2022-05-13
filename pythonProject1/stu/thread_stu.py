import threading
import urllib
import json
import time
from urllib.request import urlopen

# def timeit(f):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = f(*args, **kwargs)
#         end_time = time.time()
#         print("%s函数运行时间:%.2f" % (f.__name__, end_time - start_time))
#         return res
#
#     return wrapper
#
#
# class MyThread(threading.Thread):
#     def __init__(self, ip):
#         super(MyThread, self).__init__()
#         self.ip = ip
#
#     def run(self):
#         url = "http://ip-api.com/json/%s" % self.ip
#         urlObj = urlopen(url)
#         pageContent = urlObj.read().decode('utf-8')
#         dict_data = json.loads(pageContent)
#
#         print('''
#                     %s
#         city: %s
#         country:%s
#         ''' % (self.ip, dict_data['city'], dict_data['country']))
#
#
# def getIp(ip):
#     url = "http://ip-api.com/json/%s" % ip
#     urlObj = urlopen(url)
#     pageContent = urlObj.read().decode('utf-8')
#     dict_data = json.loads(pageContent)
#
#     print('''
#                %s
#     city: %s
#     country:%s
#     ''' % (ip, dict_data['city'], dict_data['country']))
#
#
# @timeit
# def main1():
#     ips = ['12.13.14.%s' % (i + 1) for i in range(10)]
#     for ip in ips:
#         getIp(ip)
#
#
# @timeit
# def main():
#     ips = ['12.13.14.%s' % (i + 1) for i in range(10)]
#     threads = []
#
#     for ip in ips:
#         t = MyThread(ip)
#         threads.append(t)
#         t.start()
#
#     [thread.join() for thread in threads]
#
#
# if __name__ == '__main__':
#     main()
#     main1()
#
#
# # 普通创建线程
#
# def run(n):
#     print('task', n)
#     time.sleep(1)
#     print('2s')
#     time.sleep(1)
#     print('1s')
#     time.sleep(1)
#     print('0s')
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run, args=('t1',))
#     t2 = threading.Thread(target=run, args=('t2',))
#     t2.setDaemon(True)
#     # t1.setDaemon(True)
#     t1.start()
#     t2.start()
#
#     print("end")

event = threading.Event()


def lighter():
    count = 0
    event.set()  # 初始者为绿灯
    while True:
        if 5 < count <= 10:
            event.clear()  # 红灯，清除标志位
            print("\33[41;lmred light is on...\033[0m]")
        elif count > 10:
            event.set()  # 绿灯，设置标志位
            count = 0
        else:
            print('\33[42;lmgreen light is on...\033[0m')

        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():  # 判断是否设置了标志位
            print('[%s] running.....' % name)
            time.sleep(1)
        else:
            print('[%s] sees red light,waiting...' % name)
            event.wait()
            print('[%s] green light is on,start going...' % name)


startTime = time.time()
light = threading.Thread(target=lighter, )
light.start()

car = threading.Thread(target=car, args=('MINT',))
car.start()
endTime = time.time()
print('用时：', endTime - startTime)


def run(n, semaphore):
    semaphore.acquire()
    time.sleep(3)
    print('run the thread:%s\n' % n)
    semaphore.release()


if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5)
    for i in range(23):
        t = threading.Thread(target=run, args=('Thread-%s' % i, semaphore))
        t.start()

    while threading.activeCount() != 1:
        pass
    else:
        print("done")


