def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l = len(data)
    return l
# Read data from file
f = open('txt_file/data02.txt','r')
data = f.read()
print(main(data))