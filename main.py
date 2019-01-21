'''
Created on 18 Dec 2018

@author: chris

Restructure steam workshop files downloaded via https://steamworkshopdownloader.io/ into proper directories
Files are unsorted, but do inclue directories in names, ie. model/author/model.mdl
- navigate to unzipped files
- read file name and split string
-- if text ends with /, 
--- check if directory already exists
--- if no directory, create new directory
--- else, enter directory
-- repeat until .
-- when text ends with .anything, finish creating directories and palce file in new directory
-return to top-level directory 
- repeat for all files

- read file name
- check if directory already exists
- create directory with every string fragment ending in /
- when string ends with .extension, rename file and place in new directory

'''
#https://docs.python.org/3/library/os.html
#https://thispointer.com/how-to-change-current-working-directory-in-python/
import os

def getDirectory():
    #Navigate to directory
    targetDir = input("Enter directory path: ") #get user input (text prompt for now)
    #cd to directory
    try:
        os.chdir(targetDir)
        print(os.getcwd())
        return targetDir
    except OSError:
        print("Could not get directory")

def getListOfFiles():
    #https://www.tutorialspoint.com/python/os_listdir.htm
    listOfFiles = os.listdir(targetDir)    #needs some way to check that it isn't finding folders
    print(len(listOfFiles), "files found")
    return listOfFiles
    
def createDirectories(listOfFiles, targetDir):
    #check if directory with string part exists
    #recursively create directory until .extension encountered
    #plonk file in 
    
    #split up each file name when we encounter a / (may be a \\ or \, seems to depend on how print is called)
    for file in listOfFiles:        #starts as a list of lists
        print(file)
        element = file.split("\\")  #produces a list
        print(element)

        for text in element:
            #if directory exists, enter
            if os.path.exists(text):        
                os.chdir(text)
                
            #else, create, Make sure we don't turn the file into a folder
            elif not os.path.exists(text) and "." not in text:
                os.makedirs(text)
                os.chdir(text)
                
            #finally needs something to plonk actual file into final directory
            if "." in text:
                placeInTo = os.getcwd()
                os.chdir(targetDir)
                os.rename(targetDir + "/" + file, placeInTo + "/" + text)
        
        #finally finally, return to top level directory        
        os.chdir(targetDir)

targetDir = getDirectory()
allFiles = getListOfFiles()
createDirectories(allFiles, targetDir)
