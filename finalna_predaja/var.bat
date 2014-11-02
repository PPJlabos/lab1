@echo off
SET /A id=1
setlocal ENABLEDELAYEDEXPANSION
FOR /r %%i IN (testlan\*) DO (

	echo %%i
	GLA.py < %%i
	
	timeout 2
	copy analizator\izlazni.txt izlazni.txt
	timeout 1
	analizator\LA.py < testin\!id!.in > tests_analizirano\!id!.out
	

	SET /A id=id+1

	echo !id!
	echo tu sam 

	timeout 3
)
endlocal