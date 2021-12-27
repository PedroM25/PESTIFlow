import time
from multiprocessing.context import Process

from scapy.layers.inet import IP, TCP, UDP
from scapy.sendrecv import send

# Each method corresponds to one or more feature vectors in the output file.

def session1():
    """ Session #1 - This capture reflects the interaction between node 10.0.0.1 and 10.0.0.2. It is a normal
    interaction between the two where a connection is established and is then closed.
    TCP flags are set.
    Only one feature vector will result from this interaction.
    """
    send(IP(src="10.0.0.1", dst="10.0.0.2", tos=0b1) / TCP(sport=1, dport=2, flags="S"), iface="Ethernet")
    send(IP(src="10.0.0.2", dst="10.0.0.1") / TCP(sport=2, dport=1, flags="SA"), iface="Ethernet")
    send(IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=1, dport=2, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.2", dst="10.0.0.1") / TCP(sport=2, dport=1, flags="U"), iface="Ethernet")
    send(IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=1, dport=2, flags="F"), iface="Ethernet")
    send(IP(src="10.0.0.2", dst="10.0.0.1") / TCP(sport=2, dport=1, flags="AF"), iface="Ethernet")
    send(IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=1, dport=2, flags="A"), iface="Ethernet")


def session2():
    """ Session #2 - This capture reflects the interaction between node 10.0.0.1 and 10.0.0.4.
    It reflects a land attack where the src IP = dst IP and src port = dst port.
    Two feature vectors will result from this interaction.
    """
    send(IP(src="10.0.0.1", dst="10.0.0.4", tos=0b00000010) / UDP(sport=1, dport=4), iface="Ethernet")
    send(IP(src="10.0.0.4", dst="10.0.0.1") / UDP(sport=4, dport=1), iface="Ethernet")
    send(IP(src="10.0.0.1", dst="10.0.0.4") / UDP(sport=1, dport=4), iface="Ethernet")
    send(IP(src="10.0.0.4", dst="10.0.0.1") / UDP(sport=4, dport=1), iface="Ethernet")
    send(IP(src="10.0.0.1", dst="10.0.0.1") / UDP(sport=1, dport=1), iface="Ethernet")
    send(IP(src="25.0.0.1", dst="10.0.0.4") / UDP(sport=1, dport=4), iface="Ethernet")


def session3():
    """ Session #3 - This capture reflects the interaction between node 10.0.0.3 and 10.0.0.4.
    TCP flags are set.
    If the "--timeout" argument is set to 15s, this interaction should result in one feature vector.
    """
    send(IP(src="10.0.0.3", dst="10.0.0.4") / TCP(sport=3, dport=4, flags="S"), iface="Ethernet")
    send(IP(src="10.0.0.4", dst="10.0.0.3") / TCP(sport=4, dport=3, flags="SA"), iface="Ethernet")
    send(IP(src="10.0.0.3", dst="10.0.0.4") / TCP(sport=3, dport=4, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.4", dst="10.0.0.3") / TCP(sport=4, dport=3, flags="U"), iface="Ethernet")
    send(IP(src="10.0.0.3", dst="10.0.0.4") / TCP(sport=3, dport=4, flags="AP"), iface="Ethernet")
    time.sleep(10)
    send(IP(src="10.0.0.4", dst="10.0.0.3") / TCP(sport=4, dport=3, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.3", dst="10.0.0.4") / TCP(sport=3, dport=4, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.4", dst="10.0.0.3") / TCP(sport=4, dport=3, flags="A"), iface="Ethernet")
    time.sleep(10)
    send(IP(src="10.0.0.3", dst="10.0.0.4") / TCP(sport=3, dport=4, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.4", dst="10.0.0.3") / TCP(sport=4, dport=3, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.3", dst="10.0.0.4") / TCP(sport=3, dport=4, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.4", dst="10.0.0.3") / TCP(sport=4, dport=3, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.3", dst="10.0.0.4") / TCP(sport=3, dport=4, flags="R"), iface="Ethernet")


def session4():
    """ Session #4 - This capture reflects the interaction between node 10.0.0.5 and 10.0.0.6.
    TCP flags are set.
    If the "--timeout" argument is set to 15s, this interaction should result in two feature vector.
    """
    send(IP(src="10.0.0.5", dst="10.0.0.6") / TCP(sport=5, dport=6, flags="S"), iface="Ethernet")
    send(IP(src="10.0.0.6", dst="10.0.0.5") / TCP(sport=6, dport=5, flags="SA"), iface="Ethernet")
    send(IP(src="10.0.0.5", dst="10.0.0.6") / TCP(sport=5, dport=6, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.6", dst="10.0.0.5") / TCP(sport=6, dport=5, flags="APU"), iface="Ethernet")
    time.sleep(20)
    send(IP(src="10.0.0.5", dst="10.0.0.6") / TCP(sport=5, dport=6, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.6", dst="10.0.0.5") / TCP(sport=6, dport=5, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.5", dst="10.0.0.6") / TCP(sport=5, dport=6, flags="A"), iface="Ethernet")
    time.sleep(5)
    send(IP(src="10.0.0.6", dst="10.0.0.5") / TCP(sport=6, dport=5, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.5", dst="10.0.0.6") / TCP(sport=5, dport=6, flags="A"), iface="Ethernet")
    send(IP(src="10.0.0.6", dst="10.0.0.5") / TCP(sport=6, dport=5, flags="A"), iface="Ethernet")
    time.sleep(5)
    send(IP(src="10.0.0.5", dst="10.0.0.6") / TCP(sport=5, dport=6, flags="F"), iface="Ethernet")
    send(IP(src="10.0.0.6", dst="10.0.0.5") / TCP(sport=6, dport=5, flags="AF"), iface="Ethernet")
    send(IP(src="10.0.0.5", dst="10.0.0.6") / TCP(sport=5, dport=6, flags="A"), iface="Ethernet")


if __name__ == '__main__':
    p1 = Process(target=session1())
    p1.start()
    p2 = Process(target=session2())
    p2.start()
    p3 = Process(target=session3())
    p3.start()
    p4 = Process(target=session4())
    p4.start()