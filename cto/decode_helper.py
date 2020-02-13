# encoding=utf-8
import execjs, re, os


def get_decode_js():
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"decode.js")
    with open(filepath) as f:
        js = f.read()
    return js;

def get_sign(lesson_id):
    """
    sign似乎和日期有关
    """
    ctx = execjs.compile(get_decode_js())
    return ctx.call("getSign", lesson_id)

def decode(enkey,lesson_id):
    """
    获取解密后的key
    enkey: 加密的key
    """
    ctx = execjs.compile(get_decode_js())
    return ctx.call("decode", enkey,lesson_id)

if __name__ == '__main__':
    lesson_id = "1909_202649"
    sign = get_sign(lesson_id)
    print sign
    # 30ca145acdd978de2f9a7787e7531f77
    assert len(sign) == 32, "sign的长度"

    enKey = "0iWOiLXatRb46nHw7cd0WaxHONZxxH7aRow0wbqHiN3xwHmaRo60WaqHONZxwH7aRoO0WaqHONZxwH7lRo60wbqHONExwH7jROw3w5qlzNUHRHQdO5RajIWqNOSDj5NpwLuwxQiPOSUDiLiUjHxUjLXdPSJ2OLidjOvSjOXdWOUlWPi7wUVlPO0BhO43i5Q1yoQPjQX3QUrdQLjJiOfxQQuP0PnHe5HdjORljQQ7NQwUw5IUiISDj59pQQJuYXHDhPK5j5IxhOeD0HQpwUV7QPQ3QOClP5iHN5RlPb0MjQ03OPhJVXvoQHQdjSRUW5UJyoQlxLmpyOvSPPXajHf1Ob7lzN0iwHnlZUO1WahHiN0AVPmPvSw3WX9ajQ3xjb7qce4";
    key =decode(enKey,lesson_id);
    print key
    assert len(key) == 16, "key的长度"

'''
with open('js.js', encoding='utf8') as f:
    js = f.read()

# 通过compile命令转换成一个js对象
docjs = execjs.compile(js)

# 使用js对象的call方法调用函数
res = docjs.call('f', 'zhangjian')
print(res)

# 使用js对象的eval方法调用变量
res = docjs.eval('name')
print(res)
'''