import os
import sys
from bsddb3 import db

def search_all(search_input):
    pass
def search_terms(search_input,init):
    if init == "t":
        #look for all the titles
        pass
    elif init == "a":
        #look for all the authors
        pass
    elif init == "o":
        #look for all the others
        pass
def search_years(search_input,sign):
    if sign == "<":
        #search for all years below
        pass
    elif sign == ":":
        #search for all years equal
        pass
    elif sign == ">":
        #search for all years above
        pass
def get_data(newline):
    #this function processes all commands inputed in one line
    outFlag = []
    for element in newline:
        if ":" in element:
            element_parsed = element.split(":")
            #print(element_parsed)
        elif "<" in element:
            element_parsed = element.split("<")
            #print(element_parsed)
        elif "output" in element:
            outFlag.append(element)
        #elif "=" in element:
            #element_parsed = element.split("=")
            ##print(element_parsed)
        elif ">" in element:
            element_parsed = element.split(">")
            #print(element_parsed)
        else:
            element_parsed = element.split(" ")
            element_parsed.append("wholeWord")#this subelement has a flag as its last element which indicates that it is a whole word
        if outFlag:
            #check the last output flag, outFlag[1] == full, print all data, elif output[1] == key, print record key
            outFlag = outFlag[len(outFlag)-1] .split("=")
            print(outFlag)
        #subword = "subelements are"+"\n"+(",".join(element_parsed))+"\n"
        #sys.stdout.write(subword)
        else:
            print("subelements are:",element_parsed)
        
        
        if element_parsed[len(element_parsed)-1] == "wholeWord":
            #delete the flag
            del element_parsed[len(element_parsed)-1]
            #process the whole word
            search_all(element_parsed)
        else:
            criteria = subelement[0]
            if criteria == "title":
                search_terms(element_parsed[1],"t")    
            elif criteria == "author":
                search_terms(element_parsed[1],"a")
            elif criteria == "other":
                search_terms(element_parsed[1],"o")
            elif criteria == "year":
                if "<" in element:
                    search_years(element_parsed[1],"<")
                elif ":" in element:
                    search_years(element_parsed[1],":")
                elif ">" in element:
                    search_years(element_parsed[1],">")
   

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
    

#parse input
def main():
    create_database()
    for line in sys.stdin:
        #first split the line into multiple segments, each line stored in nline
        nline = line.split(" ")
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