from shutil import _ntuple_diskusage


name = input("whats your name?: ")

lastName = input("whats your last name?: " )

age = int(input("how old are you?: "))

ip = input("whats your ip?: ")

if type(ip) != int:

    print(name, lastName, "is", age, "and he exposed his ip, here it is", ip)