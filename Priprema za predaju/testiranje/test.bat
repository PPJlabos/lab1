
@for /d %%i in (testovi/*) do (
     GLA.py < testovi/%%i/test.lan
     SLEEP 2
     analizator\LA.py < testovi/%%i/test.in > testovi/%%i/analizirano.out
     echo %%i
     @echo %%i )
