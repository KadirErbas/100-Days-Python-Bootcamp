import tkinter


# Window
window = tkinter.Tk()
window.title("BMI Calculator")

window.minsize(width=250, height=210)
window.config(padx=20, pady=20)

# label
weight_input_label = tkinter.Label(text="Enter Your Weight (KG)")
weight_input_label.config(fg="black")
weight_input_label.config(pady=5)
weight_input_label.pack()


# Entry
weight_input = tkinter.Entry(width=15)
weight_input.pack()


height_input_label = tkinter.Label(text="Enter Your Height (CM)")
height_input_label.config(fg="black")
height_input_label.config(pady=5)
height_input_label.pack()

# Entry2
height_input = tkinter.Entry(width=15)
height_input.pack()

result_label = tkinter.Label()
# button
def button_clicked():
    if(height_input.get() == "" or weight_input.get() == ""):
        result_label.config(text=f"Enter both weight and height!")
        return
    try:
        input_kg = int(weight_input.get())
        input_m = int(height_input.get()) / 100
    except(ValueError):
        result_label.config(text=f"Enter a valid number!")
        return

    user_BMI = input_kg / input_m ** 2

    result_string = f"Your BMI is {round(user_BMI,1)}. You are "
    if(user_BMI < 18.5):
        result_string += "Under Weight"
    elif(18.5 <= user_BMI < 25):
        result_string+= "Normal"
    elif(25 <= user_BMI < 30):
        result_string += "Over Weight"
    elif(30 <= user_BMI < 35):
        result_string += "Obesity (Class I)"
    elif(35 <= user_BMI < 40):
        result_string += "Obesity (Class II)"
    elif(user_BMI >= 40):
        result_string += "Extreme Obesity"

    result_label.config(text=result_string)




calculate_button = tkinter.Button(text="Calculate", command=button_clicked)

calculate_button.pack(anchor=tkinter.W, padx=80, pady=10)


result_label.pack()

window.mainloop()