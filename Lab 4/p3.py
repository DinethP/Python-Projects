import fnmatch
import sys
import re
import glob


def case1(fName, outputObject):
    try:
        input_fName = open(fName)
        characters, words, lines = 0, 0, 0
        
        for character in input_fName.read():
            if character.isalpha():
                characters += 1

        input_fName = open(fName)
        
        for l in input_fName:
            for word in l.split():
                words += 1

        input_fName = open(fName)
        
        for l in input_fName:
            lines += 1
        writeCase1(characters, words, lines, outputObject)
    except:
        print('Opening file', fName, 'failed!')
        exit()

def case2(fNames, outputObject):
    try:
        
        for fName in fNames:
            input_fName = open(fName)
            characters, words, lines = 0, 0, 0
            for character in input_fName.read():
                if character.isalpha():
                    characters += 1

            input_fName = open(fName)
            for l in input_fName:
                for word in l.split():
                    words += 1

            input_fName = open(fName)
            for item in input_fName:
                lines += 1
            writeCase2(fName, characters, words, lines, outputObject)
    except:
        print('Opening file', fName, 'failed!')
        exit()

def writeCase1(characters, words, lines, outputObject):

    outputFile = open(outputObject, "w")
    outputFile.writelines(['Number of characters: ', str(characters), '.',
                         '\n', 'Number of words: ', str(words), '.',
                         '\n', 'Number of lines: ', str(lines), '.', '\n'])
   

def writeCase2(fName, characters, words, lines, outputObject):
    
    outputFile = open(outputObject, "w")
    outputFile.writelines(['Name of file: ', fName, '.',  
                        '\n','Number of characters: ', str(characters), '.',
                          "\n", 'Number of words: ', str(words), '.',
                         '\n', 'Number of lines: ', str(lines), '.', '\n'])


modified = []

fileList = [f for f in glob.glob("*.txt")]

if '?' in sys.argv[1]:
    modified = fnmatch.filter(fileList, sys.argv[1])
    case2(modified, sys.argv[2])

elif '*' in sys.argv[1]:
    regex = re.compile(sys.argv[1])
    modified = fnmatch.filter(fileList, sys.argv[1])
    case2(modified, sys.argv[2])

else:
    case1(sys.argv[1], sys.argv[2])