import sys
import algorithm

#Get the necessary page name from the arguments
page = str.join(' ', sys.argv[1:])

#Run the program
algorithm.run(page)