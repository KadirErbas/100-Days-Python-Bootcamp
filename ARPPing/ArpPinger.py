import argparse
import scapy.all as scapy


class ARPPing:

	def __init__(self):
		print("ArpPing worked")

	def get_user_input(self):
		# Initialize parser
		parser = argparse.ArgumentParser()

		# Adding optional argument
		parser.add_argument("-i", "--ipaddress", type=str, help="IP adresi girmelisini 192.168.1.0 şeklinde girmelisiniz")

		# Read arguments from command line
		args = parser.parse_args()

		if args.ipaddress:
			return args
		else:
			print("ip adresi, -i argümaniyla girmelisiniz")

	def arp_request(self, ip):
		ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=f"{ip}/24"), timeout=2)
		ans.summary(lambda s,r: r.sprintf("%Ether.src% %ARP.psrc%"))


if __name__ == "__main__":
	arp_ping = ARPPing()
	user_input = arp_ping.get_user_input()
	arp_ping.arp_request(user_input.ipaddress)