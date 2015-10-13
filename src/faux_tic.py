#!/usr/bin/env python

# Generate a UDP datagram embedding TIC data

import socket
import json


class TicData:

    parameters = {
        "ADCO", "OPTARIF", "ISOUSC", "BASE", "IINST",
        "ADPS", "IMAX", "PAPP", "MOTDETAT"}

    def __init__(self):
        self.parameters = {}
        for param in TicData.parameters:
            self.parameters[param] = param

    def setParameter(self, parameter, value):
        if parameter not in TicData.parameters:
            raise ValueError
        self.parameters[parameter] = value

    def dumps(self):
        """Get a JSON string representation."""
        return json.dumps(self.parameters)


class McastDatagram:

    def __init__(self, ip_dst, port):
        self.ip_dst = ip_dst
        self.port = port

    def loadData(self, data):
        self.data = data

    def send(self):
        """Sends a single UDP broadcast datagram."""
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(self.data, (self.ip_dst, self.port))


def main():
    tic = TicData()
    tic.setParameter("ADCO", "M09-3390-V16")
    print(tic.dumps())

    dg = McastDatagram("192.168.1.255", 4242)
    dg.loadData(tic.dumps())
    dg.send()


if __name__ == '__main__':
    main()
