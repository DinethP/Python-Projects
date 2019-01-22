import sys


def CheckLine(line_found):
    if len(line_found) < 1:
        print('No match!')
        
    else:
        for item in line_found:
            print(item)

def Case1(fName, keyword):
    line_found = []
    
    try:
        file = open(fName)
        for line in file:
            if keyword in line.split():
                line_found.append(line.rstrip())
        CheckLine(line_found)
        file.close()
    
    except:
        
        print('File does not exist!')
        exit()

def sublist(keyword, line):
   
   return all(item in line  for item in keyword)

def Case2(fName, keyword):
    
    keyword_split = keyword.split()
    line_found = []
    
    try:
        file = open(fName)
        for line in file:
            line_lower = [word.lower() for word in line.split()]
            if sublist(keyword_split, line_lower):
                line_found.append(line.rstrip())
        CheckLine(line_found)
        file.close()
    
    except:
        
        print('File does not exist!')
        exit()


if '.txt' not in sys.argv[-1] or len(sys.argv) < 3:
    print('Not enough arguments!')
    exit()

else:
    fName = sys.argv[-1]
    
if len(sys.argv) > 3:
    
    keyword = " ".join([i.lower() for i in sys.argv[1:-1]])
    Case2(fName, keyword)

else:
    Case1(fName, sys.argv[0])