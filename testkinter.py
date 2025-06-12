import tkinter as tk
import re
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('IP Umrechner')

def neues_fenster_öffnen():
    neues_fenster = Toplevel(root)
    neues_fenster.title("Test")
    neues_fenster.geometry('800x600')
    root.withdraw()

    global binär_eingabe


    binär_eingabe = tk.Entry(master=neues_fenster)
    binär_eingabe.place(x=50, y=50)
    bestätigen_button = ttk.Button(
        neues_fenster, text='Bestätigen', command=bestätigen
    )
    bestätigen_button.place(x=200, y=200)

    return_button = ttk.Button(
        neues_fenster,
        text='Zurück zum Hauptfenster',
        command=lambda: (root.deiconify(), neues_fenster.destroy())
    )
    return_button.pack(pady=20)

    output1 = tk.Label(master=neues_fenster, textvariable=decimal_ip)
    output1.place(x=400,y=400)

def neues_fenster_öffnen2():
    neues_fenster2 = Toplevel(root)
    neues_fenster2.title("Test")
    neues_fenster2.geometry('800x600')
    root.withdraw()

    global dezimal_eingabe


    dezimal_eingabe = tk.Entry(master=neues_fenster2)
    dezimal_eingabe.place(x=300, y=350)
    bestätigen_button2 = ttk.Button(
    neues_fenster2, text='Bestätigen', command=bestätigen2
    )
    bestätigen_button2.place(x=200, y=200)

    return_button = ttk.Button(
        neues_fenster2,
        text='Zurück zum Hauptfenster TEST',
        command=lambda: (root.deiconify(), neues_fenster2.destroy())
    )
    return_button.pack(pady=20)


def bestätigen():
    global decimal_ip
    user_input = binär_eingabe.get()
    
    def binär_zu_ip(binär_ip):
        global decimal_ip
        
        octets = binär_ip.split('.')

        decimal_octets = [str(int(octet, 2)) for octet in octets]

        return '.'.join(decimal_octets)


    if all(len(octet) == 8 and all(bit in '01' for bit in octet) for octet in user_input.split('.')):
        decimal_ip = binär_zu_ip(user_input)
        print(f"Deine IP Adresse in binär lautet: {decimal_ip}")
    else:
       print("Ungültiger Input. Muss in binär sein und aus jeweils 8 Bit bestehen")
    
        


    



def bestätigen2():

    def is_valid_ip(ip):
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        return re.match(pattern, ip) is not None



    ip_address = dezimal_eingabe.get()

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
                octets_binary = '.'.join(octets_binary)
                
                
                print(f"In Binär:  {octets_binary}")

            except ValueError as e:
                print(e)


first_button = ttk.Button(
    root,
    text='Binär --> Dezimal',
    command=neues_fenster_öffnen
)

first_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

second_button = ttk.Button(
    root,
    text='Dezimal --> Binär',
    command=neues_fenster_öffnen2
)

second_button.pack(
    ipadx=10,
    ipady=10,
    expand=True
)

root.mainloop()