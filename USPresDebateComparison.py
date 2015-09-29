# Testing the Intelligence of US Presidents Since 1980.
# Project 2 for CS0931
# A Program by Tyler Daelemans.
# Copyright 2014.

# This program will run by itself when you run it in IDLE. (Hit F5.)
# It will ask if you want to run it again when you're done. If you make a mistake,
# either re-run the program or type "runProgram()" in IDLE.
import urllib
import re
import random
test = False
# Most of my test cases are unconventional because they are contingent upon a URL. Instead, I just
# chose to have periodic "printouts" of my strings to make sure they were functioning as they should.
# There is one 'conventional' test function for the dictionaryCheck if you insist.

#Step 1
# * -> string * string
def presidentSelection():
    '''Prompts the user to enter two candidates they would like to compare. Valid
    options include: Reagan, H.W. Bush, Clinton, W. Bush, Kerry, Obama.'''
    candidate1 = raw_input('Who is the first candidate you would like to compare? \n (Blank defaults to President George W. Bush.) \n Valid inputs are: "Reagan", "HWBush", "Clinton", "WBush", "Kerry", and "Obama."\n')
    candidate2 = raw_input('Who is the second candidate you would like to compare? \n (Blank defaults to former Senator John F. Kerry.) \n Valid inputs are: "Reagan", "HWBush", "Clinton", "WBush", "Kerry", and "Obama."\n')
    if candidate1.lower() == 'bush':
        decision = raw_input('Do you mean H.W. Bush (Type "HW") or W. Bush (Type "W")? \n')
        if decision.upper() == "HW":
            candidate1 = "HWBush"
        if decision.upper() == "W":
            candidate1 = "WBush"
        if decision.upper() != "HW":
            if decision.upper() != "W":
                print "Error, please try again."
    if candidate2.lower() == 'bush':
        decision = raw_input('Do you mean H.W. Bush (Type "HW") or W. Bush (Type "W")? \n')
        if decision.upper() == "HW":
            candidate2 = "HWBush"
        if decision.upper() == "W":
            candidate2 = "WBush"
        if decision.upper() != "HW":
            if decision.upper() != "W":
                print "Error. Please try again."
    if candidate1 == '':
        candidate1 = "WBush"
    if candidate2 == '':
        candidate2 = "Kerry"
    candidate1 = candidate1.lower()
    candidate2 = candidate2.lower()
    return [candidate1, candidate2]


