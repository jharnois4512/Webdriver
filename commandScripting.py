import os
import csv
import subprocess

def main():
    with open('manualDatabase.csv', 'r') as t:
        reader = csv.DictReader(t)
        with open('digOutput.txt', 'w') as r:
            for lines in reader:
                # commmand = ['dig', lines['Full Host with Comma'], '| findstr /C:"CNAME"']
                # print(subprocess.call(commmand, stdout=r))
                r.write(str(os.system('dig ' + lines['Full Host with Comma'] + ' | findstr /C:"CNAME" >> outputDig.txt' )))

main()