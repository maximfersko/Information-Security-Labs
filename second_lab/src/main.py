import tkinter as tk
from tkinter import messagebox


def encrypt():
    input_text = input_field.get()
    key = key_field.get()
    output_text = ""

    hex_mode = hex_var.get()
    if hex_mode:
        input_text = bytes.fromhex(input_text).decode('utf-8')
        key = bytes.fromhex(key).decode('utf-8')

    for i, c in enumerate(input_text):
        output_text += chr(ord(c) ^ ord(key[i % len(key)]))

    if hex_mode:
        output_text = output_text.encode().hex()

    output_field.delete(0, tk.END)
    output_field.insert(0, output_text)


def decrypt():
    input_text = output_field.get()
    key = key_field.get()
    output_text = ""

    hex_mode = hex_var.get()
    if hex_mode:
        input_text = bytes.fromhex(input_text).decode('utf-8')
        key = bytes.fromhex(key).decode('utf-8')

    for i, c in enumerate(input_text):
        output_text += chr(ord(c) ^ ord(key[i % len(key)]))

    if hex_mode:
        output_text = output_text.encode().hex()

    output_field.delete(0, tk.END)
    output_field.insert(0, output_text)


root = tk.Tk()
root.title("XOR Encryption/Decryption")

input_field = tk.Entry(root)
input_field.pack()

key_field = tk.Entry(root)
key_field.pack()

hex_var = tk.IntVar()
hex_checkbox = tk.Checkbutton(root, text="Hex Mode", variable=hex_var)
hex_checkbox.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack()

output_field = tk.Entry(root)
output_field.pack()

root.mainloop()