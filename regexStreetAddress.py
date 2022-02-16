import re

def get_complete_address(data):
    return "\r\nAddress: %s - Number: %s - City: %s - State: %s" % (data[0], data[1], data[2], data[3])

addresses = """
ACE Engineering College, 999 - Ankushapur - Hy
ACE Academy, 8266 - Abids - TS
"""
pattern = re.compile("([\w\s]+),\s{1}([0-9]+)\s-\s([\w\s]+)\s-\s([a-zA-Z]{2})")
result = map(lambda address: get_complete_address(address), pattern.findall(addresses))
print("******************")
print("*   ADDRESSES    *")
print("******************")
print("\r\n".join(result))
