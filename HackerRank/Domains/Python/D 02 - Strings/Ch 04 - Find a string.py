import re

string = input ()
substring = input ()
pattern = "(?=%s)" % substring

print (len (re.findall (pattern, string)))