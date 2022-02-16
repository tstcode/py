import re

urls = """
https://www.aceec.ac.in
ftp://archives.yahoo.com
https://www.usp.br
https://www.aceenggacademy.com
http://news.yahoo.com?date=today
"""
def get_url_pattern(url):
    return "Schema: %s - Host: %s - Path: %s - Querystring: %s" % (url[0], url[1], url[2], url[3])

pattern = re.compile("(ftp|http|https)://([\w\.]+)([\w\/]+)?([\?\w\/\=]+)?")
result = map(lambda uri: get_url_pattern(uri), pattern.findall(urls))
print("\r\n".join(result))
