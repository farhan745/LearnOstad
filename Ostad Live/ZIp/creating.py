import zipfile

with zipfile.ZipFile("new.zip","w") as zip:
    zip.write("d1.text")
    zip.write("d2.text")