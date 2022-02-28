import tkinter as tk
def main():
        window = tk.Tk()
        text = tk.Text(window, height=10, width=30)
        text.pack()
        for i in range(1,10):
                text.insert(tk.END, 'Hello\n')
        tk.mainloop()

if __name__ == '__main__':
	main()
	
