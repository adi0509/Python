fout=open("out.csv","a")
# first file: 
for line in open("<full_path>/fit1.csv"):     
	fout.write(line) 
# now the rest:     
for num in range(2,25):     
	f = open("<full_path>/fit"+str(num)+".csv")     
	next(f) # skip the header 
        next(f) # skip the header    
	for line in f:          
		fout.write(line)     
	f.close() # not really needed 
fout.close()
