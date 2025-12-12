import matplotlib.pyplot as plt
import numpy as np
import os
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.colors as mcolors

# Helper functie om de grafiek te maken (elimineert code duplicatie)
def _create_plot(x_as_pos, y_as_pos, x_streep_dik, y_streep_dik, x_streep_dun, y_streep_dun, 
                 vierkant, cijferkleur, titel, x_as_label, y_as_label, titel_kleur, 
                 x_as_label_kleur, y_as_label_kleur):
    """
    Creëert een matplotlib plot met de opgegeven parameters.
    Deze functie wordt gebruikt door zowel teken_grafiek als save_grafiek.
    """
    plt.figure(figsize=(8, 8))
    plt.plot([], [], linestyle='-', alpha=0)

    # Set axis limits
    plt.xlim(0, x_as_pos + 1)
    plt.ylim(0, y_as_pos + 1)

    # Add thick lines
    for x in range(0, x_as_pos + 1, x_streep_dik):
        plt.axvline(x=x, color='black', linewidth=1.5)
    for y in range(0, y_as_pos + 1, y_streep_dik):
        plt.axhline(y=y, color='black', linewidth=1.5)

    # Add thin lines
    for x in range(0, x_as_pos + 1, x_streep_dun):
        plt.axvline(x=x, color='gray', linewidth=1, linestyle='--')
    for y in range(0, y_as_pos + 1, y_streep_dun):
        plt.axhline(y=y, color='gray', linewidth=1, linestyle='--')

    # Make the axes thicker and black
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)

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
    plt.xlabel(x_as_label, color=x_as_label_kleur, fontsize=12, ha='right')
    plt.ylabel(y_as_label, color=y_as_label_kleur, fontsize=12, va='top', rotation=0)

    # Change the color of the tick labels
    plt.tick_params(axis='x', colors=cijferkleur)
    plt.tick_params(axis='y', colors=cijferkleur)

# Functie om input te valideren
def validate_inputs():
    """
    Valideert alle GUI inputs en retourneert een dictionary met de waarden.
    Gooit een ValueError als de input ongeldig is.
    """
    try:
        # Valideer integer inputs
        x_as_pos = int(entry_x_as_pos.get())
        y_as_pos = int(entry_y_as_pos.get())
        x_streep_dik = int(entry_x_streep_dik.get())
        y_streep_dik = int(entry_y_streep_dik.get())
        x_streep_dun = int(entry_x_streep_dun.get())
        y_streep_dun = int(entry_y_streep_dun.get())
        
        # Valideer dat waarden positief zijn
        if x_as_pos <= 0 or y_as_pos <= 0:
            raise ValueError("As posities moeten positief zijn")
        if x_streep_dik <= 0 or y_streep_dik <= 0:
            raise ValueError("Dikke streep afstanden moeten positief zijn")
        if x_streep_dun <= 0 or y_streep_dun <= 0:
            raise ValueError("Dunne streep afstanden moeten positief zijn")
            
        # Valideer kleuren
        cijferkleur = entry_labelkleur.get().strip()
        titel_kleur = entry_titel_kleur.get().strip()
        x_as_label_kleur = entry_x_as_label_kleur.get().strip()
        y_as_label_kleur = entry_y_as_label_kleur.get().strip()
        
        for kleur, naam in [(cijferkleur, "Label Kleur"), 
                            (titel_kleur, "Titel Kleur"),
                            (x_as_label_kleur, "X-as Label Kleur"),
                            (y_as_label_kleur, "Y-as Label Kleur")]:
            if not mcolors.is_color_like(kleur):
                raise ValueError(f"'{kleur}' is geen geldige kleur voor {naam}")
        
        return {
            'x_as_pos': x_as_pos,
            'y_as_pos': y_as_pos,
            'x_streep_dik': x_streep_dik,
            'y_streep_dik': y_streep_dik,
            'x_streep_dun': x_streep_dun,
            'y_streep_dun': y_streep_dun,
            'vierkant': var_vierkant.get(),
            'cijferkleur': cijferkleur,
            'titel': entry_titel.get(),
            'x_as_label': entry_x_as_label.get(),
            'y_as_label': entry_y_as_label.get(),
            'titel_kleur': titel_kleur,
            'x_as_label_kleur': x_as_label_kleur,
            'y_as_label_kleur': y_as_label_kleur
        }
    except ValueError as e:
        raise ValueError(f"Ongeldige input: {str(e)}")

# Functie om de grafiek te tekenen
def teken_grafiek():
    try:
        params = validate_inputs()
        _create_plot(**params)
        plt.show()
    except ValueError as e:
        messagebox.showerror("Invoerfout", str(e))
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een fout opgetreden: {str(e)}")

# Functie om de grafiek op te slaan
def save_grafiek():
    try:
        params = validate_inputs()
        bestandsnaam = entry_bestandsnaam.get().strip()
        
        # Specificeer het pad naar de Downloads-map
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        if bestandsnaam == "":
            bestandsnaam = "grafiek.png"
        
        # Zorg ervoor dat de bestandsnaam eindigt op .png
        if not bestandsnaam.endswith('.png'):
            bestandsnaam += '.png'
        
        # Maak het volledige pad
        full_path = os.path.join(downloads_path, bestandsnaam)
        
        # Creëer de grafiek
        _create_plot(**params)
        
        # Sla de grafiek op
        plt.savefig(full_path, dpi=300, bbox_inches='tight', pad_inches=0.1)
        plt.close()  # Sluit de figuur om geheugen vrij te maken
        
        messagebox.showinfo("Succes", f"Grafiek opgeslagen als:\n{full_path}")
        
    except ValueError as e:
        messagebox.showerror("Invoerfout", str(e))
    except Exception as e:
        messagebox.showerror("Fout", f"Er is een fout opgetreden bij het opslaan: {str(e)}")

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
button_teken = ttk.Button(root, text="Teken Grafiek", command=teken_grafiek)
button_teken.grid(row=15, column=0, columnspan=2)

# Knop om de grafiek op te slaan
button_opslaan = ttk.Button(root, text="Opslaan Grafiek", command=save_grafiek)
button_opslaan.grid(row=16, column=0, columnspan=2)

root.mainloop()
