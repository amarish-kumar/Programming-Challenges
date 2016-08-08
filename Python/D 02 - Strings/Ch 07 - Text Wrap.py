import textwrap

s = input ()
n = int (input ())

print ("\n".join (textwrap.wrap (s, n)))