import os
import glob
from zipfile import ZipFile

# assign directory and extention
sDirectory = input("Please specify ZIP file source: \n") # Specify Source Directory
dDirectory = input("Extraction destination: \n") # Specify Destination Directory
ext = '.zip'
bslash = "\\" # added to make print statement display correct path
# iterate through directory searching for ZIP -- uses os module and Zipfile module
for path, dirc, files in os.walk(sDirectory):
    for name in files:
        if name.endswith(ext):
            print("Found: " + sDirectory + bslash + name)
            for filename in glob.iglob(f'{sDirectory}/*' + ext):           
                with ZipFile(filename, 'r') as zipObj:
                    # Extract all the contents of zip file in destination directory
                    zipObj.extractall(dDirectory)
                                       
dashStr = "-"
extractMsg = "The Zip files have been extracted!"
dnrMsg = "Leaving ZIP files in place"
dashRepeat1 = dashStr * len(extractMsg)
dashRepeat2 = dashStr * len(dnrMsg)
removeMsg = "Would you like to remove ZIP files? (Y)es or (N)o:  "
print(dashRepeat1 + "\n" + extractMsg + "\n" + dashRepeat1)

answer = input(removeMsg)

removeZIP = os.listdir(sDirectory)

if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
    for item in removeZIP:
        if item.endswith(".zip"):
            os.remove(os.path.join(sDirectory, item))
            print("Removing ZIP file: " + item)
    print("\n\n")


else:   
    print(dashRepeat2 + "\n" + dnrMsg + "\n" + dashRepeat2)
            
        