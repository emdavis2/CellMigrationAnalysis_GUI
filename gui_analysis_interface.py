import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import pandas as pd
from skimage.color.rgb_colors import black

filepath = ""
data_path = ""
data_path_1 = False
data_path_2 = False
data_path_3 = False

# need 2 sections: retrieve data
# select figure specifications/modify
# status button too
# more gray area to do all of this


class CellSegmentationGUI:

    def __init__(self, root):
        # self.filepath = ""
        # self.data_path = ""
        self.root = root
        self.root.title("Cell Segmentation Analysis")

        # Configure initial window size
        self.root.geometry("900x500")

        # this is the script we will be executing through the GUI
        self.global_script = "python3"
        self.substrate = ""

        # self.menu = Menu(root)
        # item = Menu(menu)
        # item.add_command(label='New')
        # menu.add_cascade(label='File', menu=item)
        # root.config(menu=menu)

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create left frame
        self.left1_frame = tk.Frame(self.main_frame, width=150)
        self.left1_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        # self.left_frame.config(background="black")

        # Create left frame
        self.left_frame = tk.Frame(self.main_frame, width=150)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        # self.left_frame.config(background="black")

        # Create right frame
        self.right_frame = tk.Frame(self.main_frame, width=500)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10, expand=True)  # was left
        # self.right_frame.config(background="black")

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.right_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create text widget
        self.text_widget = tk.Text(self.right_frame, yscrollcommand=self.scrollbar.set)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.text_widget.yview)

        # label for function selection
        self.f1_label = tk.Label(self.left1_frame, text="Specify Paths", font=("Arial", 11, "bold"))
        self.f1_label.pack(pady=10)

        # Create file path selection button
        self.file_button = tk.Button(self.left1_frame, text="Figure Save Location", command=self.select_file)
        self.file_button.pack(pady=6)

        # Enter location for file directory
        self.save_loc = tk.Label(self.left1_frame, text="Enter directory name(optional):", font=("Arial", 8, "bold"))
        self.save_loc.pack(pady=5)

        self.enter_mkdir = tk.Entry(self.left1_frame)
        self.enter_mkdir.pack(pady=5)

        # Select data location
        self.file_button = tk.Button(self.left1_frame, text="Stiff_Gel Data Location", command=self.select_data)
        self.file_button.pack(pady=10)

        # Select data location 2
        self.file_button = tk.Button(self.left1_frame, text="Soft_Gel Data Location", command=self.select_data_2)
        self.file_button.pack(pady=10)

        # Select data location 3
        self.file_button = tk.Button(self.left1_frame, text="Glass Data Location", command=self.select_data_3)
        self.file_button.pack(pady=10)

        # large overall label
        self.surface_label = tk.Label(self.left_frame, text="Build Figures", font=("Arial", 11, "bold"))
        self.surface_label.pack(pady=10)

        # label for function selection
        self.surface_label = tk.Label(self.left_frame, text="Choose function category:", font=("Arial", 8, "bold"))
        self.surface_label.pack(pady=10)

        # Create checkbox for acf fun
        self.acf_fun_var = tk.IntVar()
        self.acf_checkbox = tk.Checkbutton(self.left_frame, text="ACF Functions", variable=self.acf_fun_var)
        self.acf_checkbox.pack()

        # Create checkbox for histogram/boxplot (cell shape over track)
        self.hist_fun_var = tk.IntVar()
        self.hist_checkbox = tk.Checkbutton(self.left_frame, text="CellShapeOverTrack", variable=self.hist_fun_var)
        self.hist_checkbox.pack()

        # Create checkbox for histogram/boxplot_2
        self.box_fun_var = tk.IntVar()
        self.box_checkbox = tk.Checkbutton(self.left_frame, text="Histogram & Boxplot", variable=self.box_fun_var)
        self.box_checkbox.pack()

        # setting global variable for substrate
        # if self.acf_fun_var.get() == 1:

        # Create checkbox for cell surface types
        self.surface_label = tk.Label(self.left_frame, text="Choose substrate:", font=("Arial", 8, "bold"))
        self.surface_label.pack(pady=10)

        self.stiff_gel_var = tk.IntVar()
        self.stiff_gel_checkbox = tk.Checkbutton(self.left_frame, text="Stiff Gel", variable=self.stiff_gel_var)
        self.stiff_gel_checkbox.pack()

        self.soft_gel_var = tk.IntVar()
        self.soft_gel_checkbox = tk.Checkbutton(self.left_frame, text="Soft Gel", variable=self.soft_gel_var)
        self.soft_gel_checkbox.pack()

        self.glass_var = tk.IntVar()
        self.glass_checkbox = tk.Checkbutton(self.left_frame, text="Glass", variable=self.glass_var)
        self.glass_checkbox.pack()

        # create minimum track length label
        self.track_length_label = tk.Label(self.left_frame, text="Enter minimum track length:", font=("Arial", 8, "bold"))
        self.track_length_label.pack(pady=5)

        self.enter_min_length = tk.Entry(self.left_frame)
        self.enter_min_length.pack(pady=5)

        # Create button to run the python script through gui
        self.run_button = tk.Button(self.left_frame, text="Generate Graphs", command=self.run_sc)
        # self.ttk.Button(self.left_frame, text="Generate Graphs", command=self.run_sc, style="RoundedButton.TButton")
        self.run_button.pack(pady=20)

        # Create menus
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.about_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="Use", command=self.show_use)
        self.about_menu.add_command(label="Author", command=self.show_author)
        self.about_menu.add_command(label="Help", command=self.show_help)

    def select_file(self):
        global filepath
        filepath = filedialog.askdirectory()
        self.text_widget.insert(tk.END, f"Figure save location: {filepath}\n")

    def select_data(self):
        global data_path_1
        data_path_1 = filedialog.askdirectory()
        self.text_widget.insert(tk.END, f"Stiff Gel: {data_path_1}\n")

    def select_data_2(self):
        global data_path_2
        data_path_2 = filedialog.askdirectory()
        self.text_widget.insert(tk.END, f"Soft Gel: {data_path_2}\n")

    def select_data_3(self):
        global data_path_3
        data_path_3 = filedialog.askdirectory()
        self.text_widget.insert(tk.END, f"Glass: {data_path_3}\n")

    def open_file(self):
        self.text_widget.insert(tk.END, "Open file option selected\n")

    def save_file(self):
        # print(pd.__version__)
        self.text_widget.insert(tk.END, "Save file option selected\n")

    def show_use(self):
        self.text_widget.insert(tk.END, "This GUI is created for use in Dr. Tim Elston's Lab at UNC. "
                                        "This interface is intended to provide streamlined creation of "
                                        "\nvisualizations. This GUI is part of a larger project analyzing durotaxis.\n")

    def show_author(self):
        self.text_widget.insert(tk.END, "Author: Noah Shaul\n")

    def show_help(self):
        self.text_widget.insert(tk.END, "Use the left sidebar to input requests for data analysis. For assistance, "
                                        "please email noajam@unc.edu.\n")

    def run_sc(self):
        try:
            global data_path
            global data_path_1
            global data_path_2
            global data_path_3
            global filepath
            if len(self.enter_mkdir.get()) != 0:
                mkdir_name = self.enter_mkdir.get()
                filepath = f'{mkdir_name}'
            else:
                filepath = f"{filepath}"
            # print(data_path)
            # note: I will eventually need to modify this code
            # for i checkbox in checked substrates subprocess.call... command lines for each
            # also need to encapsulate acf calling and for call in fxn go through substrates

            min_length = self.enter_min_length.get()

            if self.acf_fun_var.get() == 1:
                fig = "GenerateDataACF.py"

                if self.stiff_gel_var.get() == 1:
                    surface = 'stiff_gel'
                    data_path = data_path_1
                    # data_path = "2023_03_30_Data/stiff_gel_data"
                if self.soft_gel_var.get() == 1:
                    surface = 'soft_gel'
                    data_path = data_path_2
                    # data_path = "2023_03_30_Data/soft_gel_data"
                if self.glass_var.get() == 1:
                    surface = 'glass'
                    data_path = data_path_3
                    # data_path = "2023_03_30_Data/glass_data"

                line = f"python, {fig}, {data_path}, {min_length}, {surface}, {filepath}"  # data_path or data
                subprocess.call(["python", fig, data_path, min_length, surface, filepath])

            if self.hist_fun_var.get() == 1:
                fig = "CellShapeOverTrack.py"
                if self.stiff_gel_var.get() == 1:
                    surface_1 = 'stiff_gel'
                    # data_path = "2023_03_30_Data/stiff_gel_data"
                if self.soft_gel_var.get() == 1:
                    surface_2 = 'soft_gel'
                    # data_path = "2023_03_30_Data/soft_gel_data"
                if self.glass_var.get() == 1:
                    surface_3 = 'glass'
                    # data_path = "2023_03_30_Data/glass_data"

                line = f"python, {fig}, {data_path_1}, {data_path_2}, {data_path_3}, {min_length}, {surface_1}, {surface_2}, {surface_3}, {filepath}"  # data_path or data
                subprocess.call(["python", fig, data_path_1, data_path_2, data_path_3, min_length, surface_1, surface_2, surface_3, filepath])
                # note: going to need to concatenate the inputs I think, make a fxn that correctly concats them.
                # so there is more user autonomy, right now fits script tho

            if self.box_fun_var.get() == 1:
                fig = "GenerateDataHistogramBoxplot.py"
                if self.stiff_gel_var.get() == 1:
                    surface_1 = 'stiff_gel'
                    # data_path = "2023_03_30_Data/stiff_gel_data"
                if self.soft_gel_var.get() == 1:
                    surface_2 = 'soft_gel'
                    # data_path = "2023_03_30_Data/soft_gel_data"
                if self.glass_var.get() == 1:
                    surface_3 = 'glass'
                    # data_path = "2023_03_30_Data/glass_data"
                    # data_path = "2023_03_30_Data/glass_data"

                line = f"python, {fig}, {data_path_1}, {data_path_2}, {data_path_3}, {min_length}, {surface_1}, {surface_2}, {surface_3}, {filepath}"  # data_path or data
                subprocess.call(["python", fig, data_path_1, data_path_2, data_path_3, min_length, surface_1, surface_2, surface_3, filepath])
                # note: going to need to concatenate the inputs I think, make a fxn that correctly concats them.
                # so there is more user autonomy, right now fits script tho

            # ensure that python environment is running pandas 1.4.4
            # settings ->  python environment -> package
            # "GUI_test_figures" -> needs to be filepath , data not data_path, global variable/reset error/permissions error
            # line I need to make: GenerateDataACF.py '2023_03_30_Data/stiff_gel_data' 30 'stiff_gel' 'GUI_test_figures'
            # save_path = "C:\\Users\\Noah Shaul\\Desktop\\elston_lab\\CellMigrationAnalysis_GUI"
            # script = "output_test.py"
            # .format(str(min_length))
            # script = "script_prac.py"
            # command = ["python", script, min_length]
            # subprocess.call(command)
            self.text_widget.insert(tk.END, f"Line constructed: {line}\n")
            # self.text_widget.insert(tk.END, f"Script {script} successfully executed\n")
            # self.right_frame(text="Script executed")
        except ValueError:
            tk.messagebox.showerror("Error_Box", "Error! Enter integer value for min_track_length")
        except:
            print("nah")
            tk.messagebox.showerror("Error_Box", "Error: cannot generate graphs")




# Create the main window
root = tk.Tk()
gui = CellSegmentationGUI(root)
root.mainloop()
