def ListToStr(row_list):
    op = ''
    for i in range(len(row_list)):
        if i != (len(row_list) - 1):
            op += str(row_list[i]) + ','
        else:
            op += 'and ' + str(row_list[i]) 
    return op
if __name__ == "__main__":
    row_list = ['apples','banana', 'tofu', 'cats']
    print(ListToStr(row_list))