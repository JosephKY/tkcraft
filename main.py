import tkinter as tk
import configLoader
import threading
import render as graphicsRender
root = tk.Tk()
root.resizable(False, False)
config = configLoader.config()

def setWindowSize(width, height):
    root.geometry(str(width) + "x" + str(height))

def setTitle(title):
    root.title(title)

setTitle(config["title"])
setWindowSize(config["width"], config["height"])

thread = None
running = False

def start():
    if(running):
        return
    running = True
    thread = threading.Thread()
    thread.start()

def stop():
    if(not running):
        return
    thread.join()
    running = False

def tick():
    None

def render():
    graphicsRender.main()

def run():
    while(running):
        None

root.mainloop()