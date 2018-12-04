#!/usr/bin/python

#Import required libraries
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

#Used syntax based on recommended syntax in Introduction to Mininet GitHub Page



class Topo0 (Topo):
	def build(self):
		switch = []
		for i in range(9):
			switch.append(self.addSwitch('s'+string(i)))
	

#Create and test network

def Test():
	# Create topology based on topo0.png
	topo = Topo0()
	'''
	# Create network
	net = Mininet(topo)
	# Start network
	net.start()
	#Dump every hosts' and switches' connections
	print "Dumping host connections"
	dumpNodeConnections(net.hosts)
	print "Dumping switch connections"
	dumpNodeConnections(net.switches)
	print "Testing network connectivity"
	net.pingALL()
	#Don't stop, enter CLI mode
	CLI(net)
	'''
	
#Main

if __name__ == '__main__':
	#Tell mininet to print useful information
	setLogLevel('info')
	Test()
