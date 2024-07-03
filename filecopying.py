
# Copy a file
# OS Module - popen() system() 
import os
os.chdir(r"C:\Users\shree")
os.popen('copy Employee Salries.txt MyTest.txt')
os.system('copy MyTest.txt Shreeya.txt')
