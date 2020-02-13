# encoding=utf-8

import urllib2,os,re
import requests

from Crypto.Cipher import AES

def test_download():
    url = 'https://v22.51cto.com/2017/10/17/190719/3156/high/loco_video_497000_0.ts'
    filedata = urllib2.urlopen(url)
    datatowrite = filedata.read()
    
    with open('loco_video_497000_0_urllib2.ts', 'wb') as f:
        f.write(datatowrite)


    print('Beginning file download with requests')

    r = requests.get(url)

    with open("loco_video_497000_0_request.ts", 'wb') as f:
        f.write(r.content)

    # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)



# bytes_key = b"935ef3d7b319ceb7"
# for i in bytes_key:
#     print i
# with open("bi.key", 'wb') as f:
#     f.write(bytes_key)

def decode():
    key = b"935ef3d7b319ceb7"
    cryptor = AES.new(key, AES.MODE_ECB) #不需要iv
    base_dir = r"C:\Users\qxx\Desktop\test\22"
    # with open(base_dir+"\loco_video_497000_0.ts","rb") as source:
    bytearr = open(base_dir+"\loco_video_497000_1.ts","rb").read()
    n = len(bytearr) % 16
    if n != 0: 
        bytearr+= (16-n)*b"\x00"
    with open(os.path.join(base_dir,  "loco_video_497000_1-dec.ts"), 'wb') as f:
        f.write(cryptor.decrypt(bytearr))
    
def sort_by_pattern(n):
    pattern  = re.compile(r"_(\d*)\.ts")
    print n
    return pattern.search(n).group(1)

def merge(base_dir):
# 获取key
    os.chdir(base_dir)
    if  os.path.exists("key.key"):
        with open("key.key","r") as key_file:
            key = key_file.readline();
    else: 
        print "not exists key "+base_dir
        return
    cryptor = AES.new(key, AES.MODE_ECB) #不需要iv
    pattern  = re.compile(r"_(\d*)\.ts")
    for path,dir_list,file_list in os.walk(base_dir):  #qxx 罗列当前文件夹的路径,当前文件夹下文件夹名、当前文件夹下的文件名
        file_list = filter(pattern.search,file_list)
        file_list.sort(key=lambda a : int(pattern.search(a).group(1)))
        merge_name = os.path.basename(path)
        print merge_name
        if os.path.exists(merge_name):
            return
        for file_name in file_list:  
            if not file_name.endswith(".ts") : 
                continue
            bytearr = open(file_name,"rb").read()
            n = len(bytearr) % 16
            if n != 0: 
                bytearr+= (16-n)*b"\x00"
            with open(merge_name+"_merge.ts", 'ab') as f:
                f.write(cryptor.decrypt(bytearr[:len(bytearr)]))
# merge( ur"D:\workspace\python\51cto-download\51cto-video-download\学习\全栈网络安全专家\1.网络安全攻防实战课（陈鑫杰主讲）\1.网络安全入门导论".encode("gbk"))

def merge_all():
    base_dir = ur"D:\workspace\python\51cto-download\51cto-video-download\学习\全栈网络安全专家\1.网络安全攻防实战课（陈鑫杰主讲）".encode("gbk")
    for path,dir_list,file_list in os.walk(base_dir):
        for dir in dir_list:
            merge(os.path.join(path,dir))
    
merge_all()

# s ="497000_125.ts"
# pattern  = re.compile(r"_(\d*)\.ts")
# list = [1,2]
# list.sort(key=lambda a : int(pattern.search(a).group(1)))
# print pattern.search(s).group(1)

        