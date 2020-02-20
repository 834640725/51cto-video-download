@rem 作用：
@rem 用法：
@rem 其他：
@rem 2020/02/19 周三 23:44:03.49
@echo off&SetLocal EnableDelayEdexpansion&cd /d "%~dp0"
rem cmd.exe /K ""D:\program_files\miniconda\Scripts\activate.bat" "D:\program_files\miniconda""

set path=%path%;D:\program_files\miniconda\condabin
set PYTHONIOENCODING=UTF-8

set url=%~1
set title=%~2
echo %1
echo %2
title %title%
call D:/program_files/miniconda/Scripts/activate
call conda activate py2
rem python course_download.py "https://edu.51cto.com/course/10932.html" "哈哈"
python course_download.py "%url%" "%title%"
call conda deactivate

title done - %title%

rem D:\program_files\miniconda\condabin\conda.bat  activate py2
rem
rem echo %1
rem echo %2
rem conda activate py2
rem python course_download.py 111 "哈哈"
rem echo 222

rem cd d:\workspace\python\51cto-download\51cto-video-download
rem cmd /C "set "PYTHONIOENCODING=UTF-8"
rem set "PYTHONUNBUFFERED=1"
rem D:\program_files\miniconda\envs\py2\python.exe c:\Users\qxx\.vscode\extensions\ms-python.python-2020.2.63072\pythonFiles\ptvsd_launcher.py --default --client --host localhost --port 51655 D:\workspace\python\51cto-download\51cto-video-download/course_download.py


pause