#Step 2
#getTranscript still needs some alteration to automatically find the URL for each prez.
# str * str -> (file)
def getTranscript(url,outputfileName, candidate): 
    '''Gets the text from a Presidency Project URL and puts it in a text file.
    INPUTS: url (String) - the url of the transcript you want
            outputfile (String) - the name of the output file to write to
    OUTPUTS: none'''

    # fetch text from URL
    print 'Fetching url:',url,'...'
    myURLFile = urllib.urlopen(url)
    myString = myURLFile.read()
    myURLFile.close()

        # There is a SINGLE line that has the ENTIRE transcript.
    # This is the LONGEST line in the file! Find it.
    myList = myString.split('\n')
    longestLine = ''
    for line in myList:
        if len(line) > len(longestLine):
            longestLine = line

    # set longest line to be myStr
    myStr = longestLine
    
    # substitute all <p> (paragraphs) with TWO newlines
    myStr = re.sub('<p>','\n\n',myStr)

    # substute all <br> (breaks) with ONE newline
    myStr = re.sub('<br>','\n',myStr)
    
    # substitutes all speakers (in italics) with an easily-identifiable tag, non-candidate
    # speakers are replaced with the string 'STOP//'
    if candidate == 'kerry' or candidate == 'wbush':
        myStr = re.sub(r'<i>Laughter</i>', '', myStr)
        myStr = re.sub(r'<i>Senator Kerry. </i>', 'KERRYSTART//', myStr)
        myStr = re.sub(r'<i>Senator John F. Kerry. </i>', 'KERRYSTART//', myStr)
        myStr = re.sub(r'<i>President Bush. </i>', 'WBUSHSTART//', myStr)
    if candidate == 'wbush':
        myStr = re.sub('BUSH:', 'WBUSHSTART//', myStr)
        myStr = re.sub('MODERATOR:', 'STOP//', myStr)
        myStr = re.sub('GORE:', 'STOP//', myStr)
    if candidate == 'obama':
        myStr = re.sub(r'<i>The President. </i>', 'OBAMASTART//', myStr)
        myStr = re.sub(r'<b>OBAMA:</b>', 'OBAMASTART//', myStr)
        myStr = re.sub(r'<b>OBAMA</b>', 'OBAMASTART//', myStr)
    if candidate == 'clinton':
        myStr
        myStr = re.sub(r'<i>The President. </i>', 'CLINTONSTART//', myStr)
        myStr = re.sub(r'<i>Laughter</i>', '', myStr)
        myStr = re.sub('Governor Clinton\.', 'CLINTONSTART//', myStr)
        myStr = re.sub('Mr. Perot\.', 'STOP//', myStr)
        myStr = re.sub('President Bush\.', 'STOP//', myStr)
        myStr = re.sub(r'<i>Q. </i>', 'STOP//', myStr)
        myStr = re.sub(r'<i>Senator Dole. </i>', 'STOP//', myStr)
        myStr = re.sub('Mr. Lehrer\.', 'STOP//', myStr)
        myStr = re.sub('Ms. Simpson\.', 'STOP//', myStr)
    if candidate == 'hwbush':
        myStr = re.sub('President Bush\.', 'HWBUSHSTART//', myStr)
        myStr = re.sub('BUSH:', 'HWBUSHSTART//', myStr)
        myStr = re.sub('DUKAKIS:', 'STOP//', myStr)
        myStr = re.sub('LEHRER:', 'STOP//', myStr)
        myStr = re.sub('GROER:', 'STOP//', myStr)
        myStr = re.sub('JENNINGS:', 'STOP//', myStr)
        myStr = re.sub('MASHEK:', 'STOP//', myStr)
        myStr = re.sub('SHAW:', 'STOP//', myStr)
        myStr = re.sub('COMPTON:', 'STOP//', myStr)
        myStr = re.sub('MITCHELL:', 'STOP//', myStr)
        myStr = re.sub('WARNER:', 'STOP//', myStr)
        myStr = re.sub('Mr. Perot\.', 'STOP//', myStr)
        myStr = re.sub('Governor Clinton\.', 'STOP//', myStr)
        myStr = re.sub('Mr. Lehrer\.', 'STOP//', myStr)
        myStr = re.sub('Ms. Simpson\.', 'STOP//', myStr)
        myStr = re.sub(r'<i>Q. </i>', 'STOP//', myStr)
    if candidate == 'reagan':
        myStr = re.sub('REAGAN:', 'REAGANSTART//', myStr)
        myStr = re.sub('GOV. RONALD REAGAN:', 'REAGANSTART//', myStr)
        myStr = re.sub('THE PRESIDENT', 'STOP//', myStr)
        myStr = re.sub('ANDERSON:', 'STOP//', myStr)
        myStr = re.sub('MOYERS:', 'STOP//', myStr)
        myStr = re.sub('CAROL LOOMIS:', 'STOP//', myStr)
        myStr = re.sub('REP. JOHN B. ANDERSON', 'STOP//', myStr)
        myStr = re.sub('GREENBERG', 'STOP//', myStr)
        myStr = re.sub('CHARLES CORDDRY', 'STOP//', myStr)
        myStr = re.sub('LEE MAY', 'STOP//', myStr)
        myStr = re.sub('JANE BRYANT QUINN', 'STOP//', myStr)
        myStr = re.sub('GOLDEN', 'STOP//', myStr)
        myStr = re.sub('MR. STONE', 'STOP//', myStr)
        myStr = re.sub('MR. SMITH', 'STOP//', myStr)
        myStr = re.sub('MR. ELLIS', 'STOP//', myStr)
        myStr = re.sub('MR. HILLIARD', 'STOP//', myStr)
        myStr = re.sub('MS. WALTERS', 'STOP//', myStr)
        myStr = re.sub('GOVERNOR REAGAN', 'REAGANSTART//', myStr)
        myStr = re.sub('The President.', 'REAGANSTART//', myStr)
        myStr = re.sub('Mr. Wieghart.', 'STOP//', myStr)
        myStr = re.sub('Mr. Mondale.', 'STOP//', myStr)
        myStr = re.sub('Ms. Walters.', 'STOP//', myStr)
        myStr = re.sub('Ms. Sawyer.', 'STOP//', myStr)
        myStr = re.sub('Mr. Barnes.', 'STOP//', myStr)
        myStr = re.sub('Mr. Newman.', 'STOP//', myStr)
        myStr = re.sub('Ms. Geyer.', 'STOP//', myStr)
        myStr = re.sub('Mr. Kalb.', 'STOP//', myStr)
        myStr = re.sub('Mr. Kondracke.', 'STOP//', myStr)
        myStr = re.sub('Mr. Trewhitt.', 'STOP//', myStr)
        myStr = re.sub('LOOMIS:', 'STOP//', myStr)       


        
    #Catches anything else bold or italic that we haven't specified and makes them STOP flags.
    myStr = re.sub('Applause', '', myStr)
    myStr = re.sub('<b>.*?</b>', 'STOP//', myStr)
    myStr = re.sub('<i>.*?</i>', 'STOP//', myStr)

    # remove all other bracket tags
    myStr = re.sub('<.*?>','',myStr)

    # remove leading and trailing whitespace
    myStr = re.sub('^\s+','',myStr)
    myStr = re.sub('\s+$','',myStr)

    #It's much easier for my regex in Step 3 if we remove new line characters.
    myStr = re.sub('\n', ' ', myStr)
    #Some weird hold-over from importing the text intoa  .txt file. I'm assuming it's because n-dashes work in .txt files but m-dashes
    # (--) do not work. Either way, it's unncessary for our purposes.
    myStr = re.sub('&mdash;', ' ' , myStr)



    # open output file FOR WRITING (note the 'w'), write to file, and close.
    print 'Writing to file',outputfileName,'...'
    outFile = open(outputfileName,'w')
    outFile.write(myStr+'\n')
    outFile.close()

    return

