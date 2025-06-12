import tkinter as tk
import re
from tkinter import *
from tkinter import ttk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

root = Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('IP Umrechner')
center_window(root)

def neues_fenster_öffnen():
    global binär_eingabe, output_label_binär, neues_fenster
    neues_fenster = Toplevel(root)
    neues_fenster.title("Binär zu Dezimal")
    neues_fenster.geometry('400x300')
    center_window(neues_fenster)

    binär_eingabe = tk.Entry(master=neues_fenster, width=34)
    binär_eingabe.pack(pady=20)

    bestätigen_button = ttk.Button(
        neues_fenster, text='Bestätigen', command=bestätigen
    )
    bestätigen_button.pack(pady=10)

    output_label_binär = tk.Label(neues_fenster, text="", fg="red")
    output_label_binär.pack(pady=10)

    return_button = ttk.Button(
        neues_fenster,
        text='Zurück zum Hauptfenster',
        command=lambda: (root.deiconify(), neues_fenster.destroy())
    )
    return_button.pack(pady=10)

    exit_button = ttk.Button(
        neues_fenster,
        text='Programm Beenden',
        command=root.quit
    )
    exit_button.pack(pady=10)

def neues_fenster_öffnen2():
    global dezimal_eingabe, output_label_dezimal, neues_fenster2
    
    neues_fenster2 = Toplevel(root)
    neues_fenster2.title("Dezimal zu Binär")
    neues_fenster2.geometry('400x300')
    center_window(neues_fenster2)

    dezimal_eingabe = tk.Entry(master=neues_fenster2, width=34)
    dezimal_eingabe.pack(pady=20)

    bestätigen_button2 = ttk.Button(
        neues_fenster2, text='Bestätigen', command=bestätigen2
    )
    bestätigen_button2.pack(pady=10)

    output_label_dezimal = tk.Label(neues_fenster2, text="", fg="red")
    output_label_dezimal.pack(pady=10)

    return_button = ttk.Button(
        neues_fenster2,
        text='Zurück zum Hauptfenster',
        command=lambda: (root.deiconify(), neues_fenster2.destroy())
    )
    return_button.pack(pady=10)

    exit_button = ttk.Button(
        neues_fenster2,
        text='Programm Beenden',
        command=root.quit
    )
    exit_button.pack(pady=10)


# Hintergrundfarbe setzen
root.configure(bg="#FFFFFF")
#neues_fenster.configure(bg="#FFFFFF")
#neues_fenster2.configure(bg="#FFFFFF")

# Rahmen für die Buttons
button_frame = Frame(root, bg='#f0f0f0')
button_frame.pack(pady=20)


# Schriftart und -größe für die Buttons anpassen
style = ttk.Style()
style.configure('TButton', font=('Arial', 12,), fg="#f00000")


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
        output_label_binär.config(text=f"Deine IP Adresse in Dezimal: {decimal_ip}")
    else:
        output_label_binär.config(text="Ungültiger Input. Muss in binär sein und aus jeweils 8 Bit bestehen")

def bestätigen2():
    def is_valid_ip(ip):
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        return re.match(pattern, ip) is not None

    ip_address = dezimal_eingabe.get()

    if not is_valid_ip(ip_address):
        output_label_dezimal.config(text="Bitte gib eine gültige IP Adresse an (e.g., 192.168.1.1).")
    else:
        octets = ip_address.split(".")
        if len(octets) != 4:
            output_label_dezimal.config(text="Ungültige IP Adresse.")
        else:
            octets_int = []
            try:
               
                for octet in octets:
                    octet_int = int(octet)
                    if octet_int < 0 or octet_int > 255:
                        raise ValueError(f"Ungültige IP Adresse: {octet} ist nicht im Bereich 0-255.")
                    octets_int.append(octet_int)

                octets_binary = [format(octet, '08b') for octet in octets_int]
                octets_binary = '.'.join(octets_binary)
                output_label_dezimal.config(text=f"In Binär: {octets_binary}")

            except ValueError as e:
                output_label_dezimal.config(text=str(e))

# Hauptfenster Buttons
first_button = ttk.Button(
    root,
    text='Binär --> Dezimal',
    command=neues_fenster_öffnen
)
first_button.pack(ipadx=10, ipady=10, expand=True)

second_button = ttk.Button(
    root,
    text='Dezimal --> Binär',
    command=neues_fenster_öffnen2
)
second_button.pack(ipadx=10, ipady=10, expand=True)

root.mainloop()
