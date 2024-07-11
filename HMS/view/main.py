from CTkPieChart import *
import customtkinter

root = customtkinter.CTk()

pie_chart = CTkPieChart(root, line_width=50)
pie_chart.pack(side="left", padx=10, pady=10)

pie_chart.add("A", 90)
pie_chart.add("B", 90)
pie_chart.add("C", 90)
pie_chart.add("D", 45)
pie_chart.add("E", 45)

values = pie_chart.get()

frame = customtkinter.CTkFrame(root, fg_color="transparent")
frame.pack(side="left", padx=(0, 10), pady=10)

for key, values in values.items():
    data_circle = customtkinter.CTkRadioButton(frame, hover=False, text=key,
                                               width=1, fg_color=values["color"])
    data_circle.select()
    data_circle.pack(pady=5)

root.mainloop()