def newgetTranscript(candidate):
    num = 1
    nameofFile = candidate + str(num) + '.txt'
    candidateList = []
    if candidate == 'kerry':
            for obj in ohfourDebates:
                candidateList.append(nameofFile)
                getTranscript(obj, nameofFile, candidate)
                nameofFile = candidate + str(num + 1) + '.txt'
                num += 1
    if candidate == 'obama':
            for obj in obamaDebates:
                candidateList.append(nameofFile)
                getTranscript(obj, nameofFile, candidate)
                nameofFile = candidate + str(num +1) + '.txt'
                num += 1
    if candidate == 'wbush':
            for obj in wbushDebates:
                candidateList.append(nameofFile)
                getTranscript(obj, nameofFile, candidate)
                nameofFile = candidate + str(num +1) + '.txt'
                num += 1
    if candidate == 'clinton':
            for obj in clintonDebates:
                candidateList.append(nameofFile)
                getTranscript(obj, nameofFile, candidate)
                nameofFile = candidate + str(num + 1) + '.txt'
                num += 1
    if candidate == 'hwbush':
            for obj in hwbushDebates:
                candidateList.append(nameofFile)
                getTranscript(obj, nameofFile, candidate)
                nameofFile = candidate + str(num + 1) + '.txt'
                num += 1
    if candidate == 'reagan':
            for obj in reaganDebates:
                candidateList.append(nameofFile)
                getTranscript(obj, nameofFile, candidate)
                nameofFile = candidate + str(num + 1) + '.txt.'
                num += 1
    return candidateList
    

