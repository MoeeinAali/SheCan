import subprocess
import sys

PRIMARY_DNS = "178.22.122.100"
SECONDARY_DNS = "185.51.200.2"

def set_dns(mode):
    if mode == "1":
        subprocess.run(['powershell', '-Command', f'Get-NetAdapter | Set-DnsClientServerAddress -ServerAddresses "{PRIMARY_DNS}", "{SECONDARY_DNS}"'])
        print("DNS servers set successfully.")
    elif mode == "0":
        subprocess.run(['powershell', '-Command', 'Get-NetAdapter | Set-DnsClientServerAddress -ResetServerAddresses'])
        print("DNS servers reset to obtain automatically.")
    else:
        print("Invalid mode. Please provide either '1' to set DNS or '0' to reset.")

if len(sys.argv) < 2:
    print("Please provide argument (0 to reset DNS, 1 to set DNS)")
    sys.exit()

mode = sys.argv[1]

if mode == "1":
    set_dns(mode)
elif mode == "0":
    set_dns(mode)
else:
    print("Invalid mode argument. Please provide either '0' or '1'.")