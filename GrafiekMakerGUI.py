import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.colors as mcolors
import ast

class GraphApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grafiek Maker Pro")
        self.geometry("1100x800")
        
        # --- State Variables ---
        self.init_variables()
        
        # --- UI Setup ---
        self.create_layouts()
        self.create_controls()
        self.create_preview_area()
        
        # --- Initial Draw ---
        self.update_plot()

    def init_variables(self):
        self.var_x_pos = tk.IntVar(value=100)
        self.var_y_pos = tk.IntVar(value=100)
        self.var_x_thick = tk.IntVar(value=10)
        self.var_y_thick = tk.IntVar(value=10)
        self.var_x_thin = tk.IntVar(value=5)
        self.var_y_thin = tk.IntVar(value=5)
        
        self.var_square = tk.BooleanVar(value=False)
        self.var_data_points = tk.StringVar(value="") # Format: (1,1), (2,4)
        
        self.var_title = tk.StringVar(value="Grafiek Titel")
        self.var_xlabel = tk.StringVar(value="X-as")
        self.var_ylabel = tk.StringVar(value="Y-as")
        
        # Colors (Default values)
        self.color_label = "black"
        self.color_title = "black"
        self.color_xlabel = "black"
        self.color_ylabel = "black"

    def create_layouts(self):
        # Main split: Controls (Left) vs Preview (Right)
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ## Control Scrollable Frame
        control_frame_container = ttk.Frame(paned, width=400)
        paned.add(control_frame_container, weight=1)
        
        canvas = tk.Canvas(control_frame_container)
        scrollbar = ttk.Scrollbar(control_frame_container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        ## Preview Frame
        self.preview_frame = ttk.Frame(paned)
        paned.add(self.preview_frame, weight=3)

    def create_controls(self):
        f = self.scrollable_frame
        pad_opts = {'padx': 5, 'pady': 5, 'sticky': 'ew'}
        
        # --- Axes Settings ---
        self.add_section_header(f, "Instellingen Assen", 0)
        
        self.add_entry(f, "X-as Lengte:", self.var_x_pos, 1)
        self.add_entry(f, "Y-as Lengte:", self.var_y_pos, 2)
        self.add_entry(f, "X-streep Dik (afstand):", self.var_x_thick, 3)
        self.add_entry(f, "Y-streep Dik (afstand):", self.var_y_thick, 4)
        self.add_entry(f, "X-streep Dun (afstand):", self.var_x_thin, 5)
        self.add_entry(f, "Y-streep Dun (afstand):", self.var_y_thin, 6)
        
        ttk.Checkbutton(f, text="Vierkante Assen (Equal Aspect)", variable=self.var_square, 
                        command=self.update_plot).grid(row=7, column=0, columnspan=2, pady=5)

        # --- Labels & Text ---
        self.add_section_header(f, "Tekst en Labels", 8)
        
        self.add_entry(f, "Grafiek Titel:", self.var_title, 9)
        self.add_entry(f, "X-as Label:", self.var_xlabel, 10)
        self.add_entry(f, "Y-as Label:", self.var_ylabel, 11)

        # --- Colors ---
        self.add_section_header(f, "Kleuren", 12)
        
        self.create_color_picker(f, "Titel Kleur", "color_title", 13)
        self.create_color_picker(f, "Label (Cijfer) Kleur", "color_label", 14)
        self.create_color_picker(f, "X-as Label Kleur", "color_xlabel", 15)
        self.create_color_picker(f, "Y-as Label Kleur", "color_ylabel", 16)

        # --- Data Plotting ---
        self.add_section_header(f, "Data Punten (Optioneel)", 17)
        ttk.Label(f, text="Punten invoer: (x,y), (x,y)").grid(row=18, column=0, **pad_opts)
        ttk.Entry(f, textvariable=self.var_data_points).grid(row=18, column=1, **pad_opts)
        
        # --- Action Buttons ---
        btn_frame = ttk.Frame(f)
        btn_frame.grid(row=20, column=0, columnspan=2, pady=20, sticky="ew")
        
        ttk.Button(btn_frame, text="Ververs Grafiek", command=self.update_plot).pack(fill=tk.X, pady=2)
        ttk.Button(btn_frame, text="Opslaan als...", command=self.save_graph).pack(fill=tk.X, pady=2)

    def add_section_header(self, parent, text, row):
        ttk.Label(parent, text=text, font=('Helvetica', 10, 'bold')).grid(row=row, column=0, columnspan=2, pady=(15, 5), sticky="w")

    def add_entry(self, parent, label_text, variable, row):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=2, sticky="w")
        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=1, padx=5, pady=2, sticky="ew")
        # Auto trigger update on FocusOut or Return
        entry.bind('<Return>', lambda e: self.update_plot())
        entry.bind('<FocusOut>', lambda e: self.update_plot())

    def create_color_picker(self, parent, label_text, attr_name, row):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, padx=5, pady=2, sticky="w")
        
        # Button showing current color
        btn = tk.Button(parent, text="Kies...", width=10, 
                        bg=getattr(self, attr_name),
                        command=lambda: self.pick_color(attr_name, btn))
        btn.grid(row=row, column=1, padx=5, pady=2, sticky="w")

    def pick_color(self, attr_name, btn_widget):
        curr_color = getattr(self, attr_name)
        color = colorchooser.askcolor(color=curr_color, title="Kies Kleur")[1] # [1] returns hex string
        if color:
            setattr(self, attr_name, color)
            btn_widget.config(bg=color)
            self.update_plot()

    def create_preview_area(self):
        # Matplotlib Figure
        self.fig = plt.figure(figsize=(6, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.preview_frame)
        self.canvas.draw()
        
        toolbar_frame = ttk.Frame(self.preview_frame)
        toolbar_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Pack canvas
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def validate_and_get_data(self):
        try:
            data = {
                'x_max': self.var_x_pos.get(),
                'y_max': self.var_y_pos.get(),
                'x_thick': self.var_x_thick.get(),
                'y_thick': self.var_y_thick.get(),
                'x_thin': self.var_x_thin.get(),
                'y_thin': self.var_y_thin.get(),
                'square': self.var_square.get(),
                'title': self.var_title.get(),
                'xlabel': self.var_xlabel.get(),
                'ylabel': self.var_ylabel.get(),
                'c_title': self.color_title,
                'c_label': self.color_label,
                'c_xlabel': self.color_xlabel,
                'c_ylabel': self.color_ylabel,
                'points': self.var_data_points.get()
            }
            if data['x_max'] <= 0 or data['y_max'] <= 0: raise ValueError("Assen moeten positief zijn.")
            return data
        except ValueError:
            return None # Ignore invalid ints during typing

    def update_plot(self):
        params = self.validate_and_get_data()
        if not params:
            return

        self.ax.clear()
        
        # --- Drawing Logic (Adapted from original) ---
        x_max, y_max = params['x_max'], params['y_max']
        
        self.ax.set_xlim(0, x_max + 1)
        self.ax.set_ylim(0, y_max + 1)
        
        # Grid Lines
        # Thick
        for x in range(0, x_max + 1, params['x_thick']):
            self.ax.axvline(x=x, color='black', linewidth=1.5, zorder=1)
        for y in range(0, y_max + 1, params['y_thick']):
            self.ax.axhline(y=y, color='black', linewidth=1.5, zorder=1)
            
        # Thin
        for x in range(0, x_max + 1, params['x_thin']):
            self.ax.axvline(x=x, color='gray', linewidth=1, linestyle='--', zorder=0)
        for y in range(0, y_max + 1, params['y_thin']):
            self.ax.axhline(y=y, color='gray', linewidth=1, linestyle='--', zorder=0)

        # Axes Styling
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.spines['left'].set_linewidth(2)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        
        # Arrows
        self.ax.plot(1, 0, ">k", transform=self.ax.get_yaxis_transform(), clip_on=False)
        self.ax.plot(0, 1, "^k", transform=self.ax.get_xaxis_transform(), clip_on=False)
        
        # Aspect Ratio
        if params['square']:
            self.ax.set_aspect('equal', adjustable='box')
        else:
            self.ax.set_aspect('auto')
            
        # Labels & Colors
        self.ax.set_title(params['title'], color=params['c_title'], fontsize=14)
        self.ax.set_xlabel(params['xlabel'], color=params['c_xlabel'], fontsize=12, loc='right')
        self.ax.set_ylabel(params['ylabel'], color=params['c_ylabel'], fontsize=12, loc='top', rotation=0)
        
        self.ax.tick_params(axis='x', colors=params['c_label'])
        self.ax.tick_params(axis='y', colors=params['c_label'])

        # --- Data Points Plotting ---
        if params['points'].strip():
            try:
                # Safe parsing of tuple strings like "(1,2), (3,4)"
                # Wrap in brackets to make it a list of tuples if it's just comma separated
                points_str = f"[{params['points']}]"
                points = ast.literal_eval(points_str)
                
                # Filter valid tuples
                xs = [p[0] for p in points if isinstance(p, (list, tuple)) and len(p) >= 2]
                ys = [p[1] for p in points if isinstance(p, (list, tuple)) and len(p) >= 2]
                
                if xs and ys:
                    self.ax.plot(xs, ys, 'ro-', linewidth=2, markersize=6, label='Data')
                    self.ax.legend()
                    
            except Exception:
                pass # Fail silently for invalid data input to avoid annoying popups while typing

        self.canvas.draw()

    def save_graph(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("PDF Document", "*.pdf"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                self.fig.savefig(file_path, dpi=300, bbox_inches='tight')
                messagebox.showinfo("Succes", f"Opgeslagen als: {file_path}")
            except Exception as e:
                messagebox.showerror("Fout", f"Kan niet opslaan: {str(e)}")

if __name__ == "__main__":
    app = GraphApp()
    app.mainloop()
