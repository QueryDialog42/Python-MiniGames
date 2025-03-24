import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        now = time.localtime()
        nowtime = time.strftime("%Y/%m/%d %H:%M:%S", now)
        print(nowtime, " " * (20 - len(nowtime)), f" {event.src_path} is created")

    def on_opened(self, event):
        now = time.localtime()
        nowtime = time.strftime("%Y/%m/%d %H:%M:%S", now)
        print(nowtime, " " * (20 - len(nowtime)), f" {event.src_path} is opened")
    
    def on_modified(self, event):
        now = time.localtime()
        nowtime = time.strftime("%Y/%m/%d %H:%M:%S", now)
        print(nowtime + " " * (20 - len(nowtime)), f"{event.src_path} is modified")

    def on_closed(self, event):
        now = time.localtime()
        nowtime = time.strftime("%Y/%m/%d %H:%M:%S", now)
        print(nowtime + " " * (20 - len(nowtime)), f"{event.src_path} is closed")
    
    def on_deleted(self, event):
        now = time.localtime()
        nowtime = time.strftime("%Y/%m/%d %H:%M:%S", now)
        print(nowtime + " " * (20 - len(nowtime)), f" {event.src_path} is deleted")
    
    def on_moved(self, event):
        now = time.localtime()
        nowtime = time.strftime("%Y/%m/%d %H:%M:%S", now)
        print(nowtime + " " * (20 - len(nowtime)), f" {event.src_path} is moved")

observer = Observer()
event_handler = MyHandler()
observer.schedule(event_handler, path="C:/Users/batug/OneDrive/Masaüstü/WatchdogFile", recursive=True)

observer.start()
try:
    while True:
        time.sleep(300)
except KeyboardInterrupt:
    observer.stop()
observer.join()