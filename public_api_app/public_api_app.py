import requests


def fetch_data(fetch_url, todo_id):
	try:
		isinstance(int(todo_id), int)
		if int(todo_id) <= 200 and int(todo_id) > 0:
			response = requests.get(fetch_url + todo_id)
			return response
		else:
			print("Please enter a To-do with ID between 1 and 200")
	except ValueError as e:
		raise(e)
	return "no data"

def main():
	print("\n\t|   Python HTTP Command line Application  |\n\t%s\n" %("-"*44))
	print("This command line application fetches data from 'jsonplaceholder.typicode.com', a \nfree online REST service that you can use whenever you need some fake data.\n\n")

	url = "https://jsonplaceholder.typicode.com/todos/"

	post_id = raw_input("Enter a To-do with ID between 1 and 200: ")
	print("\n\tGetting To-do List with ID number "+post_id + "\n")
	get_r = fetch_data(url,post_id)
	print("\tTo-do List Details\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n" % 
		("-"*17,get_r.text, "-"*11, get_r.status_code))

if __name__ == '__main__':
	main()