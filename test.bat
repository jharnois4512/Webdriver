@echo off
for /f "tokens=*" %%s in (domainTests.txt) do (
    dig %%s >> domainOut.txt 
    nslookup %%s >> domainOut.txt
)
