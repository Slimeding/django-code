set /p commit_log=请输入描述日志信息:

git add .
git commit -m "%commit_log%"
git push origin master
pause