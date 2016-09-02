import re

year = raw_input("Enter the year of the file you wish to access(ex. 2015): ")
qtr = raw_input("Enter the quarter you wish to access (ex. 4): ")
filetype = raw_input("Enter the type of file you would like to extract (ex. 10-K): ")
#if "/" in filetype:
#       temp = filetype.split("/")
#       filetype = temp[0] + "\/" + temp[1]
#       print filetype

path = "./forms/" + str(year)
filename = "/QTR" + str(qtr) + "form.idx"
infile = path + filename
outfile = path + "/QTR" + str(qtr) + "_CIK_" + filetype + ".csv"
print outfile

f = open(infile, "r")
lines = f.readlines()

w = open(outfile, "w")
w.write("Company Name, CIK, Date Filed, Location\n")

for line in lines:
        line.strip()
        line = line.replace(",", "")
        sections = re.split(r'\s{2,}', line)
        if sections[0] == filetype:
                for i in range(1,5):
                        w.write(sections[i])
                        if i != 4:
                                w.write(",")
                w.write("\n")
'''
        query = "ftp://anonymous:pvr@gmail.com@ftp.sec.gov/" + sections[4]
        path = sections[1].replace(' ','_')
        path = path.replace('.','')
        path = path.replace('/','')
        path = path.replace('\\','')
        location = "./forms/2015/10-K/" + path + ".txt"
        urllib.urlcleanup()
#       urllib.urlretrieve(query, location)
        try:
                infile = urllib.urlopen(query)
        except:
                print "failed when opening " + query
        text = infile.read()
        print location
        i = open(location, "w")
        i.write(text)
        i.close()
'''