#Step 3
# str -> str
# Removes punctuation from our strings for analysis.
def removePunctuation(s):
    '''Takes a string as argument, and returns another string,
    replacing punctuation marks with whitespaces.
    '''
    result = ''
    for char in s:
        if(char == '!' or char == '$'or char == '&' or char == '('
           or char == ')' or char == '?' or char == '.' or char == ','
           or char == '"' or char == '\'' or char == ';' or char == ':'
           or char == '-' or char == '_'):
            result += ' '
        else:
            result += char
    return result

#str * str -> str
def candidateSpeech(fileName, name):
    '''This opens each transcript file and transcribes it to a string. It also uses
    regular expressions to read-in only text for the candidate with "name."'''
    myFile = open(fileName,'r')
    myString = myFile.read()
    myFile.close()
    newString = ''
    if name == 'kerry':
        matchList = re.findall('KERRYSTART//(.*?)(STOP//|WBUSHSTART//)', myString)
        for subString in matchList:
            newString += str(subString)
    if name == 'wbush':
        matchList = re.findall('WBUSHSTART//(.*?)(STOP//|KERRYSTART//)', myString)
        for subString in matchList:
            newString += str(subString)
    if name == 'obama':
        matchList = re.findall('OBAMASTART//(.*?)(STOP//)', myString)
        for subString in matchList:
            newString += str(subString)
    if name == 'clinton':
        matchList = re.findall('CLINTONSTART//(.*?)(STOP//)', myString)
        for subString in matchList:
            newString += str(subString)
    if name == 'hwbush':
        matchList = re.findall('HWBUSHSTART//(.*?)(STOP//)', myString)
        for subString in matchList:
            newString += str(subString)
    if name == 'reagan':
        matchList = re.findall('REAGANSTART//(.*?)(STOP//)', myString)
        for subString in matchList:
            newString += str(subString)
    return newString

# * -> str
def candidateCompile(candidate, candidateList):
    '''This function compiles all instances of candidateSpeech for each candidate
    into a single string. Candidate should be candidate's name, candidateList should
    be their respective debate file list.'''
    candText = ''
    for debateFile in candidateList: 
        candText += candidateSpeech(debateFile, candidate)
    candText = removePunctuation(candText)
    return candText
        

#Step 4
# str -> str list
def listCreate(stringName):
    '''Takes a string, splits it into words. Creates a list.'''
    newList = stringName.split()
    return newList

#Step 5
# str list -> str list
def listTwelve(listName):
    '''Takes a list, and outputs the same list with words that are longer than
    seven characters. Also removes any "flagging" text that made it into the list.'''
    TwelveList = []
    for obj in listName:
        if len(obj) > 12:
            TwelveList.append(obj)
    for obj in TwelveList:
        if obj == 'REAGANSTART//' or obj == 'HWBUSHSTART//' or obj == 'CLINTONSTART//' or obj == 'WBUSHSTART//' or obj == 'KERRYSTART//' or obj == 'OBAMASTART//' or obj == 'STOP//':
            TwelveList.remove(obj)
        if obj.lower() == 'REAGANSTART//' or obj.lower() == 'HWBUSHSTART//' or obj.lower() == 'CLINTONSTART//' or obj.lower() == 'WBUSHSTART//' or obj.lower() == 'KERRYSTART//' or obj.lower() == 'OBAMASTART//' or obj.lower() == 'STOP//':
            TwelveList.remove(obj)
    return TwelveList

#str list -> str list
def satWords(listName):
    '''Checks if the list contains words in the list of SAT words.'''
    candidateSAT = []
    myFile = open('SATWords.txt','r')
    satString = myFile.read()
    myFile.close()
    satWords = 'abase '
    satMatch = re.findall('\n[A-Za-z-]*', satString)
    for subString in satMatch:
        satWords += subString
    satList = satWords.split()
    for word in listName:
        if word == word in satList:
           candidateSAT.append(word)
    return candidateSAT

