urls=[
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "http://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]
count_a=0;
count_b=0;
count_c=0;
for i in urls:
    a=i.split('/')
    
    for k in a:
        if k=="a.txt":
            count_a+=1;
        elif k=="b.txt":
            count_b+=1;
        elif k=="c.jpg":
            count_c+=1;
   
            
print "a.txt"+str(count_a)
print "b.txt"+str(count_b)
print "c.jpg"+str(count_c)