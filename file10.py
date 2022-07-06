def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    arr_1 = []
    arr = data.split('\n')
    for i in arr:
        arr_1.append(len(i))
    return max(arr_1)

# Read data from file
f = open('txt_file/data10.txt','r')
data = f.read()
print(main(data))