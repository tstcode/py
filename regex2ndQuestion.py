import re

str = '''
Mr. Akhil logged in at Mon, 19 Jan 2019 07:50:17 GMT from qw65j@gmail.com
Mr. Ankit logged in at Sun, 20 Oct 2020 08:20:27 GMT from abcef.123@gmail.com
Mr. Ravi logged in at Fri, 10 Aug 2021 02:50:47 GMT from pqr@gmail.com
Mr. Younus logged in at Tue, 21 Feb 2007 09:10:17 GMT from asdf@gmail.com
'''

#timestamp
timestamp = re.compile("\w{3}, \d{1,2} \w{3} \d{4} \d{2}:\d{2}:\d{2} \w{3}")
matcher = timestamp.findall(str)
for i in matcher:
    print(i)
    
print('\n')

#email
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", str)
for i in emails:
    print(i)
 

print('\n')

#Months
months = re.compile("\w{3}, \d{1,2} (\w{3}) (\d{4}) (\d{2}:\d{2}:\d{2}) \w{3}")
matcher = months.findall(str)
for i in matcher:
    print(i[0])
    
    
print('\n')

#Years
years = re.compile("\w{3}, \d{1,2} (\w{3}) (\d{4}) (\d{2}:\d{2}:\d{2}) \w{3}")
matcher = years.findall(str)
for i in matcher:
    print(i[1])

    
print('\n')

#Time
time = re.compile("\w{3}, \d{1,2} (\w{3}) (\d{4}) (\d{2}:\d{2}:\d{2}) \w{3}")
matcher = time.findall(str)
for i in matcher:
    print(i[2])



