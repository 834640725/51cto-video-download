# encoding=utf-8


import requests
import sys,os
import re
from Crypto.Cipher import AES

import time
import threading
from Queue import Queue
from threading import Thread
from cto import tools


def download(base_dir):
    '''
    base_dir里必须有vedio.m3u8、key.key文件; 
    只下载base_dir当前文件夹; 
    '''
    # 获取key
    base_dir = base_dir if base_dir.endswith(os.sep) else base_dir+os.sep
    key_file = base_dir + "key.key"
    if  os.path.exists(key_file):
        with open(key_file,"r") as f:
            key = f.read();
    else: 
        print "not exists key "+base_dir
        return
    
    m3u8_file = base_dir+"vedio.m3u8";
    if  os.path.exists(m3u8_file):
        with open(m3u8_file,"r") as f:
            m3u8_content = f.read()
    else: 
        print "not exists m3u8_file "+base_dir
        return
    file_list = os.listdir(base_dir)
    file_list = filter(lambda n: n.endswith("ts"),file_list)
    if len(file_list)>0:
        print u"ts文件已存在 "+base_dir
        return
    lesson_name = os.path.basename(os.path.dirname(base_dir)) #base_dir以/结尾, 所以要去一次dirname
    ts_filename_downloading =  base_dir+lesson_name+".ts.downloading"   #下载中的完整路径     
    # 上层目录
    ts_filename = os.path.dirname(os.path.dirname(base_dir))+os.sep+lesson_name+".ts" #下载完成后的ts完整路径;
    # 移动视频到课程目录下: 把路径里的"m3u8"文件夹去掉; 
    if os.sep+"m3u8"+os.sep in ts_filename:
        ts_filename = ts_filename.replace(os.sep+"m3u8"+os.sep,os.sep)
    if os.path.exists(ts_filename):
        print u"ts文件已存在 "+base_dir
        return

    cryptor = AES.new(key, AES.MODE_ECB) #不需要iv
    urls = re.findall(r'https.*', m3u8_content)
    print "\r\n"+ts_filename_downloading,
    if os.path.exists(ts_filename_downloading):
        os.remove(ts_filename_downloading)  
    for url in urls: 
        print "-",
        res = requests.get(url)
        byte_arr = res.content
        n = len(byte_arr) % 16
        if n != 0: 
            byte_arr+= (16-n)*b"\x00"
        with open(ts_filename_downloading,"ab") as f:
            f.write(cryptor.decrypt(byte_arr))
    print "done"   
 
    tools.check_or_make_dir(os.path.dirname(ts_filename)) 
    os.rename(ts_filename_downloading,ts_filename)

def get_dir_list(base_dir):
    list = []
    for path,dir_list,file_list in os.walk(base_dir):
        # 文件名按照数字大小排序
        dir_list.sort(key=lambda n:n.split(".")[0].zfill(6))
        for dir in dir_list:
            list.append(os.path.join(path,dir))
    return list

def downlaod_all(base_dir,reverse = False):
    '''
    下载base_dir及子目录下的文件;
    '''
    dir_list = get_dir_list(base_dir)
    if reverse:
        dir_list.reverse()
    for dir in dir_list:
        download(dir)


def download_main():
    '''
    单线程下载的入口
    '''
    reverse = False
    arg1 = ""
    arg2 = ""
    if len(sys.argv)>=2:
        arg1 = sys.argv[1]
    if len(sys.argv)>=3:
        arg2 =  sys.argv[2]

    dir = ""
    reverse = False
    if arg1: 
        print "dir "+arg1
        dir = arg1
    if arg2 == "1":
        print "reverse true"
        reverse = True
    downlaod_all(dir.decode("gbk"), reverse)    

queue = Queue()

def download_multi():
    while True:
        dir = queue.get()
        print 'thread: %s, dir: %s' % (threading.current_thread(),dir)
        download(dir)
        queue.task_done()
        if queue.empty():
            break

def download_all_multi(base_dir,thread_count = 3):
    dir_list = get_dir_list(base_dir)
    for dir in dir_list:
        queue.put(dir)
    for i in range(thread_count):
        t = Thread(target=download_multi)
        t.daemon = True # 设置线程daemon  主线程退出，daemon线程也会推出，即时正在运行
        t.start()
    queue.join()

def download_main_multi():
    '''
    多线程下载的入口
    '''
    if len(sys.argv)>=2:
        dir = sys.argv[1]
    else:
        print "缺少dir参数"
        return
    download_all_multi(dir.decode("gbk"),3)   

if __name__ == "__main__": 
    # download_main()
    download_main_multi()





