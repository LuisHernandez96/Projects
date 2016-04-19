#Luis Fernando Hernandez Sanchez A00815356

from scapy.all import *
global iCont
global askdIP
global vctmIP
global vctmMAC
iCont=0
askdIP=" "
vctmIP=" "
vctmMAC=" "

def arp_display(pkt):
	global iCont
	global askdIP
	global vctmIP
	global vctmMAC
	if pkt[ARP].op == 1: #who-has (request)		
		iCont=0
		askdIP= pkt[ARP].pdst
		vctmIP= pkt[ARP].psrc
		vctmMAC= pkt[ARP].hwsrc
	if pkt[ARP].op == 2: #is-at (response)
		iCont=iCont+1
		if iCont > 3:
			if askdIP==pkt[ARP].psrc:
				return "IP: " + vctmIP + " MAC: " + vctmMAC + " is under attack, " + pkt[ARP].psrc + " is being duplicated by " + pkt[ARP].hwsrc
			else:
				return pkt[ARP].psrc + " is being duplicated by " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=999)
