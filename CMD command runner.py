# CMD RUNNER
#command ="netstat -an"
import tkinter as tk
import subprocess
window=tk.Tk()
window.title("APP")
window.geometry('500x500')
label=tk.Label(window,text="Enter cmd command for prompt")
label.pack(padx=10)

#function for result
def result():
       command = text.get()
       result = subprocess.run(command, shell=True, capture_output=True, text=True)
       output.insert(tk.END,result.stdout + result.stderr)
               

bt=tk.Button(window,text="Run",bg="Black",fg="White",command=result)
bt.pack(padx=10,pady=5)

#entry from user
text=tk.Entry(window,width=100)
text.pack(padx=10,pady=5)

#output screen
output = tk.Text(window, height=20, width=60)
output.pack(padx=10, pady=10)

window.mainloop()
