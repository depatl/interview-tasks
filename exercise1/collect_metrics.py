#!/usr/bin/env python3
"""
collect_metrics.py

Script to read a list of server IPs from servers.txt, simulate an SSH connection,
and generate a random CPU usage metric for each server.

Output in JSON format: [{"server": IP, "cpu": UTILIZATION }]

Usage:
    python collect_metrics.py
"""
