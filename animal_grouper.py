import os
import numpy as np
import pandas as pd
import random
import tkinter as tk
from tkinter import filedialog as fd


class Animal_grouper:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(string="Animal Grouper")
        self.window.iconbitmap(os.getcwd() + "/favicon.ico")

        self.file = tk.StringVar()
        self.file.set("Please select a file.")
        self.gender = tk.BooleanVar()
        self.gender.set(False)
        self.constant = tk.DoubleVar()
        self.constant.set(1.0)
        self.group_amount = tk.IntVar()
        self.group_amount.set(4)

        self.title = tk.Label(
            text="Animal Grouping Program",
        )

        # Create the five frames.
        self.root = tk.Frame(self.window, padx=20, pady=10)
        self.input_frame = tk.LabelFrame(self.root, text="Data", padx=20, pady=10)
        self.config_frame = tk.LabelFrame(self.root, text="Config", padx=20, pady=5)
        self.log_frame = tk.LabelFrame(self.root, text="Log", padx=20, pady=10)
        self.display_frame = tk.LabelFrame(self.root, text="Status", padx=20, pady=10)
        self.button_frame = tk.Frame(self.root, padx=20, pady=10)

        # Create and pack the widgets for input_frame.
        self.input_label = tk.Label(self.input_frame, text="Select a File: ")
        self.file_label = tk.Label(
            self.input_frame,
            width=50,
            fg="blue",
            bg="white",
            anchor="w",
            textvariable=self.file,
        )
        self.input_browseBtn = tk.Button(
            self.input_frame, text="Browse", command=self.upload
        )

        self.input_label.pack(side="left")
        self.file_label.pack(side="left")
        self.input_browseBtn.pack(side="right")

        # Create and pack the widgets for config_frame.
        self.config_top = tk.Frame(self.config_frame)
        self.config_bottom = tk.Frame(self.config_frame)

        self.group_amount_label = tk.Label(
            self.config_top, text="Group Amount: ", anchor="w"
        )
        self.group_amount_scale = tk.Scale(
            self.config_top,
            variable=self.group_amount,
            from_=2,
            to=10,
            length=400,
            tickinterval=1,
            resolution=1,
            orient=tk.HORIZONTAL,
        )

        self.group_amount_label.pack(side="left")
        self.group_amount_scale.pack(side="right")

        self.gender_checkbox = tk.Checkbutton(
            self.config_bottom,
            text="Based on Gender ",
            variable=self.gender,
            onvalue=True,
            offvalue=False,
        )
        self.constant_label = tk.Label(self.config_bottom, text="Constant: ")
        self.constant_scale = tk.Scale(
            self.config_bottom,
            variable=self.constant,
            from_=0.5,
            to=1.5,
            length=200,
            tickinterval=1,
            resolution=0.05,
            orient=tk.HORIZONTAL,
        )
        self.gender_checkbox.pack(side="left")
        self.constant_scale.pack(side="right")
        self.constant_label.pack(side="right")

        self.config_top.pack(fill=tk.BOTH)
        self.config_bottom.pack(fill=tk.BOTH)

        # Create and pack the widgets for log_frame.
        self.log_left = tk.Frame(self.log_frame)
        self.log_right = tk.Frame(self.log_frame)

        self.log_file_label = tk.Label(
            self.log_left, text="Selected File:", anchor="w", width=15
        )
        self.log_group_amount_label = tk.Label(
            self.log_left, text="Group Amount: ", anchor="w", width=15
        )
        self.log_gender_label = tk.Label(
            self.log_left, text="Group on Gender: ", anchor="w", width=15
        )
        self.log_constant_label = tk.Label(
            self.log_left, text="Constant: ", anchor="w", width=15
        )

        self.log_file_var = tk.Label(
            self.log_right,
            textvariable=self.file,
            anchor="e",
            fg="Blue",
            width=50,
            bg="white",
        )
        self.log_group_amount_var = tk.Label(
            self.log_right,
            textvariable=self.group_amount,
            anchor="e",
            fg="Blue",
            width=50,
            bg="white",
        )
        self.log_gender_var = tk.Label(
            self.log_right,
            textvariable=self.gender,
            anchor="e",
            fg="Blue",
            width=50,
            bg="white",
        )
        self.log_constant_var = tk.Label(
            self.log_right,
            textvariable=self.constant,
            anchor="e",
            fg="Blue",
            width=50,
            bg="white",
        )

        self.log_file_label.pack()
        self.log_group_amount_label.pack()
        self.log_gender_label.pack()
        self.log_constant_label.pack()

        self.log_file_var.pack()
        self.log_group_amount_var.pack()
        self.log_gender_var.pack()
        self.log_constant_var.pack()

        self.log_left.pack(side="left")
        self.log_right.pack(side="right")

        # Create and pack the widgets for display_frame.
        self.display_text = tk.Text(
            self.display_frame,
            height=8,
            width=88,
            fg="Blue",
        )
        self.display_text.pack()

        # Create and pack the widgets for button_frame.
        self.clear_button = tk.Button(
            self.button_frame, text="Clear", command=self.clear
        )
        self.confirm_button = tk.Button(
            self.button_frame, text="Confirm", command=self.confirm
        )
        self.quit_button = tk.Button(
            self.button_frame, text="Quit", command=self.window.destroy
        )

        self.clear_button.pack(side="left")
        self.confirm_button.pack(side="right")
        self.quit_button.pack(side="right")

        # Pack the frames.
        self.title.pack()
        self.input_frame.pack(fill=tk.BOTH)
        self.config_frame.pack(fill=tk.BOTH)
        self.log_frame.pack(fill=tk.BOTH)
        self.display_frame.pack(fill=tk.BOTH)
        self.button_frame.pack(fill=tk.BOTH)

        self.root.pack()

        # Start the main loop.
        tk.mainloop()

    def clear(self, event=None):
        self.display_text.delete(1.0, tk.END)

    def upload(self, event=None):
        filename = fd.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a File",
            filetypes=[("Excel files", ".xlsx .xls")],
        )
        self.file.set(filename)

    def confirm(self, event=None):
        file_name = self.file.get()
        number = self.group_amount.get()
        gender = self.gender.get()
        constant = self.constant.get()
        self.display_text.insert(tk.END, "Selected a File: " + file_name + "\n")
        self.display_text.insert(tk.END, "Group Amount: " + str(number) + "\n")
        self.display_text.insert(
            tk.END,
            "Group on Gender: True\n"
            if self.gender.get() == 1
            else "Group on Gender: False\n",
        )
        self.display_text.insert(tk.END, "Constant: " + str(constant) + "\n")
        try:
            if gender:
                grouper = Animal_grouping_generator_based_on_gender(
                    file_name, number, constant
                )
            else:
                grouper = Animal_grouping_generator(file_name, number, constant)

            message = grouper.get_grouped_data()
            self.display_text.insert(tk.END, "\nResult: " + message + "\n")
        except:
            self.display_text.insert(tk.END, "\nResult: Failed!\n")
        finally:
            self.display_text.insert(
                tk.END,
                "-" * 86 + "\n",
            )


