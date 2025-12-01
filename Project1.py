#!/usr/bin/python3

from argparse import ArgumentParser
import socket
from threading import Thread
from time import time

open_ports = []

def prepare_args():
    """ prepare arguments

        return:
            args(argparse.Namespace)
    """
    parser = ArgumentParser(
        description="Python Based Fast Port Scanner",
        usage="%(prog)s 192.168.1.2",
        epilog="Example - %(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.2 "
    )
    parser.add_argument(metavar="IPv4", dest="ip", help="host to scan")
    parser.add_argument("-s", "--start", dest="start", metavar="\b", type=int, help="starting port", default=1)
    parser.add_argument("-e", "--end", dest="end", metavar="\b", type=int, help="ending port", default=65535)
    parser.add_argument("-t", "--threads", dest="threads", metavar="\b", type=int, help="threads to use", default=500)
    parser.add_argument("-V", "--verbose", dest="verbose", action="store_true", help="verbose output")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0", help="display version")
    args = parser.parse_args()
    return args

def prepare_ports(start: int, end: int):
    """generator function for ports"""
    for port in range(start, end + 1):
        yield port

def scan_port():
    """scan ports"""
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.settimeout(0.2)

            port = next(ports)

            try:
                s.connect((arguments.ip, port))
                open_ports.append(port)
                if arguments.verbose:
                    print(f"Open: {port}")
            except (ConnectionRefusedError, socket.timeout, PermissionError, OSError):
                pass  # ignore blocked or closed ports

        except StopIteration:
            break

        finally:
            s.close()


def prepare_threads(threads: int):
    """create, start, join threads"""
    thread_list = []
    for _ in range(threads + 1):
        thread_list.append(Thread(target=scan_port))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    arguments = prepare_args()
    ports = prepare_ports(arguments.start, arguments.end)
    start_time = time()
    prepare_threads(arguments.threads)
    end_time = time()

    if arguments.verbose:
        print()

    print(f"Open Ports Found - {open_ports}")
    print(f"Time Taken - {round(end_time - start_time, 2)}")
