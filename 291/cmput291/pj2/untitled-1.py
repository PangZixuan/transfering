# elif init == "a":
     #look for all the authors
     searchcom=(init+"-"+search_input)
     hi=str.encode(searchcom)
     printer=curs_te.set(hi)
     subword=printer[1].decode()
     reasult=full_res(subword)
     print(reasult)        
     
 elif init == "o":
     #look for all the others
     searchcom=(init+"-"+search_input)
     hi=str.encode(searchcom)
     printer=curs_te.set(hi)
     subword=printer[1].decode()
     reasult=full_res(subword)
     print(reasult)        