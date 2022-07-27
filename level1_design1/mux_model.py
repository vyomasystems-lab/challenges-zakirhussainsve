# python program to implement multiplexer
# Function to print output
def Multiplexer(I,s):
	#decimal value of s
	d= (s[0] * 16) + (s[1] * 8) + (s[2] * 4) + (s[3] * 2) + (s[4] * 1)
	# getting the output of decimal value from inputs
	return b = I[d]
	