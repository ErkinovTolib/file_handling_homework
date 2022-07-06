def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    c = 0
    c_n = 0
    l = [c,c_n]
    for i in data:
        if i.isdigit():
            c+=1
        elif not(i.isdigit()):
            c_n += 1
        l = [c,c_n]
    return l
    
# Read data from file
file = open('txt_file/data05.txt','r')
data = file.read()
print(main(data))