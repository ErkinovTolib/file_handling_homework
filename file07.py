def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    for i in data:
        l = len(data)
    ans = [l]
    
    return ans 
# Read data from file
f = open('txt_file/data06.txt')
data = f.read()
print(main(data))