#str list -> str list
def removeDuplicates(listName):
    listName = sorted(listName)
    finalList = [listName[0]]
    for index in range(1, len(listName)):
        current = listName[index]
        previous = listName[index - 1]
        current = current.lower()
        previous = previous.lower()
        if current != previous:
            finalList.append(current)
    return finalList
        

# Step 6

# str -> str list
def getWebsterDictionary(letter):
    '''Gets all the words, parts of speech, and definitions for words
    starting with the letter and writes a tab-delimited file.
    INPUTS: letter (String)- a letter (from A to Z, case insensitive)
    OUTPUTS: lowercase list of words starting with input letter'''

    # make letter lowercase
    letter = letter.lower()

    # fetch text from URL
    url = 'http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_' + letter + '.html'
    myURLFile = urllib.urlopen(url)
    myString = myURLFile.read()
    myURLFile.close()
    myString = myString.lower()
    myList = myString.split()

    return myList

# str list -> str list
def dictionaryCheck(listName):
    '''Checks whether the words in the list exist in the dictionary.
    Deletes any words that are not.'''
    newList = []
    for word in listName:
        dictionaryLetter = word[0]
        testDictionary = getWebsterDictionary(dictionaryLetter)
        if word.lower() in testDictionary:
            newList.append(word)
            print "Adding " + word + " to valid word list."
    return newList

def testDictionaryCheck():
    testList = ['Cat', 'dog', 'earth', 'friend']
    testResult = dictionaryCheck(testList)
    if testList != testResult:
        print 'dictionaryCheck is not functioning properly.'
    if testList == testResult:
        print 'dictionaryCheck is functioning properly.'

# Step 7
# str List * str -> float
def frequencyCalculate(truncatedList, entireDebateString):
    '''Takes the number of words that were unique, >12 characters, or on the SAT list and divides them
    by the total number of words in all the debates. Outputs a frequency as a float.'''
    frequency = len(truncatedList) / float(len(entireDebateString.split()))
    return frequency

# Step 8
# float * float * str * str -> (file)
def intelligence(frequency1, frequency2, candidate1, candidate2, cand1text, cand2text, cand1List, cand2List):
    '''Creates a matrix and prints a file that compares the percentages of the
two candidates.'''
    print 'Writing file ' + candidate1 + 'v' + candidate2 + '.csv' + '...'
    outfileName = candidate1 + 'v' + candidate2 + '.csv'
    outFile = open(outfileName, 'w')
    print 'Writing header text ...'
    headerRow = 'Vocabulary Usage of ' + str(candidate1.upper() + ' vs. ' + str(candidate2.upper()) + '\n')
    outFile.write(headerRow)
    print 'Writing data ...'
    outFile.write(',' + candidate1 + ',' + candidate2 + ',' + '\n' + '% of Unique Words Fitting Criteria' + ',' + str(frequency1) + ',' + str(frequency2) + ', \n' + 'Number of Unique Words Fitting Criteria:' + ',' + str(len(cand1List)) + ',' + str(len(cand2List)) + ', \n' + 'Total words examined: ,' + str(len(cand1text.split())) + ',' + str(len(cand2text.split())) + '\n')
    sampleList1 = []
    sampleList2 = []
    listoflists = [cand1List, cand2List]
    emptstr1 = ''
    emptstr2 = ''
    for candlist in listoflists:
        if candlist == cand1List:
            sampList = sampleList1
        if candlist == cand2List:
            sampList = sampleList2
        numbersUsed = []
        for index in range(0, 50):
            wordindex = random.randrange(0, len(candlist))
            if wordindex in numbersUsed:
                wordindex = random.randrange(0, len(candlist))
                if wordindex in numbersUsed:
                    wordindex = random.randrange(0, len(candlist))
                    if wordindex in numbersUsed:
                        wordindex = random.randrange(0, len(candlist))
                        if wordindex in numbersUsed:                        
                                wordindex = random.randrange(0, len(candlist))
                                if wordindex in numbersUsed:
                                        wordindex = random.randrange(0,len(candlist))
                                        if wordindex in numbersUsed:
                                                print "You have some insane luck."
                                                # A little easter egg if you somehow manage to defy the odds of getting a duplicate number
                                                # six times in a row.
                                                # I'm realizing I could have used a "while loop" to do this instead.
                                                # Though this is 45 minutes before the deadline, and I like the easter egg.
            numbersUsed.append(wordindex)
            sampList.append(candlist[wordindex])
    for obj in sampleList1:
        emptstr1 += obj + ' '
    for obj in sampleList2:
        emptstr2 += obj + ' '
    outFile.write('Sample words used: ,' + emptstr1 + ',' + emptstr2 + ', \n')
    print 'Done.'

