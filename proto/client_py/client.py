from http import client
import socket
from queue import Queue
import json
from pattern_py.pattern import Pattern
import datetime

class Client:

    """
    The size of the packet
    Completely arbitrary
    # TODO(3)
    """
    _PACKET_SIZE: int = 2048

    """
    Used to tell when whether a member is a client or a server,
    in a served patter
    """
    _ROLE: str = "client"

    """
    The port number of the protocol
    Completely arbitrary
    # TODO(8)
    """
    _PORT = 4761

    """
    The IP address of the client
    """
    _ip_address: str = ""

    """
    Used to store saved and validated patterns
    """
    _patterns: dict[str, Pattern] = {}
    """
    Used to determine whether the client has a served pattern.
    When the connect() method is called,
    it firsts assetrs whether this is True
    """
    _has_served_pattern: bool = False

    """
    The networking socket of the client
    """
    _sock: socket.socket

    """
    Used to keep track of know members and their patterns
    Invalidate after TODO(1) minutes for now let's say 1
    For now IP: timestamp
    # TODO(9)
    """
    _validated_members: dict[str, datetime.datetime] = {}


    @staticmethod
    def is_ip_valid(ip: str) -> bool:
        for i in ip.split("."):
            if 0 > int(i) > 255:
                return False

        return True

    def __init__(self) -> None:
        return None

    def add_ip(self, ip: str) -> bool:
        
        if Client.is_ip_valid(ip):
            self._ip_address = ip
            return True

        return False

    def add_pattern(self, pattern: Pattern) -> bool:
        """
        Is used to add different patters,
        according to which the members can communicate.
        """

        # TODO(5)
        if pattern.is_valid(self._PACKET_SIZE):
            self._patterns[pattern.name] = pattern
            return True

        return False

    def remove_pattern(self, ) -> None:
        ...

    def send_data(self, data: dict, recipient_ip: str) -> dict:
        if self._ip_address:
            if self._is_data_valid(data):
                if self._is_recipient_valid(data,recipient_ip):
                    self._sock.sendto(self._serialize_data(data), recipient_ip)

                    return self._un_serialize_data(
                        self._sock.recvfrom(self._PACKET_SIZE)[0]
                    )

                return {"Error": "The recipient is invalid"}
            return {"Error": "Data to be sent is invalid"}
        return {"Error": "This client has no IP"}


    def _is_data_valid(self, data: dict) -> dict:
        ...

    def _is_recipient_valid(self, data: dict, recipient_ip: str) -> bool:
        ...

    # TODO(4)
    def _serialize_data(self, data: dict[str, str]) -> bytes:

        result: bytes = b""

        for field in data:
            result += b"01" + field.encode() + b"02" + data[field].encode()

        # TODO(2) maybe unnecassary
        result += b"03"

        return result

    def _un_serialize_data(self, data: bytes) -> dict:
        
        result: dict[str, str] = {}

        # TODO(2) maybe unnecassary '.rstrip(b"03")'
        for field in data.rstrip(b"03").split(b"01")[1:]:
            result[
                field.split(b"02")[0].decode()
            ] = field.split(b"02")[1].decode()            

        return result

    def connect(self, remote_ip: str) -> bool:

        if self._has_served_pattern:
            return self._connect(remote_ip)

        print("There are no valid served patterns")
        return False

    def _connect(self, remote_ip: str) -> bool:
        ...

    def _disconnect(self, remote_ip: str) -> bool:
        ...
    
if __name__ == "__main__":

    client = Client();

    data = {"fero":"fero","jožo":"jožo"}
    print(data)
    data = client._serialize_data(data)
    print(data)
    data = client._un_serialize_data(data)
    print(data)
