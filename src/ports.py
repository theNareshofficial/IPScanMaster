#!/usr/bin/env python

import socket
import sys
import time

ports = {
    20: "FTP-CLI",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "Microsoft RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "Microsoft-DS",
    465: "SMTPS",
    515: "LPD",
    520: "RIP",
    587: "SMTP (Submission)",
    631: "IPP (CUPS)",
    636: "LDAPS",
    873: "rsync",
    993: "IMAPS",
    995: "POP3S",
    1024: "Dynamic/Private",
    1080: "Socks Proxy",
    1194: "OpenVPN",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Monitor",
    1521: "Oracle",
    1701: "L2TP",
    1723: "PPTP",
    1883: "MQTT",
    2049: "NFS",
    2375: "Docker REST API",
    2376: "Docker REST API (TLS)",
    2483: "Oracle DB",
    2484: "Oracle DB (TLS)",
    3306: "MySQL",
    3389: "RDP",
    3690: "Subversion",
    4444: "Metasploit",
    4786: "Cisco Smart Install",
    5432: "PostgreSQL",
    5900: "VNC",
    5984: "CouchDB",
    6379: "Redis",
    6443: "Kubernetes API",
    6667: "IRC",
    8000: "HTTP-Alt",
    8008: "HTTP-Alt",
    8080: "HTTP-Proxy",
    8086: "InfluxDB",
    8181: "HTTP-Alt",
    8443: "HTTPS-Alt",
    8888: "HTTP-Alt",
    9000: "SonarQube",
    9092: "Kafka",
    9200: "Elasticsearch",
    9300: "Elasticsearch",
    11211: "Memcached",
    27017: "MongoDB",
    27018: "MongoDB",
    50000: "SAP",
    50070: "Hadoop",
    5672: "RabbitMQ",
    7000: "Couchbase",
    7200: "Hazelcast",
    8090: "Jenkins",
    8444: "Jenkins",
    9090: "Openfire",
    9999: "NMAP",
    10000: "Webmin",
    5044: "Logstash",
    5555: "Open Remote",
    15672: "RabbitMQ Management",
    5601: "Kibana",
}

def scan_ports(ip, verbose=True):
    print(f"Scanning common and advanced ports on {ip}...")

    open_ports = {}
    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.50)
        result = sock.connect_ex((ip, port))
        if verbose:
            print(f"\rChecking port's -> {port} ...", end="")
        if result == 0:
            open_ports[port] = service
        sock.close()
        sys.stdout.flush()
        time.sleep(0.01)
    
    if open_ports:
        print("\nScan complete. Open ports found:")
        for port, service in open_ports.items():
            print(f"Port {port} ({service})")
    else:
        print("\nScan complete. No open ports found among the common and advanced ports.")
    
    return open_ports

if __name__ == "__main__":
    scan_ports()
