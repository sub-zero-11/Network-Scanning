<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=28&duration=3000&pause=800&color=00E5FF&center=true&vCenter=true&width=900&lines=Network+%E2%80%94+Scanning+Script" alt="Network — Scanning Script">
</p>

# Network-Scanning

NetworkScanning is a fast, multi-threaded network enumeration tool written in Python, designed for learning, internal security assessments, and offensive security practice.

The tool focuses on speed, simplicity, and clarity while demonstrating core concepts such as socket programming, threading, service identification, and basic banner grabbing.

---

## Key Features

- Multi-threaded TCP port scanning
- Common service identification
- Basic banner grabbing
- Lightweight OS fingerprinting (TTL-based)
- Clean and readable CLI output
- Minimal dependencies


## Usage

```
python3 network_scanner.py -t <target-ip> -p 1-1024
```
<br>

# Specify port range and threads: <br>

```
python3 network_scanner.py -t <target-ip>  -p 1-65535 --threads 150
```

## Command-Line      Options <br>
```
Option	        Description 
-t, --target	Target IP address
-p, --ports	    Port range (default: 1-1024)
--threads	    Number of scanning threads
--timeout	    Socket timeout value
```

## Author: SUB-ZERO

## [LinkedIn:](https://www.linkedin.com/in/salman-hussein-3615852a4/)

## License
This project is licensed under the Apache License 2.0.


