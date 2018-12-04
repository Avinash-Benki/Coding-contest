#This prorgram is providing the Service availability for the areas: Bangalore, Chennai, Hyderabad, Mumbai, Delhi 
dict={560001:"Bangalore",600003:"Chennai",500003:"Hyderabad",400001:"Mumbai",110012:"Delhi"}
pincode=input("Enter the pin code : ")

print("Entered pincode is:\t"+str(pincode))
number_of_digits=len(str(pincode))

while number_of_digits!=6:
	print("Invalid length of pincode....")
	pincode=input("Enter the 6 digit pin-code here")
	print("Entered pincode is:\t"+str(pincode))
	number_of_digits=len(str(pincode))

if pincode in dict.keys():
	print"Service available for the locality:",dict.get(pincode)
else:
	print"No Service available for the locality:",pincode
