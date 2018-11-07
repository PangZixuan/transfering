import os
import sys
import string
from bsddb3 import db
global outfull
outfull=False
def full_res(printer):
    global outfull
    if outfull:
        thisresult=curs_re.set(printer)[1]
        return thisresult
    else:
        return printer
def search_all(search_input):
    pass
def search_terms(search_input,init):
    answerlist=[]
    searchcom=(init+"-"+search_input)
    answer=curs_te.set(str.encode(searchcom))
    while answer:
        answerlist.append(answer[1])
        answer=curs_te.next_dup()
   # for answers in answerlist:
        #print(answers[1])        
    return answerlist
        
def search_years(search_input,sign):
    if sign == "<":
        #search for all years below
        answerlist=[]
        goodanswer=(curs_ye.first())
        while goodanswer:
            if goodanswer[0].decode()< search_input:
                answerlist.append(goodanswer[1])
                goodanswer=(curs_ye.next())
            else:
                break
        return answerlist        

      
    elif sign == ":":
        #search for all years equal
        answerlist=[]
        goodanswer=curs_ye.set(str(search_input).encode())
        #answerlist.append(goodwanswer)
       # goodanswer=curs_ye.next_dup()
        while goodanswer:
            answerlist.append(goodanswer[1])
            goodanswer=curs_ye.next_dup()   
        return answerlist
            
        
    elif sign == ">":
        #search for all years above
        answerlist=[]
        goodanswer=(curs_ye.last())
        year=goodanswer[0].decode()
        while goodanswer:
            year=goodanswer[0].decode()
            if year>search_input:
                answerlist.insert(0,goodanswer[1])
                goodanswer=(curs_ye.prev())
            else:
                break
        return answerlist
def get_data(newline):
    #this function processes all commands inputed in one line
    #outFlag = []
    global resultlist
    resultlist=[]
    for element in newline:
        if ":" in element:
            element_parsed = element.split(":")
            #print(element_parsed)
        elif "<" in element:
            element_parsed = element.split("<")
            #print(element_parsed)
        #elif "output" in element:
           # outFlag.append(element)
        #elif "=" in element:
            #element_parsed = element.split("=")
            ##print(element_parsed)
        elif ">" in element:
            element_parsed = element.split(">")
            #print(element_parsed)
        else:
            element_parsed = element.split(" ")
            element_parsed.append("wholeWord")#this subelement has a flag as its last element which indicates that it is a whole word
        #if outFlag:
            #check the last output flag, outFlag[1] == full, print all data, elif output[1] == key, print record key
            #outFlag = outFlag[len(outFlag)-1] .split("=")
           # print(outFlag)
        #subword = "subelements are"+"\n"+(",".join(element_parsed))+"\n"
        #sys.stdout.write(subword)
       # else:
           # print("subelements are:",element_parsed)
        if element_parsed[len(element_parsed)-1] == "wholeWord":
            #delete the flag
            del element_parsed[len(element_parsed)-1]
            #process the whole word
            search_all(element_parsed)
        else:
            criteria = element_parsed[0]
            if criteria == "title":
                result=search_terms(element_parsed[1],"t")
                resultlist.append(result)
            elif criteria == "author":
                result=search_terms(element_parsed[1],"a")
                resultlist.append(result)
            elif criteria == "other":
                result=search_terms(element_parsed[1],"o")
                resultlist.append(result)
            elif criteria == "year":
                if "<" in element:
                    result=search_years(element_parsed[1],"<")
                    resultlist.append(result)
                elif ":" in element:
                    result=search_years(element_parsed[1],":")
                    resultlist.append(result)
                elif ">" in element:
                    result=search_years(element_parsed[1],">")
                    resultlist.append(result)
    print("final result: ",resultlist)
    final=resultlist[0]
    for i in range(0,len(resultlist)):
        if i+1<len(resultlist):
            final=list(set(final)&set(resultlist[i+1]))
    if final != []:
        for every in final:
            print(full_res(every))
            
        #print(final)
    else:
        print("No matching found")

def create_database():
    DB_re = "re.idx"
    DB_te = "te.idx"
    DB_ye = "ye.idx"
    
    global curs_re
    global database_re    
    database_re = db.DB()#set up database for records
    database_re.open(DB_re,None, db.DB_HASH, db.DB_CREATE)
    curs_re = database_re.cursor()
    
    global curs_te
    global database_te    
    database_te = db.DB()#set up database for terms
    database_te.open(DB_te,None, db.DB_BTREE, db.DB_CREATE)
    curs_te = database_te.cursor()
    
    global curs_ye
    global database_ye    
    database_ye = db.DB()#set up database for years
    database_ye.open(DB_ye,None, db.DB_BTREE, db.DB_CREATE)
    curs_ye = database_ye.cursor()
def handleform(whatform,nline):
    global outfull
    if whatform=="output=full"or whatform=="output=full\n":
        outfull=True
        nline[nline.index(whatform)]=None

    elif whatform=="output=key"or whatform=="output=key\n":
        outfull=False
        nline[nline.index(whatform)]=None
#parse input
def main():
    create_database()
    for line in sys.stdin:
        #first split the line into multiple segments, each line stored in nline
        nline = line.split(" ")
        for item in nline:
            handleform(item,nline)
        ncount=0
        while ncount<len(nline):
            if nline[ncount]==None:
                nline.remove(None)
            else:
                ncount=ncount+1
        print("command:",nline)
        
        #print(nline)
        newline = []
        for i in range(len(nline)):#for each element of nline, 
            #print(i)
            new = nline[i].replace("\n","")#get rid of \n at the end of the element
            nline[i] = new
            #print(nline)
            #reconstruct elements of nline such that phrases that should be one element is in one element
            if ":" in nline[i]:
                newline.append(nline[i])
            elif "<" in nline[i]:
                newline.append(nline[i])
            elif "=" in nline[i]:
                newline.append(nline[i])
            elif ">" in nline[i]:
                newline.append(nline[i])
            else:
                if newline:
                    lastIndex = len(newline)-1
                    #print(lastIndex)
                    newPhrase = newline[lastIndex]+' '+nline[i]
                    newline[lastIndex] = newPhrase
                else:
                    newline.append(nline[i])
                
        #parse newline
        print("element = ",newline)
        global result
        result = []
        get_data(newline)
main()

#cursor - set (key) dup - next dup
#first_record = cursor.set(key) return first pair with key : key 
#dup = curs_re.next_dup() return [key , value] same key different values 
#key value pair cursor.next()  string "2012""2013"
#while  dup:
    
    