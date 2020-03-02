
# encoding=utf-8
from cto import Login
from cto import lesson,tools
import sys,re,os
import  download_m3u8
import simplejson as  json

def course_download(course_id, course_name):
    '''
    下载课程, 比如: https://edu.51cto.com/course/18136.html
    course_id是3223
    course_name是课程的名字, u"MyBatis视频教程[IntelliJ IDEA版本]"
    '''
    session = Login().login()
    lesson.Lesson(session).set_course(course_id,course_name).lesson_list().download_m3u8()

def download_main():
    '''
    下载的入口
    '''
    reverse = False
    arg1 = ""
    arg2 = ""
    if len(sys.argv)>=2:
        arg1 = sys.argv[1]
    if len(sys.argv)>=3:
        arg2 =  sys.argv[2]

    print "arg1: "+arg1
    print "arg2:" +arg2 
    raw_input(u"确认后回车继续.............".encode("gbk"))
    os.system("chcp 65001") # cmd编码切换为utf8

    url = arg1
    id = re.split("[\./]",url)[-2]
    id = int(id)
    name = unicode(arg2,"gbk")
    name = re.sub('[\?\*\/\\\!]', '', name)
    name = tools.filename_reg_check(name)

    print "id: "+str(id)
    print "name: "+name
    course_download(id,name)

    base_dir = os.path.join(tools.main_path(),u"学习",name)
    download_m3u8.download_all_multi(base_dir)

def debug():
    course_id = 21072
    course_name = "别购买_共717课时-51CTO学院"
    session = Login().login()
    course = lesson.Lesson(session).set_course(course_id,course_name)
    # -------------------

    course_json_file = ur"Z:\xuexi\学习\别购买_共717课时-51CTO学院\m3u8\course.json"
    with open(course_json_file,"r") as f:
        course_json = f.read()
    data = json.loads(course_json)
    data_list = data["list"]  
    course.list = data_list[687:]
    course.download_m3u8()

if __name__ == "__main__": 
    # https://edu.51cto.com/course/3223.html
    # course_download(3223,u"互联网大佬教你如何做经理-实战视频课程")
    # course_download(21007,u"清华编程高手尹成带你用java刷爆leetcode挑战腾讯offer")
    # course_download(8278,u"【微职位】软考：职场实用技能培训")
    # course_download(18136,u"MyBatis视频教程[IntelliJ IDEA版本]")
    # course_download(21054,u"清华编程高手尹成带你基于keras+tensorflow实战深度学习人工智能")
    # course_download(21012,u"mysql高级教程")
    # course_download(20936,u"【精进-每天1小时】JIRA扩展定制从入门到精通 - ScriptRunner插件开发实战")
    # course_download(20760,u"Office365从入门到精通之Excel全方位")
    # course_download(18034,u"【3月1号前免费学】Oracle数据库培训教程（从Oracle 11g 到 Oracle 19c）")
    # course_download(17895,u"【3月1号前免费学】MySQL数据库入门到高薪培训教程（从MySQL 5.7 到 8.0）") 

    # debug()
    download_main()



