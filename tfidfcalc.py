import math, os, string

def wordList(Doc):
    lst = []

    with open(Doc, 'r') as f:
        for line in f:
            for word in line.split():
                lst.append(word.strip())
                #adding all words in lst

    return lst

def removePuncs(wordList):
    wordListRet = []
    stopWords = [ "a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours    ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]
    #getting stopwords
  
    for word in wordList:
        word = word.translate(str.maketrans('', '', string.punctuation))
        #take out punctuation
        word = word.lower()
        #replace all uppercase with lowercase
        word = word.strip()
        #take out whitespace and newlines
        if word != '' and word not in stopWords:
            wordListRet.append(word)
    
    return wordListRet

def termFrequencyInDocs(wordL):
    dic = {}
    for word in wordL:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
            #increment dic freq when found

    return dic

def wordDocFre(dicList):
    dicRet = {}

    for dic in dicList:
        for word in dic:
            if word in dicRet:
                dicRet[word] += 1  
                #increment number of doc with word
            else:
                dicRet[word] = 1
                #starting value of word

    return dicRet


def inverseDocFre(dicList,base):
    #base is output dic from wordDocFre
    #dicList is as is in wordDocFre
    idfDic = {}
    N = len(dicList)
    #getting number of doc

    for word in base:
        idfDic[word] = math.log((N+1) / base[word])
        #calculate idf

    return idfDic

def tfidf(docList):
    tfidfDicList = []
    #making return list of dictionary
    dicList = []

    for doc in docList:
        dicList.append(termFrequencyInDocs(removePuncs(wordList(doc))))
        #make list of dictionaries

    base = wordDocFre(dicList)
    idfDic = inverseDocFre(dicList, base)
    #calculate idf

    for dic in dicList:
        tfidfDic = {}
        N = len(dic)
        for word, freq in dic.items():
            tf = (freq/N)
            tfidfDic[word] = (tf)*(idfDic[word])
            #calculate the tfidf of each word in each doc
        tfidfDicList.append(tfidfDic)
        #build return list

    return tfidfDicList

#getting the list of dictionaries
docList = []

for filename in os.listdir(os.getcwd()+'\ACL txt'):
    docList.append(os.path.join(os.getcwd()+'\ACL txt', filename))

print(tfidf(docList))
