## ChangeRes
Windows Resolution Changer

Changes the Resolution by inputting the resolution after starting the script or by launching it with -x and -y parameters.

## Requirements:
pypiwin32\n
argparse

## Creating a .bat File
Create a .bat with the following code and replace *width* and *height*
```
ChangeRes.exe -x width -y height
```
For example:
```
ChangeRes.exe -x 1280 -y 720
```

## Is there a .exe file?
Yes, you can run it on every computer without having python 3 installed.
https://github.com/TA40/ChangeRes/releases/download/1.0/ChangeRes.exe

## Credits
With the help of StackOverflow and the Author Peter Wood
https://stackoverflow.com/a/54262365/7799387
