#!/usr/bin/python

#Import required libraries
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink


#Used syntax based on recommended syntax in Introduction to Mininet GitHub Page



class Topo0 (Topo):
	def build(self):
		switch = []
		host = []
		#Create hosts h1~h6
		for i in range(6):
			host.append(self.addHost('h%s'%(i+1)))
		#Create switches s1~s9
		for i in range(9):
			switch.append(self.addSwitch('s%s'%(i+1)))
		#Since all the links have different statistics, generate them manually
		#Python arrays start from 0, the index in array is one smaller than actual index
		#Example: host[0] is h1
		self.addLink( host[0], switch[0], bw=10, delay = '50us', loss = 12)	
		self.addLink( host[1], switch[1], bw=5, delay = '2ms', loss = 3)	
		self.addLink( host[2], switch[2], bw=7, delay = '63us', loss = 9)	
		self.addLink( host[3], switch[3], bw=12, delay = '40us', loss = 14)	
		self.addLink( host[4], switch[4], bw=15, delay = '30us', loss = 18)	
		self.addLink( host[5], switch[5], bw=3, delay = '5ms', loss = 2)	
		self.addLink( switch[0], switch[6], bw=23, delay = '1ms', loss = 8)	
		self.addLink( switch[1], switch[6], bw=18, delay = '2ms', loss = 9)	
		self.addLink( switch[2], switch[6], bw=15, delay = '3ms', loss = 5)	
		self.addLink( switch[3], switch[7], bw=19, delay = '80us', loss = 7)	
		self.addLink( switch[4], switch[7], bw=30, delay = '95us', loss = 2)	
		self.addLink( switch[5], switch[7], bw=20, delay = '60us', loss = 6)	
		self.addLink( switch[6], switch[8], bw=40, delay = '5ms', loss = 2)	
		self.addLink( switch[7], switch[8], bw=50, delay = '4ms', loss = 3)	
	

#Create and test network

def Test():
	# Create topology based on topo0.png
	topo = Topo0()
	# Create network, need to set TCLink as link to set loss
	net = Mininet(topo=topo,link = TCLink)
	# Start network
	net.start()
	#Dump every hosts' and switches' connections
	print "Dumping host connections"
	dumpNodeConnections(net.hosts)
	print "Dumping switch connections"
	dumpNodeConnections(net.switches)
	print "Testing network connectivity"
	net.pingAll()
	#Don't stop, enter CLI mode
	CLI(net)
	
#Main

if __name__ == '__main__':
	#Tell mininet to print useful information
	setLogLevel('info')
	Test()
