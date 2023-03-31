# Notification-System
This was one of my first projects in python. I was following a Youtube Course and this task was given there.
*****
A programmer works 9 to 5 from Monday to Friday. Write a program for him to perform following tasks:
1. Drink 3.5 L of water during his working day. Assume he takes 250mL at a time.
2. Perform eye exercise every 30 minutes.
3. Perform a physical activity every 45 minutes.

A log must be made when the programmer does these tasks in three .txt files(for each task)
An alarm must ring to notify the programmer.
*****

I used the pygame module to ring his alarm.
Also I felt like there might be a chance of the three tasks coincinding. So I decided to use a main file which the programmer will run.
This file will then import functions for each task from three other files. The reason for doing this is that I wanted to try out the multi threading.
I run the three functions concurrently using Threadpool.
