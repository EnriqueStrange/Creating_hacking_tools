# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:01:46 2023

@author: Strange
"""

import socket
import threading

class PortScanner:
    def __init__(self, target, start_port, end_port, num_threads=10):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.num_threads = num_threads
        self.lock = threading.Lock()

    def scan_port(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((self.target, port))
            s.close()
            if result == 0:
                with self.lock:
                    print("Port", port, "is open")
            else:
                with self.lock:
                    print("Port", port, "is closed")
        except:
            pass

    def run_scan(self):
        for i in range(self.num_threads):
            thread = threading.Thread(target=self.scan_thread)
            thread.start()

    def scan_thread(self):
        while True:
            port = self.get_next_port()
            if port is None:
                break
            self.scan_port(port)

    def get_next_port(self):
        with self.lock:
            if self.start_port > self.end_port:
                return None
            else:
                port = self.start_port
                self.start_port += 1
                return port

target = input("Enter the IP address you want to scan: ")
start_port = 3546
end_port = 4563
num_threads = 10

scanner = PortScanner(target, start_port, end_port, num_threads)
scanner.run_scan()
