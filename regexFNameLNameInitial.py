import re


def get_complete_name(name):
    return "First: %s - Last: %s" % (name[1], name[0])
  
  
names = """
Prof K, Jayabharathi
Dr G, Sreenivasulu
Dr P, VenkateswaraRao
Dr P, Chiranjeevi
"""
pattern = re.compile("([a-zA-Z]+),\s+([a-zA-Z]+)")
print("******************")
print("*     NAMES      *")
print("******************")
result = map(lambda name: get_complete_name(name), pattern.findall(names))
print("\r\n".join(result))
