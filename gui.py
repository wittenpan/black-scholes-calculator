
from test import BlackScholesModel
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Black Scholes Model Heatmap")
        #input fields for the user
        self.create_input_fields()
        #buttons
        self.create_buttons()
    def create_input_fields(self):
        self.labels = ["Time to Maturity", "Strike", "Current Price","Volatility","Interest Rate"]
        self.entries={}
        for i, label in enumerate(self.labels):
            ttk.Label(self.root,text=label).grid(row=i,column=0)
            entry = ttk.Entry(self.root)
            entry.grid(row=i,colum=1,padx=5,pady=5)
            self.entries[label] = entry
    def create_buttons(self):
        generate_button = ttk.Button(self.root,text="Generate Heatmap",command = self.generate_heatmap)
        generate_button.grid(row=len(self.labels),column=0,columnspan=2,pady=10)