def import_excel(filename: str) -> pd.core.frame.DataFrame:
    """
    Import the data in the excel file's sheet 1 as a dataframe
    """
    df = pd.read_excel(filename)

    return df


def grouping_randomly(
    array: np.ndarray, group_number: int, max_number_per_group: int
) -> np.ndarray:
    """
    Group the ndarray data randomly into group_number.
    Each group cannot have more than the max_number_per_group
    and return as a ndarray
    """
    randomly_grouped_data = []
    for i in range(group_number):
        randomly_grouped_data.append(list())

    for data in array:
        i = random.randrange(group_number)
        full = len(randomly_grouped_data[i]) == max_number_per_group

        while full:
            i = random.randrange(group_number)
            full = len(randomly_grouped_data[i]) == max_number_per_group
        randomly_grouped_data[i].append(data)

    return np.array(randomly_grouped_data)


def check_std_for_each_group(
    grouped_data: np.ndarray, group_number: int, constant: float
) -> bool:
    """
    Check the standard deviation (std) is in the allowed range (constant).
    """
    std = grouped_data.std()

    std_of_each_group = []
    for i in range(group_number):
        std_of_each_group.append(grouped_data[i].std())

    for i in range(group_number):
        if std_of_each_group[i] > std * constant:
            return True
    return False


class Animal_grouping_generator:
    def __init__(self, filename: str, group_number: int, constant: float):
        self.df = import_excel(filename)
        self.constant = constant
        self.sample_size = self.df.shape[0]
        self.weight_ndarray = np.array(self.df["Weight"])
        self.mean = self.weight_ndarray.mean()
        self.std = self.weight_ndarray.std()
        self.group_number = group_number
        self.number_per_group = self.sample_size // self.group_number
        self.max_number_per_group = (
            self.number_per_group
            if self.sample_size % self.group_number == 0
            else self.number_per_group + 1
        )

    def grouping(self, ndarray: np.ndarray, max_number: int):
        grouped_ndarray = grouping_randomly(ndarray, self.group_number, max_number)
        check = check_std_for_each_group(
            grouped_ndarray, self.group_number, self.constant
        )
        counter = 0
        while check:
            grouped_ndarray = grouping_randomly(ndarray, self.group_number, max_number)
            check = check_std_for_each_group(
                grouped_ndarray, self.group_number, self.constant
            )
            counter += 1
            if counter > 999:
                return "Tried 1000 times.\nThe deviation of the data is too big. Please try again or adjust the constant.\n"

        return grouped_ndarray

    def convert_ndarray_to_df(self, grouped_ndarray):
        grouped_df = pd.DataFrame()
        for i in range(self.group_number):
            grouped_df[f"Group {i+1}"] = grouped_ndarray[i]

        return grouped_df

    def get_grouped_data(self):
        grouped_ndarray = self.grouping(self.weight_ndarray, self.max_number_per_group)
        if type(grouped_ndarray) == str:
            return "The diversity of data is too high. Please set to a higher constant."
        else:
            grouped_df = self.convert_ndarray_to_df(grouped_ndarray)
            summary_df = grouped_df.describe()
            with pd.ExcelWriter("output.xlsx") as writer:
                grouped_df.to_excel(writer, sheet_name="Grouped data")
                summary_df.to_excel(writer, sheet_name="Summary")
            return "Success!"


