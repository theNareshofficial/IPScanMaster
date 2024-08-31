#!/usr/bin/env python3

import socket
import time
import sys
from tools.color import *
from src.sublister import *

ports = {

    1: "tcpmux",
    9: "Discard",
    15: "netstat",
    20: "FTP-CLI",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    26: "rsftp",
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
    554: "RTSP (Real-Time Streaming)",
    587: "SMTP (Submission)",
    631: "IPP (CUPS)",
    636: "LDAPS",
    873: "rsync",
    990: "FTPS",
    993: "IMAPS",
    995: "POP3S",
    1024: "Dynamic/Private",
    1080: "Socks Proxy",
    1194: "OpenVPN",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Monitor",
    1521: "Oracle DB",
    1701: "L2TP",
    1723: "PPTP",
    1883: "MQTT",
    2000: "Cisco-sccp",
    2049: "NFS",
    2222: "EtherNetIP-1",
    2375: "Docker REST API",
    2376: "Docker REST API (TLS)",
    2483: "Oracle DB",
    2484: "Oracle DB (TLS)",
    3000: "Grafana",
    3306: "MySQL",
    3389: "RDP",
    3690: "Subversion",
    4373: "Remote Authenticated Command",
    4443: "HTTPS-Alt",
    4444: "Metasploit",
    4567: "MySQL Group Replication",
    4786: "Cisco Smart Install",
    5060: "SIP",
    5432: "PostgreSQL",
    5672: "RabbitMQ",
    5900: "VNC",
    5938: "TeamViewer",
    5984: "CouchDB",
    6379: "Redis",
    6443: "Kubernetes API",
    6667: "IRC",
    7000: "Couchbase",
    7200: "Hazelcast",
    8000: "HTTP-Alt",
    8008: "HTTP-Alt",
    8080: "HTTP-Proxy",
    8081: "SonarQube",
    8086: "InfluxDB",
    8088: "Kibana",
    8181: "HTTP-Alt",
    8443: "HTTPS-Alt",
    8444: "Jenkins",
    8888: "HTTP-Alt",
    9000: "SonarQube",
    9090: "Openfire",
    9092: "Kafka",
    9093: "Prometheus Alertmanager",
    9200: "Elasticsearch",
    9300: "Elasticsearch",
    9418: "Git",
    9990: "JBoss Management",
    9993: "Unreal Tournament",
    9999: "NMAP",
    10000: "Webmin",
    10050: "Zabbix Agent",
    10051: "Zabbix Server",
    11211: "Memcached",
    11300: "Beanstalkd",
    1521: "Oracle DB",
    25565: "Minecraft",
    27015: "Source Engine Games",
    27017: "MongoDB",
    27018: "MongoDB",
    5044: "Logstash",
    50000: "SAP",
    50030: "Hadoop",
    50070: "Hadoop",
    5555: "Open Remote",
    61616: "ActiveMQ",
    
}

def scan_ports(ip, verbose=True):
    
    try:
        count = 0
        open_ports = {}

        for port, service in ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.50)
            result = sock.connect_ex((ip, port))
            if verbose:
                print(f"\r{BRIGHT_RED} [!] Checking port => {port} ...", end=" ")
            if result == 0:
                open_ports[port] = service
                count += 1
            sock.close()
            sys.stdout.flush()
            time.sleep(0.01)
    
        if open_ports:
            output = ""
            print("\n")
            for port, service in open_ports.items():
                output += f"Port {port} ({service})\n"
                print(f"{BRIGHT_MAGENTA} [+]{BRIGHT_CYAN} Port {port} ({service})")

            print(f" \n\t{BRIGHT_MAGENTA} [+] {BRIGHT_CYAN} {count} Open Ports Found...")
        else:
            print(f" \n\t{BRIGHT_MAGENTA} [+] {BRIGHT_CYAN} No open ports found among the common and advanced ports.")
    
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        pass
    return open_ports

if __name__ == "__main__":
    scan_ports()