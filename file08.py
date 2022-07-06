def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    ans = []
    for i in data:
        if i.isdigit():
            ans.append(int(i))
    return max(ans)

# Read data from file
f = open('txt_file/data08.txt','r')
data = f.read()
print(main(data))