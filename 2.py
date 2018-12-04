# Automation program for customer and sales manager
number_of_products=input("Enter the number of products :")

list_of_products=[]
sortedlist=[]
print "Enter the product names"

for i in range(number_of_products):
	newproduct=raw_input("- ")
	list_of_products.append(newproduct)



for i in range(number_of_products):
	list_of_products[i]=list_of_products[i].upper()

while list_of_products:
	smallest=min(list_of_products)
	sortedlist.append(smallest)
	list_of_products.pop(list_of_products.index(smallest))

print "The products in Alphabetical Order are as follow: "

for i in range(number_of_products):
	print i+1,sortedlist[i]
