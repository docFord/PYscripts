# convert domains to their dns on the wire equivalent
# this is a function I use in other programs

a = ['domain.com', 'seconddomain.co.uk', 'bearkraken.com', 'tdalpacafarm.com', '123456789.co.uk', 'christinadudley.com']

pay = ""

print("\tDomains\n+----------------------+")
for domain in a:
	domain = domain.split('.')
	#print domain
	for item in domain:
		x = format(len(item), 'x')
		if len(x) == 1:
			newX = x.rjust(len(x) + len(x) % 2, '0')
			pay += "|{hex}|{domain}".format(hex=newX,domain=item)
		else:
			pay += "|{hex}|{domain}".format(hex=newX,domain=item)
    	pay += "|00|"
    	print(pay)
   	pay = ""
print("")

#CONVERTED TO A FUNCTION IS THE FOLLOWING
"""
def hexConvert(domain):
	pay = ""
	domain = domain.split('.')
	for item in domain:
		x = format(len(item), 'x')
		if len(x) == 1:
			newX = x.rjust(len(x) + len(x) % 2, '0')
			pay += "|{hex}|{domain}".format(hex=newX,domain=item)
		else:
			pay += "|{hex}|{domain}".format(hex=newX,domain=item)
    	pay += "|00|"
    	print(pay)
      #return pay
    
    #if using the hexConvert values we can return pay instead of printing it for use in our program



Example usage:
for domain in file:
    hexConvert(domain)
    
#if reusing the value from function

alertsid = 1000000
for domain in a:
    dnsDomain = hexConvert(domain)
    orig = domain
    print("alert dns $HOME_NET any -> $EXTERNAL_NET any (msg:\"test dns alert for {orig}\"; content:\"{domain}\"; alertsid:{alertsid}; rev:1;)").format(orig=orig,domain=dnsDomain,alertsid=alertsid)
    alertsid = alertsid + 1
"""




