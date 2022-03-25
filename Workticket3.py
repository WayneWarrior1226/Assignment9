## BEGIN Work ticket 3 Veronica Dean (3/24/2022) here
#Find the GCD of two numbers is Euclid's algorithm. 

#Create a recursive function called gcd that takes parameters a and b and
#returns the greatest common divisor asumming both a and b are positive. 
def gcd(a, b):

        if b > a:
                return gcd(b, a)
        if a % b == 0:
                return b

        return gcd(b, a % b)

#Print the gcd for integer pairs 12,8 and 20,24

print(gcd(12,8))
print(gcd(20,24))

## END Work ticket 2 Veronica Dean (3/24/2022) here
## HALF-LIFE /  Bass / John Richards Sr. / After-Burner Elite 
