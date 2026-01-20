import math  

def main():
    A = int(input("Enter the first term: "))#TO DO
    B = int(input("Enter the second term: "))
    
    
    pythag(A,B)
def pythag(A,B):
    added = A**2 + B**2
    output = math.sqrt(added)
    print(output)
main()
