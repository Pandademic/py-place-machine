import tkinter as tk
import random

# configure the title


root = tk.Tk()
root.geometry("600x600")
root.title("Place machine!")


# variable


countrys = ["U.S.A", "switzerland", "new zealand"]
citys = ["albany", "bern", "auckland"]


# functions


def add():
    countrys.append(place_name_input.get())
    citys.append(capital_name_input.get())
    list_o_countrys["text"] = str(countrys)
    list_o_citys["text"] = str(citys)

def display_random():
    r_num = random.randint(0,len(countrys) - 1)
    r_num_2 = random.randint(0,len(citys) - 1)
    random_city_display_label["text"] =  countrys[r_num_2]
    random_country_display_label["text"] = citys[r_num]
# widgets

## SECTION 1


place_name_input = tk.Entry(root)
capital_name_input = tk.Entry(root)
append_place_capital = tk.Label(root, text = "Add to the known world:")
add_btn = tk.Button(root, text = "  add!  ", command = add,bg="blue",fg="white")

## SECTION 2


list_o_countrys = tk.Label(root)
list_o_citys = tk.Label(root)


## SECTION 3


random_city_display_label = tk.Label(root)
random_country_display_label =  tk.Label(root)
random_selector_btn = tk.Button(root,text="   Display a random city and country  ",command=display_random,bg="blue",fg="white")


# place


place_name_input.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
capital_name_input.place(relx=0.5,rely=0.3, anchor=tk.CENTER)
append_place_capital.place(relx=0.5,rely=0.1,anchor=tk.CENTER)
add_btn.place(relx=0.5,rely=0.4,anchor=tk.CENTER)

list_o_countrys.place(relx=0.1,rely=0.5)
list_o_citys.place(relx=0.1,rely=0.6)

random_city_display_label.place(relx=0.3,rely=0.9)
random_country_display_label.place(relx=0.3,rely=0.8)
random_selector_btn.place(relx=0.3,rely=0.7)
# loop


root.mainloop()
