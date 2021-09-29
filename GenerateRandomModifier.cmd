:: 'test' will be a random integer from 1-100, inclusive.
SET /A test=%RANDOM% %%100 +1
echo %test%>StJude2021.txt
