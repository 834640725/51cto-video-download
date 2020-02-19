
# encoding=utf-8
from cto import Login
from cto import lesson

def course_download(course_id, course_name):
    '''
    下载课程, 比如: https://edu.51cto.com/course/18136.html
    course_id是3223
    course_name是课程的名字, u"MyBatis视频教程[IntelliJ IDEA版本]"
    '''
    session = Login().login()
    lesson.Lesson(session).set_course(course_id,course_name).lesson_list().download_m3u8()

# https://edu.51cto.com/course/3223.html
# course_download(3223,u"互联网大佬教你如何做经理-实战视频课程")
# course_download(21007,u"清华编程高手尹成带你用java刷爆leetcode挑战腾讯offer")
# course_download(8278,u"【微职位】软考：职场实用技能培训")
# course_download(18136,u"MyBatis视频教程[IntelliJ IDEA版本]")
# course_download(21054,u"清华编程高手尹成带你基于keras+tensorflow实战深度学习人工智能")
course_download(21012,u"mysql高级教程")

