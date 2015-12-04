import re
filename = raw_input("Enter name of file: ")
source_file = open(filename, "r").read()
ignored_ips = ["127.0.0.1", "127.0.1.1"]
unique_visitors = []
count = 0
pattern = re.compile('(([0-9]{1,3}[\.]){3}[0-9]{1,3})')
matches = pattern.findall(source_file)
for match in matches:
    if match[0] not in ignored_ips and match[0] not in unique_visitors:
    	print match[0]
	unique_visitors.append(match[0])
	count += 1
print "Total unique IPs: "+str(count)
