import matplotlib.pyplot as plt
import numpy as np
import os
import tkinter as tk
from tkinter import ttk

# Functie om de grafiek te tekenen
def teken_grafiek(x_as_pos, y_as_pos, x_streep_dik, y_streep_dik, x_streep_dun, y_streep_dun, vierkant, cijferkleur, titel, x_as_label, y_as_label, titel_kleur, x_as_label_kleur, y_as_label_kleur):
    plt.figure(figsize=(8, 8))  # Create the blank chart with a custom ratio
    plt.plot([], [], linestyle='-', alpha=0)  # Add invisible plot to maintain structure

    # Set axis limits
    plt.xlim(0, x_as_pos + 1)
    plt.ylim(0, y_as_pos + 1)

    # Add thick lines every 10 units
    for x in range(0, x_as_pos + 1, x_streep_dik):
        plt.axvline(x=x, color='black', linewidth=1.5)  # Thick vertical lines
    for y in range(0, y_as_pos + 1, y_streep_dik):
        plt.axhline(y=y, color='black', linewidth=1.5)  # Thick horizontal lines

    # Add thin lines every 5 units
    for x in range(0, x_as_pos + 1, x_streep_dun):
        plt.axvline(x=x, color='gray', linewidth=1, linestyle='--')  # Thin vertical lines
    for y in range(0, y_as_pos + 1, y_streep_dun):
        plt.axhline(y=y, color='gray', linewidth=1, linestyle='--')  # Thin horizontal lines

    # Make the axes thicker and black
    ax = plt.gca()  # Get the current axes
    ax.spines['bottom'].set_linewidth(3)  # Bottom spine (x-axis)
    ax.spines['left'].set_linewidth(3)    # Left spine (y-axis)

    # Add arrows to the x and y axes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Hide the top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Set the aspect ratio to 'equal' to make the axes scale equally
    if vierkant:
        ax.set_aspect('equal', adjustable='box')

    # Set title and axis labels with color and alignment
    plt.title(titel, color=titel_kleur, fontsize=14)
    plt.xlabel(x_as_label, color=x_as_label_kleur, fontsize=12, ha='right')  # X-as label rechts uitgelijnd
    plt.ylabel(y_as_label, color=y_as_label_kleur, fontsize=12, va='top', rotation=0)  # Y-as label boven uitgelijnd en horizontaal

    # Change the color of the tick labels
    plt.tick_params(axis='x', colors=cijferkleur)  # X-as tick labels
    plt.tick_params(axis='y', colors=cijferkleur)  # Y-as tick labels

    # Show the plot
    plt.show()

