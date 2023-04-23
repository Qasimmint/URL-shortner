import pyshorteners as ps

# pyshortner is a file contains class Shornter that has its funtion short(), that takes url as its arg
# tinyurl, adfly, bitly, clckru, qspru, dadg, isdg, osdb are different URL services

# shortening bunch of urls using file handling operation of python
with open("urls.txt", 'r') as file:
    for urls in file.readlines():
        url = urls.strip() # removing extra whitespace, so that url can be shortens at once without error
        shortner = ps.Shortener()
        result = shortner.tinyurl.short(url)
        print(result)

# shortening url upon various url shotetning services
url = str(input("Enter URL here: "))
shorter = ps.Shortener()
services = ["tinyurl", "clckru", "osdb"]
for service in enumerate(services):
    print(service)
select = int(input("Chose the service: "))
if select == 0:
    result = shorter.tinyurl.short(url)
    print(f"tinyurl serviced linked {result}, You can copy or click it to access through")
elif select == 1:
    result = shorter.clckru.short(url)
    print(f"ckckru serviced linked {result}, You can copy or click it to access through")
elif select == 2:
    result = shorter.osdb.short(url)
    print(f"osdb serviced linked {result}, You can copy or click it to access through")
else:
    print("Enter the valid entry")