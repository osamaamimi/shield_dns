#!/bin/bash
CON="Inwi_Home_@"
nmcli connection modify "$CON" ipv4.dns "" ipv4.ignore-auto-dns no
nmcli connection modify "$CON" ipv6.ignore-auto-dns no
nmcli connection up "$CON"
echo "Shield OFF - DNS back to automatic"
