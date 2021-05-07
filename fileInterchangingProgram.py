
# getting the fileNames of the user and storing it in variables
fileA = str(input('Enter The Name Of The First file\n'))
fileB = str(input('Enter The Name Of The Second file\n'))


def readFile(fileA, fileB):
    if(not fileA and fileB):
        print('Please fill the text inputs correctly')
    else:
        # opening the fileA and reading al its data and storing it in fileAData variable
        fileAData = open(fileA, 'r').read()
        # opening the fileB and reading al its data and storing it in fileBData variable
        fileBData = open(fileB, 'r').read()

        # opening the fileA file and writing the fileB data that is in fileBData variable
        changeFileBDataWithFileAData = open(fileB, 'w').write(fileAData)

        # opening the fileB file and writing the fileA data that is in fileAData variable
        changeFileADataWithFileBData = open(fileA, 'w').write(fileBData)


# calling the readFile function
readFile(fileA, fileB)
