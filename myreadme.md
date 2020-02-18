
2020-02-16: 目前可以解密视频, 下载到本地观看; 

# 使用方法
windows下cmd解决乱码问题: 
```
chcp 65001
set PYTHONIOENCODING=UTF-8
```

下载视频分为两步
1. 下载m3u8和key文件: 
- 对于微职位课程:
 `python run.py`
- 对于课程: 
参考 course_download.py

2. 解析m3u8和key, 下载视频:  
`python download_m3u8.py "m3u8和key所在的文件夹"`