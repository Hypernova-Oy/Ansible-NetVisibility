# Ansible-NetVisibility
Ansible module for finding out the network information a given server and a client need to communicate.

Each server/LXC-container in our server environments can have multiple layers of visibility depending on the
network segments where the two parties reside.

Typically the visibility levels for a server IP are as follows:
- public  #Public internet
- intra   #Secured intranet
- local   #A local LXC container inside a LXC host
- socket  #Sharing a socket between multiple LXC containers via a bind mount

This module calculates the network information needed to connect from one device to the other via whatever
network segments they are in.

