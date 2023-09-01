import nmap3

nmap = nmap3.Nmap()
results = nmap.scan_top_ports('scanme.nmap.org')
