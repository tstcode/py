import re
names = """
Prof K Jayabharathi
Dr G Sreenivasulu
Dr P VenkateswaraRao
Dr P Chiranjeevi
"""
def get_complete_name(name):
    complete_name = name.split(" ")
    return "First: %s - Last: %s" % (complete_name[0], complete_name[1])
pattern = re.compile("[a-zA-Z]+\s[a-zA-Z]+\n")
result = map(lambda x: get_complete_name(x), pattern.findall(names))
print("******************")
print("*     NAMES      *")
print("******************")
print("\r".join(result))
