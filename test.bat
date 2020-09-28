@echo off
for /f "tokens=*" %%s in (domainTests.txt) do (
    dig %%s >> domainOut.txt 
    nslookup %%s >> domainOut.txt
)


rem Things that we want to have as statistics:
rem     What browser
rem     What extension 
rem     The number of cookies
rem     The number of objects interacted with
rem     