# GUI Animal Grouper
<img width="424" alt="GUI_grouper" src="https://github.com/luluwu516/GUI_animal_grouper/assets/98475122/a44211d0-421a-401c-9c8a-5ae7c0accefc">

The program uses a graphical user interface (GUI) for experimental animal grouping.
It's based on my first side project, [Animal Grouping](https://github.com/luluwu516/animal-grouping), applying `tkinter` library to make a GUI program 


## Motivation
I had a project about supplement feeding for swine, and before the experiment, I had to group the piglets. I randomly grouped them first, 
but the deviation of the piglets' weight was too large, so I spent more than 1 hour arranging the groups. I did the same thing twice for my project, which was really a waste of time.


When I learned Data Science with Python, I created a program to do it for myself and other researchers. And after learning more about Python, 
I built a GUI and shared the Executable file with my friends, which made me full of achievements.


## Get Starting
1. Upload your file with a specific format as the following shows:


<img width="618" alt="input_data" src="https://github.com/luluwu516/GUI_animal_grouper/assets/98475122/0e3cf23a-59df-4264-b601-9c3edc77a6a5">


2. Select the output folder.


<img width="424" alt="success" src="https://github.com/luluwu516/GUI_animal_grouper/assets/98475122/fc62ea0d-818b-4f8c-83c4-0d5fc6bb61e3">


3. Set the group amount.
4. (Optional) If animals are based on gender, please check the checkbox.
5. Adjust the constant, which refers to the acceptable standard deviation. If the animals' weight deviation is low, I recommend adjusting it to under 1.0.
6. Make sure every parameter is correct in the log pane, then click "Confirm."
7. Woala! Here is your grouped data with a summary!


<img width="620" alt="output_data1" src="https://github.com/luluwu516/GUI_animal_grouper/assets/98475122/7d39fe43-cb90-47ef-9dd5-f1ca0244dc67">


If you check based on gender, the output file will have more information, as shown in the following:


![output_data2](https://github.com/luluwu516/GUI_animal_grouper/assets/98475122/a65c0eb1-4b70-4526-a4d2-76b7049e9ce8)


## Problem?
### Failed


<img width="424" alt="fail2" src="https://github.com/luluwu516/GUI_animal_grouper/assets/98475122/a93acf40-d06e-4d1d-a7a0-4fae2c81e074">


For the "Failed" message, please ensure the data is in the correct format and set an available output folder. 


### The diversity of data is too high. 


<img width="424" alt="fail" src="https://github.com/luluwu516/GUI_animal_grouper/assets/98475122/2ea380fb-af6a-47de-8ac2-125c760e7b66">


If you receive the message, "The diversity of data is too high. Please set it to a higher constant." Please adjust the constant to a higher level.