ohfourDebates = ['http://www.presidency.ucsb.edu/ws/index.php?pid=63163', 'http://www.presidency.ucsb.edu/ws/index.php?pid=72776', 'http://www.presidency.ucsb.edu/ws/index.php?pid=72770']
obamaDebates = ['http://www.presidency.ucsb.edu/ws/index.php?pid=78691', 'http://www.presidency.ucsb.edu/ws/index.php?pid=84482', 'http://www.presidency.ucsb.edu/ws/index.php?pid=84526', 'http://www.presidency.ucsb.edu/ws/index.php?pid=102317', 'http://www.presidency.ucsb.edu/ws/index.php?pid=102343', 'http://www.presidency.ucsb.edu/ws/index.php?pid=102344'] 
wbushDebates = ['http://www.presidency.ucsb.edu/ws/index.php?pid=63163', 'http://www.presidency.ucsb.edu/ws/index.php?pid=72776', 'http://www.presidency.ucsb.edu/ws/index.php?pid=72770', 'http://www.presidency.ucsb.edu/ws/index.php?pid=29418', 'http://www.presidency.ucsb.edu/ws/index.php?pid=29419', 'http://www.presidency.ucsb.edu/ws/index.php?pid=29420']
clintonDebates = ['http://www.presidency.ucsb.edu/ws/index.php?pid=52060', 'http://www.presidency.ucsb.edu/ws/index.php?pid=52115', 'http://www.presidency.ucsb.edu/ws/index.php?pid=21625', 'http://www.presidency.ucsb.edu/ws/index.php?pid=21617', 'http://www.presidency.ucsb.edu/ws/index.php?pid=21605']
hwbushDebates = ['http://www.presidency.ucsb.edu/ws/index.php?pid=21625', 'http://www.presidency.ucsb.edu/ws/index.php?pid=21617', 'http://www.presidency.ucsb.edu/ws/index.php?pid=21605', 'http://www.presidency.ucsb.edu/ws/index.php?pid=29412', 'http://www.presidency.ucsb.edu/ws/index.php?pid=29411']
reaganDebates = ['http://www.presidency.ucsb.edu/ws/index.php?pid=29408', 'http://www.presidency.ucsb.edu/ws/index.php?pid=39199', 'http://www.presidency.ucsb.edu/ws/index.php?pid=39296', 'http://www.presidency.ucsb.edu/ws/index.php?pid=29407']
def runProgram():
    '''This function runs the program! No inputs required.'''
