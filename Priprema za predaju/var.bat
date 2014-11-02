@echo off
SET /A id=1
setlocal ENABLEDELAYEDEXPANSION
FOR /d %%i in (tests/*) DO (
	copy tests\%%i\test.in testin\!id!.in
	SET /A id=id+1

	echo !id!
	echo tu sam 
)
endlocal