import html_parser

#Method that loops through all the first links until it reaches Philosophy and prints out each page on it's path
def run(page):

	#Initialize the page counter
	counter = 0

	#Initialize the initial parameters for the get_first_link function
	url = ''
	is_page = True
	link_set = html_parser.get_first_link(url, page, is_page)

	#Boolean variable that checks if we reached philosophy
	reached = str.lower(link_set[0]) == 'philosophy'

	#If the first page is not Philosophy, print the first page's name
	if reached == False:
		print(page)

	#Loops through the links until philosophy is reached
	while reached == False:

		#Increase the page counter
		counter += 1

		#Print the current page
		print(link_set[0])

		#Set the new parameters
		url = link_set[1]
		is_page = False
		link_set = html_parser.get_first_link(url, page, is_page)
		reached = str.lower(link_set[0]) == 'philosophy'

		#Finish off the program by printing the last page (philosophy) and how many steps were needed to arrive at it
		if reached:
			counter += 1
			print('philosophy')
			print('We reached philosophy in ' + str(counter) + ' steps.')