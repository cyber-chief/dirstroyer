#!/usr/bin/python
import sys
import getopt
import requests
import concurrent.futures

wordlist = ''
outputFile = ''
threads = 10
URL = ''
codes= [200,301,403,302]
results = []

def main(argv):
    global wordlist
    global outputFile
    global threads
    global URL
    global codes
    
    try:
        opts,args = getopt.getopt(argv, "hw:o:t:u:sC:", ["wordlist=", "outputfile=", "threads=","url=", "statuscodes="])
    except getopt.GetoptError:
        print 'dirstroyer.py -u <url> -o <output file> '
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print 'dirstroyer.py -u <url> -o <output file> '
        elif opt in ('-w', "--wordlist"):
            wordlist = arg
        elif opt in ("-u", "--url"):
            URL = arg
        elif opt in ("-t", "--threads"):
            threads = arg
        elif opt in ("-o", "--outfile"):
            outputFile = arg
        elif opt in ("-sC", "--statuscodes"):
            codes = arg
    if len(argv) == 0:
        print 'dirstroyer.py -u <url> -o <output file> '
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future = executor.submit(dirstroy)
        future.result()
    
def dirstroy():
    results = []
    if wordlist == '':
        print "please set wordlist"
        sys.exit(2)
    elif URL == '':
        print "please set URL"
        sys.exit(2)
        if not url.contains("http://") or not url.contains("https://"):
            print "Malformed URL. Please enter http(s)://$url"
            sys.exit(2)
    f = open(wordlist, "r")
    if not outputFile == '':
        out = open(outputFile, "a")
    dirs = f.read().splitlines()
    print dirs
    for direct in dirs:
        req = requests.get(url=URL+ "/" + direct, verify=False)
        if req.status_code in codes:
            results.append("/" + direct)
            print "/"+ direct + " " + str(req.status_code)
            if not outputFile == '':
                out.write("/"+ direct + " " + str(req.status_code) + '\r\n')
            
if __name__ == '__main__':
    main(sys.argv[1:])
