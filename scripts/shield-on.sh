#!/bin/bash
CON="Inwi_Home_@"
nmcli connection modify "$CON" ipv4.dns 127.0.0.1 ipv4.ignore-auto-dns yes
nmcli connection modify "$CON" ipv6.ignore-auto-dns yes
nmcli connection up "$CON"
echo "Shield ON - DNS points to 127.0.0.1"
