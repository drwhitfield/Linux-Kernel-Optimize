# -*- coding: utf-8 -*-
#!/usr/bin/python

"""

Enforce Linux Kernel optimzations for high performance servers in enterprise environment.
Usage: sudo python KernelOptimize.py

"""

__author__      =           'Donald Whitfield'
__copyright__   =           '(c) 2021, S-Box Security'
__version__     =           '1.0.0'
__maintainer__  =           'Donald Whitfield'
__email__       =           'donaldwhitfield@icloud.com'
__status__      =           'Development'


import os
import subprocess

TCP_CONG_CTL = ["net.ipv4.tcp_congestion_control=htcp"] #tcp congestion control
TCP_WIN_SCALING = ["net.ipv4.tcp_window_scaling=1"] #tcp window scaling
TCP_SACKS = ["net.ipv4.tcp_sack=1"] #tcp selective acknowledgements
LOW_LAT_MODE = ["net.ipv4.tcp_low_latency=1"] #tcp low latency mode
TCP_WIN_BUFF = ["net.ipv4.tcp_adv_win_scale=1"] #tcp window size buffering
TCP_SYN_FLOODS = ["net.ipv4.tcp_syncookies=1", "net.ipv4.tcp_synack_retries=5"]
TCP_SOURCE_ROUTES = ["net.ipv4.conf.default.accept_source_route=0", "net.ipv4.conf.all.forwarding=0", "net.ipv6.conf.all.forwarding=0", "net.ipv4.conf.all.mc_forwarding=0", "net.ipv6.conf.all.mc_forwarding=0"]
MCAST_TRAFFIC = ["net.ipv4.icmp_echo_ignore_broadcasts=1"]
TCP_MEMORY = ["net.ipv4.tcp_rmem=4096 87380 4194304", "net.ipv4.tcp_wmem=4096 65536 4194304"]
TCP_TIMESTAMPS = ["net.ipv4.tcp_timestamps=0"]
CPU_QUEUE = ["net.core.netdev_max_backlog=250000"]
TCP_BUFFER_RING = ["net.core.rmem_max=4194304", "net.core.wmem_max=4194304", "net.core.rmem_default=4194304", "net.core.wmem_default=4194304", "net.core.optmem_max=4194304"]

kernel_params = TCP_BUFFER_RING + CPU_QUEUE + TCP_TIMESTAMPS + TCP_MEMORY + MCAST_TRAFFIC + TCP_SOURCE_ROUTES + TCP_SYN_FLOODS + TCP_WIN_BUFF + LOW_LAT_MODE + TCP_SACKS + TCP_WIN_SCALING + TCP_CONG_CTL

for param in kernel_params:
    subprocess.Popen(['/sbin/sysctl', '-w', param])
         

#Make the kernel changes persistent across reboots, by writing them to /etc/sysctl.conf

with open ('/etc/sysctl.conf', 'w') as f:
    for os-param in kernel_params:
        print >>f, os-param