class Animal_grouping_generator_based_on_gender(Animal_grouping_generator):
    def __init__(self, filename, group_number, constant):
        Animal_grouping_generator.__init__(self, filename, group_number, constant)

        # female
        self.female_df = self.df[self.df["Sex"] == "F"]
        self.female_weight_ndarray = np.array(self.female_df["Weight"])
        self.female_sample_size = self.female_df.shape[0]
        self.female_mean = self.female_weight_ndarray.mean()
        self.female_std = self.female_weight_ndarray.std()
        self.female_number_per_group = self.female_sample_size // self.group_number
        self.female_max_number_per_group = (
            self.female_number_per_group
            if self.female_sample_size % self.group_number == 0
            else self.female_number_per_group + 1
        )

        # male
        self.male_df = self.df[self.df["Sex"] == "M"]
        self.male_weight_ndarray = np.array(self.male_df["Weight"])
        self.male_sample_size = self.male_df.shape[0]
        self.male_mean = self.female_weight_ndarray.mean()
        self.male_std = self.female_weight_ndarray.std()
        self.male_number_per_group = self.male_sample_size // self.group_number
        self.male_max_number_per_group = (
            self.male_number_per_group
            if self.male_sample_size % self.group_number == 0
            else self.male_number_per_group + 1
        )

        # grouped data
        self.grouped_female_data()
        self.grouped_male_data()

    def grouped_female_data(self):
        self.grouped_female_ndarray = self.grouping(
            self.female_weight_ndarray, self.female_max_number_per_group
        )
        if type(self.grouped_female_ndarray) == str:
            return ""
        else:
            self.grouped_female_list = self.grouped_female_ndarray.tolist()
            self.grouped_female_df = self.convert_ndarray_to_df(
                self.grouped_female_ndarray
            )
            return self.grouped_female_df

    def grouped_male_data(self):
        self.grouped_male_ndarray = self.grouping(
            self.male_weight_ndarray, self.male_max_number_per_group
        )
        if type(self.grouped_male_ndarray) == str:
            return ""
        else:
            self.grouped_male_list = self.grouped_male_ndarray.tolist()
            self.grouped_male_df = self.convert_ndarray_to_df(self.grouped_male_ndarray)
            return self.grouped_male_df

    def combining_two_sex(self):
        if (
            type(self.grouped_female_ndarray) == str
            or type(self.grouped_male_ndarray) == str
        ):
            return ""
        else:
            group_label = []
            for i in range(self.group_number):
                group_label.append(i)

            # group container
            grouped_list = []
            for i in range(self.group_number):
                number = random.choice(group_label)
                grouped_list.append(
                    self.grouped_female_list[i] + self.grouped_male_list[number]
                )
                group_label.pop(group_label.index(number))

            grouped_ndarray = np.array(grouped_list)

            return grouped_ndarray

    def grouping_with_two_gender(self):
        grouped_ndarray = self.combining_two_sex()
        if type(grouped_ndarray) == str:
            return ""
        else:
            check = check_std_for_each_group(
                grouped_ndarray, self.group_number, self.constant
            )
            while check:
                grouped_ndarray = self.combining_two_sex()
                check = check_std_for_each_group(
                    grouped_ndarray, self.group_number, self.constant
                )

            return grouped_ndarray

    def get_grouped_data(self):
        grouped_ndarray = self.grouping_with_two_gender()
        if type(grouped_ndarray) == str:
            return "The diversity of data is too high. Please set to a higher constant."
        else:
            grouped_df = self.convert_ndarray_to_df(grouped_ndarray)
            summary_df = grouped_df.describe()
            with pd.ExcelWriter("output.xlsx") as writer:
                grouped_df.to_excel(writer, sheet_name="Grouped data")
                self.grouped_female_df.to_excel(writer, sheet_name="Female")
                self.grouped_male_df.to_excel(writer, sheet_name="Male")
                summary_df.to_excel(writer, sheet_name="Summary")
            return "Success!"


if __name__ == "__main__":
    ag = Animal_grouper()
