def open_file(file_name): # Do not change this line
    '''Opens the given filename and returns its file object, or None if not found'''
    try:
        file_object = open(file_name, 'r')
        return file_object
    except FileNotFoundError:
        print("File not found")
        return None

def read_matrix(file_object): # Do not change this line
    '''Creates an n-by-n integer matrix by reading data from file_object. 
    The matrix is a list of lists.'''
    matrix=[]
    for line in file_object:
        line=line.strip().split()
        #breytum öllu bara í int strax
        for i in range(0,len(line)):
            line[i]=int(line[i])
        matrix.append(line)
    return matrix


def row_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    sum=[]
    for row in matrix:
        sum_row=0
        for num in row:
            sum_row+=num
        sum.append(sum_row)
    #ef ég breyti listanum í set og allt er eins þá ætti hann að vera með lengd 1
    if len(set(sum))==1:
        return sum[0]
    else:
        return 0
def col_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    sum_list=[]
    for i in range(0, len(matrix[1])):
        sum=0
        for row in matrix:
            sum+=row[i]
        sum_list.append(sum)
    if len(set(sum_list))==1:
        return sum_list[0]
    else:
        return 0

def printmatrix(matrix):
    #passa uppá strengi og int
    for row in matrix:
        for i in range(0, len(row)-1):
            print(str(row[i])+"\t", end="")
        print(str(row[-1])+"\t")



def main(): # Do not change this line
    file_name=input("File name: ")
    file_object=open_file(file_name)
    #Ég vil bara halda áfram ef það er einhver fæll
    if file_object!=None:
        matrix=read_matrix(file_object)
        printmatrix(matrix)
        if col_sum_same(matrix) and row_sum_same(matrix):
            print("Same sums")
        else:
            print("Not same sums")
  

# Main program starts here. Do not change it.
if __name__ == "__main__":
    main()