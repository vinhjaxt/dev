import os, re

def search(regex, text):
    searchRegex = re.compile(regex, re.I) # I: k phan biet chu hoa thuong
    result = searchRegex.findall()
    print(result)

while True:
    dirs = input('Nhap thu muc can xu ly: ')
    if os.path.exists(dirs) == True:
        print('OK')
        break
userSearch = input('Nhap Regexes:   ')

folder = os.listdir(dirs)

for file in folder:
    if file.endswith('.txt'):
        print(os.path.join(dirs, file))
        txtfile = open(os.path.join(dirs, file), 'r+')
        msg = txtfile.read()
        search(userSearch, msg)
