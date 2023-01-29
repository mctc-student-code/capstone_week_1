file_name = 'hello.txt'

try:
    """ classic way
    data_file = open(file_name) 
    contents = data_file.read() # what if the content is so big that the computer memory can't manage, throws an exception
    print(contents)
    data_file.close()
    """
    # context version - closes the file automatically using the with context version
    with open(file_name) as data_file:
        contents = data_file.read()
        print(contents)
    
except FileNotFoundError as fnf:
    print(f'Sorry, {file_name} file not found.')