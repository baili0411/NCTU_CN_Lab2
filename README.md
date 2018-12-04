# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

To execute the program, run 
>`/Network_Topology/src/topology.py`

This will create and start the network. 
(0616020) % 3 is 0.
The created network is based on topo0.png.

After pinging all the hosts, mininet enters CLI mode.
We can then execute the iPerf command.
The result is shown in the following picture.
![The result after running iPerf](iPerf_result.png)

---
## Description

### Mininet API in Python

>`from mininet.topo import Topo`  
>`from mininet.net import Mininet`    
>`from mininet.util import dumpNodeConnections`  
>`from mininet.log import setLogLevel`  
>`from mininet.cli import CLI`  
>`from mininet.link import TCLink`  

Importing the required libraries from the Mininet API.

>`setLogLevel('info')`

Set Mininet's default output level. We use info since it provides useful information

>`class Topo0 (Topo):`  
>`def build(self):`  
>`...`

Topo 0 inherits from Mininet's Topo class, and override the build() function to define our own build function.

>`self.addHost('h%s'%(i+1))`

Create a host in the topology, using the string in the brackets as the name.  
'h%s'%(i+1) is Python's string formating, substituting %s with i+1

>`self.addSwitch('s%s'%(i+1)`

Create a switch in the topology, using the string in the brackets as the name.  
's%s'%(i+1) is Python's string formating, substituting %s with i+1

>`self.addLink( host[0], switch[0], bw=10, delay = '50us', loss = 12)`

Create a bidirectional link in the topology.  
The first two parameters are the two nodes we want to link together.  
The bw parameter is an integer that represents the bandwidth in Mbps.  
The delay paramter is a string that represents the delay with units.
The loss paramter is an integer that represents the loss percentage.

>`Mininet(topo=topo,link = TCLink)`

Create a Mininet network emulation object, using the topology defined in object "topo".  
The link type is set to TCLink to allow the limitations set in addLink().

>`net.start()`

Start the "net" network emulation.

>`dumpNodeConnections(net.hosts)`
>`dumpNodeConnections(net.switches)`

Dump the connections from the nodes specified in the brackets.

>`net.pingAll()`

Test connectivity by having all the nodes ping each other.

>`CLI(net)`

Invoke Mininet's CLI(command line interface) mode, with the network emulation being "net".

### iPerf Commands

>`h2 iperf -s -u -i 1 > ./out/result &`

Run iPerf on h2 with arguments -s -u -i 1, then write the output to file /Network_Topology/out/result instead of stdout(the terminal)( > ./out/result ).  
The & at the end means that iperf will run in the background.  
iperf -s -u -i 1 means that we run iPerf in server mode( -s ), the connection type is UDP( -u ), and a report about the bandwidth, jitter, and loss is made every second( -i 1 ).  

>`h6 iperf -c 10.0.0.2 -u –i 1`  

Run iPerf on h6 with arguments -c 10.0.0.2 -u -i 1.  
This one isn't executed in the background, and the output we see in the terminal is this part.  
iperf -c 10.0.0.2 -u -i 1 means that we run iPerf as a client and connect to 10.0.0.2( -c 10.0.0.2 ), using UDP ( -u ), and a report about the bandwidth, jitter, and loss is made every second( -i 1 ).  


### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**


2. **Example of Mininet**


3. **Topology Generator**


4. **Measurement**

---
## References


* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)

---
## Contributors

* [Baili Deng](https://github.com/baili0411)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3