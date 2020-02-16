
2020-02-16: 可以使用; 

windows测试能用, 解决乱码: 
```
chcp 65001
set PYTHONIOENCODING=UTF-8
```

下载视频分为两步
1. 现在m3u8和key文件: 
- 对于微职位课程:
 `python run.py`
- 对于课程: 
参考 course_download.py

2. 解析m3u8和key下载视频: 
`python download_m3u8.py "m3u8和key所在的文件夹"`