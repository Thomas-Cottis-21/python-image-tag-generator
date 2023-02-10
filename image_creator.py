import os 

directory = os.fsencode("C:\Development\Projects\Playgrounds\python_playground\gallery")

for file in os.listdir(directory):
    filename = file.decode()
    print('<img src="' + "/assets/img/gallery/" + filename + '" alt="'+ filename + '">')
