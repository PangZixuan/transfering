import os
#create three
os.system("sort years.txt -u -o years.txt")
os.system("perl break.pl <years.txt>y1.txt")
os.system("sort terms.txt -u -o terms.txt")
os.system("perl break.pl <terms.txt>t1.txt")
os.system("sort recs.txt -u -o recs.txt")
os.system("perl break.pl <recs.txt>r1.txt")

#create index
os.system("db_load -T -t hash -f r1.txt -c duplicates=1 re.idx")
os.system("db_load -T -t btree -f t1.txt -c duplicates=1 te.idx")
os.system("db_load -T -t btree -f y1.txt -c duplicates=1 ye.idx")