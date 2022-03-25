## BEGIN Work ticket 2 Veronica Dean (3/23/2022) here

#Define a recursive function print_range with parameters start and end

def print_range(start,end):
	if start == end:
		print(start)
#Count recursively from start to end
	else:
		if start<end:
			print(start)
			print_range(start+1,end)
		else:
			print(end)
			print_range(start,end+1)

#Gather input from user
			
start = int(input("Enter which number you would like to start with: "))
end = int(input("Enter which number you would like to end with: "))

#Print the result
print_range(start,end)


## END Work ticket 2 Veronica Dean (3/24/2022) here
## HALF-LIFE / Ron Bass / John Richards Sr. / After-Burner Elite 
