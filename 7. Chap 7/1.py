import re 

string1 = re.compile(r'^nap\s+tien\s+(.+?)(\s|$)')
text = string1.search('nap tien trinh em oi oi')
print(text.group(1))
