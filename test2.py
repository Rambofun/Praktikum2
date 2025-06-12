import re

def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip) is not None



ip_address = input("Enter an IP address: ")

if not is_valid_ip(ip_address):
    print("Bitte gib eine gültige IP Adresse an (e.g., 192.168.1.1).")
else:
    octets = ip_address.split(".")

    if len(octets) != 4:
        print("Ungültige Ip Adresse.")
    else:
        octets_int = []
        try:
            for octet in octets:
                octet_int = int(octet)
                if octet_int < 0 or octet_int > 255:
                    raise ValueError(f"Ungültige IP Adresse: {octet} is not in the range 0-255.")
                octets_int.append(octet_int)

            octets_binary = [format(octet, '08b') for octet in octets_int]

            print("In Binär:", octets_binary)

        except ValueError as e:
            print(e)
