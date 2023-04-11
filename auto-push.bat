set year=%date:~0,4%
set month=%date:~5,2%
set day=%date:~8,2%
set hour=%Time:~0,2%
set min=%Time:~3,2%
set second=%Time:~6,2%


git add .
git commit -m "%year%/%month%/%day%%hour%:%min%:%second%"
git push origin master
pause