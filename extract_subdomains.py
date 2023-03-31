import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python extract_subdomains.py <domain_name>")
    exit(1)

domain_name = sys.argv[1]

command = "dig {} +short | grep '^[^;].*{}'".format(domain_name, domain_name)
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

if process.returncode != 0:
    print("Error:", error.decode().strip())
    exit(1)

subdomains = output.decode().strip().split("\n")
print("********* Created By Darwin **********")
print("********* RunSubDom **********")
print("Subdomains:")
for subdomain in subdomains:
    print(subdomain)