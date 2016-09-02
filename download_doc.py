import threading, urllib
import Queue

urls_outfile = []
error = []

download_file = raw_input("Enter the CIK document containing the URL's you wish to download (ex. forms/year/QTR#_CIK_formtype.csv): ")
f = open(download_file, "r")

file_type = download_file.rsplit("_", 1)
file_type = file_type[1].strip(".csv")

lines = f.readlines()
f.close()

for line in lines:
        line.strip()
        sections = line.split(',')
        sections[3].strip('\n')
        query = "ftp://anonymous:pvr@gmail.com@ftp.sec.gov/" + sections[3]
        outfile = sections[0].replace(' ','_')
        outfile = outfile.replace('.','')
        outfile = outfile.replace('/','')
        outfile = outfile.replace('\\','')
        temp = download_file.split("/")
        out_path = temp[0] + "/" + temp[1] + "/" + file_type + "/" + outfile + ".txt"
        payload = query.strip() + "~" + out_path
        urls_outfile.append(payload)



def read_url(url_file, queue):
        url_file_mod = url_file.split("~")
        url = url_file_mod[0]
        url.strip()
        out = url_file_mod[1]
        try:
                data = urllib.urlopen(url).read()
                w = open(out, "w")
                w.write(data)
                w.close()
        except:
                error.append(url_file)

        #queue.put(data)


def fetch_parallel():
        result = Queue.Queue()
        threads = [threading.Thread(target=read_url, args = (url_file,result)) for url_file in urls_outfile]
        for t in threads:
                t.start()
        for t in threads:
                t.join()
        return result

fetch_parallel()

for urls in error:
        url_file_mod = urls.split("~")
        url = url_file_mod[0]
        url.strip()
        out = url_file_mod[1]
        try:
                data = urllib.urlopen(url).read()
                w = open(out, "w")
                w.write(data)
                w.close()
        except:
                error.append(url_file)