# This is the new main function of this program.
    myCandList = presidentSelection()
    while myCandList[0] == 'bush' or myCandList[1] == 'bush':
        myCandList = presidentSelection()
    if myCandList[0] == 'reagan' or myCandList[0] == 'hwbush' or myCandList[0] == 'clinton' or myCandList[0] == 'wbush' or myCandList[0] == 'kerry' or myCandList[0] == 'obama':
        pass
    else:
        print 'Invalid candidate. Running program again.'
        runProgram()
    if myCandList[1] == 'reagan' or myCandList[1] == 'hwbush' or myCandList[1] == 'clinton' or myCandList[1] == 'wbush' or myCandList[1] == 'kerry' or myCandList[1] == 'obama':
        pass
    else:
        print 'Invalid candidate. Running program again.'
        runProgram()
    candidate1 = myCandList[0]
    candidate2 = myCandList[1]
    candidate1list = newgetTranscript(candidate1)
    candidate2list = newgetTranscript(candidate2)
    print 'Transcribing files to string ... '
    cand1text = candidateCompile(candidate1, candidate1list)
    cand2text = candidateCompile(candidate2, candidate2list)
    print 'Files transcribed.'
    if test:
        print "Test of first candidate's debate speech: \n" + cand1text[0:500]
        print "Test of second candidate's debate speech: \n"+ cand2text[0:500]
    print 'Creating lists ... '
    cand1List = listCreate(cand1text)
    cand2List = listCreate(cand2text)
    if test:
        print "Test of list creation: \n" + str(cand1List[0:25])
        print "Test of list creation: \n" + str(cand2List[0:25])
    cand1ListLength = listTwelve(cand1List)
    cand2ListLength = listTwelve(cand2List)
    if test:
        print cand1ListLength
    candidate1sat = satWords(cand1List)
    candidate2sat = satWords(cand2List)
    cand1List = cand1ListLength + candidate1sat
    cand2List = cand1ListLength + candidate2sat
    if test:
        print "Test of mixing two lists: \n"+ str(cand2List[0:100])
    cand1List = removeDuplicates(cand1List)
    cand2List = removeDuplicates(cand2List)
    print 'Lists created.'
    if test:
        print cand1List[0:50]
    dictionaryRun = raw_input('Do you want to run the dictionaryCheck? (y/n?) \n (WARNING: NOT RECOMMENDED. WILL TAKE ~40 MINS) \n')
    if dictionaryRun == 'yes' or dictionaryRun == 'y':
        # Even with the fast method of iteration, this function runs slowly. Use at your own risk.
        # it takes about 40 minutes to run properly. (It checks if ~400 words are in the dictionary.)
        # It works though, if you want to go to lunch and come back later.
        print 'Running dictionaryCheck...'
        cand1List = dictionaryCheck(cand1List)
        cand2List = dictionaryCheck(cand2List)
        print 'dictionaryCheck completed. (Finally.)'
    if dictionaryRun == 'No' or dictionaryRun == 'n':
        print 'Not running dictionaryCheck. Continuing on ...'
    else:
        print 'Invalid input. Not running dictionaryCheck. Continuing on ...'
    if test:
        testDictionaryCheck()
    frequency1 = frequencyCalculate(cand1List, cand1text)
    frequency2 = frequencyCalculate(cand2List, cand2text)
    print "The Frequency of " + candidate1 + " is " + str(frequency1) + "."
    print "The Frequency of " + candidate2 + " is " + str(frequency2) + "."
    if frequency1 > frequency2:
        print candidate1.upper() + " has a more varied and \"intellectual\" vocabulary than " + candidate2.upper() + "."
    if frequency2 > frequency1:
        print candidate2.upper() + " has a more varied and \"intellectual\" vocabulary than " + candidate1.upper() + "."
    if frequency1 == frequency2:
        if candidate1 == candidate2:
            print 'These are the same candidate... not sure what insight you\'re hoping for.'
        else:
            print candidate1.upper() + " and " + candidate2.upper() + '(by some stroke of luck,) have the exact same variance in vocabulary.'
    intelligence(frequency1, frequency2, candidate1, candidate2, cand1text, cand2text, cand1List, cand2List)
    rerun = raw_input('Run again with different inputs? (y/n) \n')
    if rerun == 'y' or rerun == 'yes':
        runProgram()
    elif rerun == 'no' or rerun == 'n':
        print 'Quitting program ...'
        print 'See you soon!'
        return
    else:
        print 'Unrecognized input. Quitting program.'
        return
runProgram()
