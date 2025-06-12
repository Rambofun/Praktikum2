def binär_zu_ip(binär_ip):
    octets = binär_ip.split('.')
    
    decimal_octets = [str(int(octet, 2)) for octet in octets]
    
    return '.'.join(decimal_octets)

user_input = input("Bitte gib eine IP Adresse in binär ein: \n> ")

if all(len(octet) == 8 and all(bit in '01' for bit in octet) for octet in user_input.split('.')):
    decimal_ip = binär_zu_ip(user_input)
    print(f"Deine IP Adresse in binär lautet: {decimal_ip}")
else:
    print("Ungültiger Input. Muss in binär sein und aus jeweils 8 Bit bestehen")
