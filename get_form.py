import urllib

year = str(raw_input("Enter the year you wish to access: "))
qtr = "QTR" + str(raw_input("Enter the QTR you wish to access: "))
query = "ftp://anonymous:pvr@gmail.com@ftp.sec.gov/edgar/full-index/" + year + "/" + qtr + "/form.idx"
location = "./forms/" + year + "/" + qtr + "form.txt"
#urllib.urlretrieve(query, location)
print "Stored raw data to " + location

#New Bash implementation call
in_file="./forms/" + year + "/" + qtr + "form.txt"
out_file="./forms/" + year + "/" + qtr + "_form.txt"
print "infile: " + in_file 
print "outfile: " + out_file


#Section depricated because of new bash implementation (extract type)
f = open("./forms/" + year + "/" + qtr + "form.txt", "r")
lines = f.readlines()
f.close()

f = open("./forms/" + year + "/" + qtr + "_form.txt", "w")
for line in lines:
        if "10-K" in line:
                f.write(line)
f.close()
