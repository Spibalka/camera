import tkinter as tk

def on_button_click():
    input_text = entry.get()
    print("Beírt szöveg:", input_text)

# Létrehozzuk a főablakot
root = tk.Tk()

# Ablak címe
root.title("Egyszerű Grafikus Felület")

# Létrehozunk egy címkét
label = tk.Label(root, text="Írj valamit:")
label.pack()

# Létrehozunk egy szövegmezőt
entry = tk.Entry(root)
entry.pack()

# Létrehozunk egy gombot
button = tk.Button(root, text="Kattints ide!", command=on_button_click)
button.pack()

# Az ablak folyamatosan fut
root.mainloop()
