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

This will create and start the network. After pinging all the hosts, mininet enters CLI mode.
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

> TODO:
> * Describe the meaning of iPerf command you used in detail

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**


2. **Example of Mininet**


3. **Topology Generator**


4. **Measurement**

---
## References

> TODO: 
> * Please add your references in the following

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

> TODO:
> * Please replace "YOUR_NAME" and "YOUR_GITHUB_LINK" into yours

* [YOUR_NAME](YOUR_GITHUB_LINK)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3