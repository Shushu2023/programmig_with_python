'''In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
 case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.'''

filename = input("enter the file name and extention to tell you the media type of the file: ")

name, extention  = filename.strip().lower().split('.')
if extention== "gif":
    print("image/gif")
elif extention == "jpg":
    print("image/jpeg")
elif extention == ".jpeg":
    print("image/jpeg")
elif extention == "png":
    print("image/png")
elif extention == "pdf":
    print("application/pdf")
elif extention =="txt":
    print("text/plain")
elif extention =="zip":
    print("application/zip. Note, Windows uploads .zip files with the non-standard MIME type application/x-zip-compressed.")
else:
    print("application/octet-stream")