# Functie om de grafiek op te slaan
def save_grafiek():
    # Verkrijg de huidige waarden uit de GUI
    x_as_pos = int(entry_x_as_pos.get())
    y_as_pos = int(entry_y_as_pos.get())
    x_streep_dik = int(entry_x_streep_dik.get())
    y_streep_dik = int(entry_y_streep_dik.get())
    x_streep_dun = int(entry_x_streep_dun.get())
    y_streep_dun = int(entry_y_streep_dun.get())
    vierkant = var_vierkant.get()
    cijferkleur = entry_labelkleur.get()
    titel = entry_titel.get()
    x_as_label = entry_x_as_label.get()
    y_as_label = entry_y_as_label.get()
    titel_kleur = entry_titel_kleur.get()
    x_as_label_kleur = entry_x_as_label_kleur.get()
    y_as_label_kleur = entry_y_as_label_kleur.get()
    bestandsnaam = entry_bestandsnaam.get()

    # Specificeer het pad naar de Downloads-map
    downloads_path = os.path.expanduser('~') + '/Downloads/'
    if bestandsnaam == "":
        bestandsnaam = "grafiek.png"  # Standaard naam als er geen naam is ingevoerd

    # Sla de grafiek op zonder witte randen
    plt.figure(figsize=(8, 8))  # Create the blank chart with a custom ratio
    plt.plot([], [], linestyle='-', alpha=0)  # Add invisible plot to maintain structure

    # Set axis limits
    plt.xlim(0, x_as_pos + 1)
    plt.ylim(0, y_as_pos + 1)

    # Add thick lines every 10 units
    for x in range(0, x_as_pos + 1, x_streep_dik):
        plt.axvline(x=x, color='black', linewidth=1.5)  # Thick vertical lines
    for y in range(0, y_as_pos + 1, y_streep_dik):
        plt.axhline(y=y, color='black', linewidth=1.5)  # Thick horizontal lines

    # Add thin lines every 5 units
    for x in range(0, x_as_pos + 1, x_streep_dun):
        plt.axvline(x=x, color='gray', linewidth=1, linestyle='--')  # Thin vertical lines
    for y in range(0, y_as_pos + 1, y_streep_dun):
        plt.axhline(y=y, color='gray', linewidth=1, linestyle='--')  # Thin horizontal lines

    # Make the axes thicker and black
    ax = plt.gca()  # Get the current axes
    ax.spines['bottom'].set_linewidth(3)  # Bottom spine (x-axis)
    ax.spines['left'].set_linewidth(3)    # Left spine (y-axis)

    # Add arrows to the x and y axes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    # Hide the top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Set the aspect ratio to 'equal' to make the axes scale equally
    if vierkant:
        ax.set_aspect('equal', adjustable='box')

    # Set title and axis labels with color and alignment
    plt.title(titel, color=titel_kleur, fontsize=14)
    plt.xlabel(x_as_label, color=x_as_label_kleur, fontsize=12, ha='right')  # X-as label rechts uitgelijnd
    plt.ylabel(y_as_label, color=y_as_label_kleur, fontsize=12, va='top', rotation=0)  # Y-as label boven uitgelijnd en horizontaal

    # Change the color of the tick labels
    plt.tick_params(axis='x', colors=cijferkleur)  # X-as tick labels
    plt.tick_params(axis='y', colors=cijferkleur)  # Y-as tick labels

    # Save the plot to the Downloads folder with the provided file name
    plt.savefig(downloads_path + bestandsnaam, dpi=300, bbox_inches='tight', pad_inches=0.1)

    print(f"Grafiek opgeslagen als {downloads_path + bestandsnaam}")

# Maak de GUI
root = tk.Tk()
root.title("Grafiek Instellingen")

# X-as positie
label_x_as_pos = ttk.Label(root, text="X-as Positie:")
label_x_as_pos.grid(row=0, column=0)
entry_x_as_pos = ttk.Entry(root)
entry_x_as_pos.grid(row=0, column=1)
entry_x_as_pos.insert(0, "100")

# Y-as positie
label_y_as_pos = ttk.Label(root, text="Y-as Positie:")
label_y_as_pos.grid(row=1, column=0)
entry_y_as_pos = ttk.Entry(root)
entry_y_as_pos.grid(row=1, column=1)
entry_y_as_pos.insert(0, "100")

# X-streep dikte
label_x_streep_dik = ttk.Label(root, text="X-streep Dikte:")
label_x_streep_dik.grid(row=2, column=0)
entry_x_streep_dik = ttk.Entry(root)
entry_x_streep_dik.grid(row=2, column=1)
entry_x_streep_dik.insert(0, "10")

# Y-streep dikte
label_y_streep_dik = ttk.Label(root, text="Y-streep Dikte:")
label_y_streep_dik.grid(row=3, column=0)
entry_y_streep_dik = ttk.Entry(root)
entry_y_streep_dik.grid(row=3, column=1)
entry_y_streep_dik.insert(0, "10")

# X-streep dunne lijn
label_x_streep_dun = ttk.Label(root, text="X-streep Dun:")
label_x_streep_dun.grid(row=4, column=0)
entry_x_streep_dun = ttk.Entry(root)
entry_x_streep_dun.grid(row=4, column=1)
entry_x_streep_dun.insert(0, "5")

