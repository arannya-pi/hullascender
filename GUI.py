import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
import time
import cv2
import PIL.Image, PIL.ImageTk
import random

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.sidebar_visible = True
        theme_color = "#FF5733"
        self.root.attributes("-fullscreen", True)

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.sidebar_frame = tk.Frame(main_frame, width=200, bg=theme_color, relief=tk.SOLID, borderwidth=2)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        sidebar_label = ttk.Label(self.sidebar_frame, text="Sidebar", style='Sidebar.TLabel')
        sidebar_label.pack(pady=10)

        self.time_label = ttk.Label(self.sidebar_frame, font=('Arial', 24))
        self.time_label.pack(pady=5)

        self.date_label = ttk.Label(self.sidebar_frame, font=('Arial', 18))
        self.date_label.pack(pady=10)

        self.update_time_date_labels()

        style = ttk.Style()
        style.configure('Sidebar.TLabel', font=('Arial', 16), foreground='blue')

        self.sidebar_tree = ttk.Treeview(self.sidebar_frame, selectmode='none', padding=(20, 10))
        self.sidebar_tree.pack()

        self.sidebar_tree.insert('', 'end', 'submenu1', text='Submenu 1', tags=('submenu1',))

        self.sidebar_tree.tag_configure('submenu1', font=('Arial', 18), anchor='center')
        self.sidebar_tree.tag_configure('submenu2', font=('Arial', 18), anchor='center')

        style.configure('submenu1.TLabel', background='cyan')
        style.configure('submenu2.TLabel', background='#FFD700')

        self.minimize_button = tk.Button(self.sidebar_frame, text="Minimize", command=self.toggle_sidebar)
        self.minimize_button.pack(pady=10)

        label_frame = tk.Frame(main_frame, bg='white')
        label_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.categories = ['Category 1', 'Category 2', 'Category 3']
        self.values = [random.randint(1, 20) for _ in range(len(self.categories))]  # Define the colors
        self.colors = ['#00FFFF', '#FFD700', '#008000']  # Define the colors

        self.cat_labels = []

        for i, category_color in enumerate(self.colors):
            cat_frame = tk.Frame(
                label_frame,
                bg=category_color,
                relief=tk.SOLID,
                borderwidth=4
            )
            cat_frame.pack(pady=20, fill=tk.BOTH, expand=True)

            cat_label = tk.Label(
                cat_frame,
                text=f"Category {i + 1}: {self.values[i]}",
                font=('Arial', 14, 'bold'),
                fg='black',
                bg=category_color,
                anchor='center'
            )
            cat_label.pack(expand=True, fill=tk.BOTH)
            self.cat_labels.append(cat_label)

        fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
        self.bars = ax.bar(self.categories, self.values, color=self.colors)

        chart_frame = tk.Frame(main_frame, bg='white', padx=10)
        chart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        camera_button = tk.Button(chart_frame, text="Open Camera", command=self.open_camera_dialog)
        camera_button.pack()

        self.update_category_values()  # Update category values every 5 seconds

    def hide_sidebar(self):
        self.sidebar_frame.pack_forget()

    def show_sidebar(self):
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    def update_time_date_labels(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d")
        self.time_label.configure(text=current_time)
        self.date_label.configure(text=current_date)
        self.root.after(1000, self.update_time_date_labels)

    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar_frame.pack_forget()
            self.minimize_button.config(text="Maximize")
            self.sidebar_visible = False
        else:
            self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.minimize_button.config(text="Minimize")
            self.sidebar_visible = True

    def update_category_values(self):
        # Update all category values with random values
        self.values = [random.randint(1, 20) for _ in range(len(self.categories))]

        # Update the labels in the category frames
        for i, label in enumerate(self.cat_labels):
            label.config(text=f"Category {i + 1}: {self.values[i]}")

        # Update the bar chart without creating a new chart
        self.update_bar_chart()

        # Schedule the next update in 5 seconds
        self.root.after(5000, self.update_category_values)

    def update_bar_chart(self):
        for bar, value in zip(self.bars, self.values):
            bar.set_height(value)

        self.canvas.draw()

    def open_camera_dialog(self):
        camera_window = tk.Toplevel(self.root)
        camera_window.title("Camera View")

        camera_canvas = tk.Canvas(camera_window, width=640, height=480)
        camera_canvas.pack()

        cap = cv2.VideoCapture(0)

        def update_camera_feed():
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                camera_canvas.create_image(0, 0, image=photo, anchor=tk.NW)
                camera_canvas.photo = photo

                camera_canvas.after(10, update_camera_feed)
            else:
                cap.release()

        update_camera_feed()

        close_button = tk.Button(camera_window, text="Close Camera", command=camera_window.destroy)
        close_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()
