# encoding=utf-8

import urllib2,os,re
import requests
import unicodedata
import sys

from Crypto.Cipher import AES
from cto import Login
from cto import lesson



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

def decode_test():
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
    '''
    ts文件机已经下载; 机密、合并; 
    '''
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
    for path,dir_list,file_list in os.walk(base_dir):  #qxx os.walk包括子文件夹; 返回: 当前文件夹的路径,当前文件夹下文件夹名、当前文件夹下的文件名
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
    
# merge_all()

def re_test():
    s ="497000_125.ts"
    pattern  = re.compile(r"_(\d*)\.ts")
    list = [1,2]
    list.sort(key=lambda a : int(pattern.search(a).group(1)))
    print pattern.search(s).group(1)
def re_test2():
    source = '#EXT-X-KEY:METHOD=AES-128,URI="/center/player/play/get-key?lesson_id=55295&id=40948&type=course&lesson_type=course&isPreview=0",IV=0x0123456789abcdef0123456789abcdef'
    uri = re.search(r'URI="(.+)",IV',source).group(1)
    print uri
# re_test2()

def dict_test():
    d = {"a":1,"b":"bb"}
    print "has_key",d.has_key("a")
    print "get ",d.get("11")
    print os.path.join("D:/","","11")
    for key in d: 
        print key,d[key]

# dict_test();        

def mkdir_test():
    '''
Exception has occurred: WindowsError
[Error 123] : u'D:\\workspace\\python\\51cto-download\\51cto-video-download\\\u5b66\u4e60/\u5168\u6808\u7f51\u7edc\u5b89\u5168\u4e13\u5bb6\\7.\u3010\u5fae\u804c\u4f4d\u3011\u4e03\u3001&&\u9632\u5fa1\u4e0e\u5b89\u5168\u5ba1\u8ba1\\2. \u5b89\u5168\u5ba1\u8ba1\uff08\u6d41\u91cf\u63a7\u5236\uff09\u539f\u7406\u4e0e\u5b9e\u8df5\\2-1.Panabit\u6d41\u91cf\u63a7\u5236\x08\u539f\u7406\uff08\u9762\u6388\uff09'
    '''
    # os.mkdir(u"2. \u5b89\u5168\u5ba1\u8ba1\uff08\u6d41\u91cf\u63a7\u5236\uff09\u539f\u7406\u4e0e\u5b9e\u8df5")
    value = u"2-1.Panabit\u6d41\u91cf\u63a7\u5236\x08\u539f\u7406\uff08\u9762\u6388\uff09"
    # value = unicodedata.normalize('NFKD', name).encode('utf8', 'ignore')
    # os.mkdir(value)
    value = unicode(re.sub(ur'[\x08]', '', value))
    # value = unicode(re.sub('[-\s]+', '-', value))
    os.mkdir(value)

    print value
# mkdir_test()

def listdir_test():
    list =os.listdir("*.py")
    print list

# listdir_test()    

def  sys_arg_test():
    print sys.argv
# sys_arg_test()    

def os_path_test():
    print( os.path.basename('/base/root/runoob.txt') )   # 返回文件名
    print( os.path.dirname('/base/root/runoob.txt') )    # 返回目录路径
    print( os.path.split('/base/root/runoob.txt') )      # 分割文件名与路径
    print( os.path.join('root','test','runoob.txt') )  # 将目录和文件名合成一个路径

def byte_string_test():
    a = b"\x69\x6a\x6b" 
    b = "ijk".encode("ascii")
    c = b"i\x6ak"
    d = "ijk"
    e = "ijk".encode("gbk") #因为各种编码类型对字母的编码和ascii是一致的
    f = "ijk".encode("utf8")
    g = "i\x6ak"
    assert a == b
    assert a == c
    assert a == d
    assert a == e
    assert a == f
    assert a == g

# byte_string_test()

# 递归检查并创建文件夹
def check_or_make_dir(path):
    sep = os.path.sep
    if not os.path.exists(path):
        if path.find(sep) != -1:
            check_or_make_dir(path[0:path.rfind(sep)])
        print path
        os.mkdir(path)

def move_ts():
    base_dir = ur"D:\workspace\python\51cto-download\51cto-video-download\学习\全栈网络安全专家".encode("gbk")
    target_dir = ur"D:\全栈网络安全专家".encode("gbk")
    for root,dir_list,file_list in os.walk(base_dir):
        for file in file_list:
            if not file.endswith("ts"):
                continue
            file_name = file.replace(".ts","")
            dir_name = os.path.basename(root)
            parent_dir = os.path.dirname(root)
            source_file = os.path.join(root,file)

            if file_name == dir_name:
                target_file_parent_dir = parent_dir
            else: 
                target_file_parent_dir = root
            target_file_parent_dir = target_file_parent_dir.replace(base_dir,target_dir)
            target_file = os.path.join(target_file_parent_dir,file)

            check_or_make_dir(target_file_parent_dir)
            print source_file
            print "target: "+target_file
            os.rename(source_file,target_file)
# move_ts()

def test_msg():
    print "\u52a0\u8f7d\u5217\u8868\u6210\u529f".decode("unicode-escape")
    # 加载列表成功
# test_msg()    

def login_test():
    session = Login().login()
    # url = 'https://edu.51cto.com/center/wejob/center/trains?page=1&size=1000'
    url = "https://edu.51cto.com/center/course/user/ajax-info-new?page=1&size=5&cate_id=0"
    resp = session.get(url)
    print resp.request.headers
    print resp.text
    url2 = "https://edu.51cto.com/center/course/user/get-study-course"
    session.get(url2).text
    s = ""
# login_test()    

def course_download_test():
    session = Login().login()
    # https://edu.51cto.com/course/3223.html
    # lesson.Lesson(session).set_course(3223,u"互联网大佬教你如何做经理-实战视频课程").lesson_list().download_m3u8()
    # 
    # lesson.Lesson(session).set_course(21007,u"清华编程高手尹成带你用java刷爆leetcode挑战腾讯offer").lesson_list().download_m3u8()
    # lesson.Lesson(session).set_course(8278,u"【微职位】软考：职场实用技能培训").lesson_list().download_m3u8()
    # lesson.Lesson(session).set_course(18136,u"MyBatis视频教程[IntelliJ IDEA版本]").lesson_list().download_m3u8()

# course_download_test()


print os.sep
print os.pathsep
print os.linesep
print os.curdir
print os.pardir