# Y-streep dunne lijn
label_y_streep_dun = ttk.Label(root, text="Y-streep Dun:")
label_y_streep_dun.grid(row=5, column=0)
entry_y_streep_dun = ttk.Entry(root)
entry_y_streep_dun.grid(row=5, column=1)
entry_y_streep_dun.insert(0, "5")

# Labelkleur
label_labelkleur = ttk.Label(root, text="Label Kleur:")
label_labelkleur.grid(row=6, column=0)
entry_labelkleur = ttk.Entry(root)
entry_labelkleur.grid(row=6, column=1)
entry_labelkleur.insert(0, "black")

# Bestandsnaam
label_bestandsnaam = ttk.Label(root, text="Bestandsnaam:")
label_bestandsnaam.grid(row=7, column=0)
entry_bestandsnaam = ttk.Entry(root)
entry_bestandsnaam.grid(row=7, column=1)

# Grafiektitel
label_titel = ttk.Label(root, text="Grafiek Titel:")
label_titel.grid(row=8, column=0)
entry_titel = ttk.Entry(root)
entry_titel.grid(row=8, column=1)
entry_titel.insert(0, "Grafiek Titel")

# X-as label
label_x_as_label = ttk.Label(root, text="X-as Label:")
label_x_as_label.grid(row=9, column=0)
entry_x_as_label = ttk.Entry(root)
entry_x_as_label.grid(row=9, column=1)
entry_x_as_label.insert(0, "X-as")

# Y-as label
label_y_as_label = ttk.Label(root, text="Y-as Label:")
label_y_as_label.grid(row=10, column=0)
entry_y_as_label = ttk.Entry(root)
entry_y_as_label.grid(row=10, column=1)
entry_y_as_label.insert(0, "Y-as")

# Titelkleur
label_titel_kleur = ttk.Label(root, text="Titel Kleur:")
label_titel_kleur.grid(row=11, column=0)
entry_titel_kleur = ttk.Entry(root)
entry_titel_kleur.grid(row=11, column=1)
entry_titel_kleur.insert(0, "black")

# X-as label kleur
label_x_as_label_kleur = ttk.Label(root, text="X-as Label Kleur:")
label_x_as_label_kleur.grid(row=12, column=0)
entry_x_as_label_kleur = ttk.Entry(root)
entry_x_as_label_kleur.grid(row=12, column=1)
entry_x_as_label_kleur.insert(0, "black")

# Y-as label kleur
label_y_as_label_kleur = ttk.Label(root, text="Y-as Label Kleur:")
label_y_as_label_kleur.grid(row=13, column=0)
entry_y_as_label_kleur = ttk.Entry(root)
entry_y_as_label_kleur.grid(row=13, column=1)
entry_y_as_label_kleur.insert(0, "black")

# Vierkant optie
var_vierkant = tk.BooleanVar()
check_vierkant = ttk.Checkbutton(root, text="Maak Grafiek Vierkant", variable=var_vierkant)
check_vierkant.grid(row=14, column=0, columnspan=2)

# Knop om de grafiek te tekenen
button_teken = ttk.Button(root, text="Teken Grafiek", command=lambda: teken_grafiek(
    int(entry_x_as_pos.get()), int(entry_y_as_pos.get()), int(entry_x_streep_dik.get()), 
    int(entry_y_streep_dik.get()), int(entry_x_streep_dun.get()), int(entry_y_streep_dun.get()),
    var_vierkant.get(), entry_labelkleur.get(), entry_titel.get(), entry_x_as_label.get(),
    entry_y_as_label.get(), entry_titel_kleur.get(), entry_x_as_label_kleur.get(), entry_y_as_label_kleur.get()))
button_teken.grid(row=15, column=0, columnspan=2)

# Knop om de grafiek op te slaan
button_opslaan = ttk.Button(root, text="Opslaan Grafiek", command=save_grafiek)
button_opslaan.grid(row=16, column=0, columnspan=2)

root.mainloop()
