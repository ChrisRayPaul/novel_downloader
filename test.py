from novel_grab.novel_grab import Downloader
import time
from threading import Thread
from multiprocessing import freeze_support


if __name__ == '__main__':
    # freeze_support()
    a = Downloader()
    a.set_url('http://book.zongheng.com/showchapter/603738.html')
    a.start()
    b = Downloader()
    b.set_url('http://book.zongheng.com/showchapter/635570.html')
    b.start()
# Thread(target=b.start).start()
# while True:
#     time.sleep(1)
#     print("a%d" % a.get_info()['percent'])
# print("b%d" % b.get_info()['percent'])
