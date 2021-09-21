'''
6B. Write a Python program to append text to a file and display the text.
'''
def main():
    f=open("test.txt","a+")
    f.write("\nPython is awesome\n")
    f.close()
main()

