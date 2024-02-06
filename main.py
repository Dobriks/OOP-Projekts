import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from mans_modulis import Salidzinajums

class NFLStats:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x700")
        self.root.title("NFL komandu salidzinajums")
        
        
        self.label_team = tk.Label(root, text="Choose NFL Team:")
        self.combo_team = ttk.Combobox(root, values=self.get_teams())
        
        self.btn_compare = ttk.Button(root, text="Compare", command=self.compare_stats)
        
        
        self.result_text = tk.Text(root, height=50, width=85, wrap=tk.WORD)
        self.result_text.config(state=tk.DISABLED)  
        
        
        self.label_team.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.combo_team.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        
        self.btn_compare.grid(row=1, column=0, columnspan=2, pady=20)
        
        
        self.result_text.grid(row=2, column=0, columnspan=2, pady=10)

    def get_teams(self):
        return ["Buffalo Bills", "New England Patriots", "Arizona Cardinals", "Atlanta Falcons", "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns", "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers", "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins", "Minnesota Vikings", "New Orleans Saints", "New York Giants", "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers", "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"]

    def compare_stats(self):
        try:
            team_name = self.combo_team.get()

            compare = Salidzinajums("statistika.csv")

            
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.config(state=tk.DISABLED)

            
            import sys
            sys.stdout = self

            
            year1 = 2022
            year2 = 2023

            compare.kom_salidzinajums(team_name, year1, year2)

            
            sys.stdout = sys.__stdout__

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input: {str(ve)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def write(self, text):
        
        self.result_text.config(state=tk.NORMAL)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = NFLStats(root)
    root.mainloop()


