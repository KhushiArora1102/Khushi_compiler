from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import parser

exp = "9-5+4*2"
print(exp)
st = parser.expr(exp)
print(st)
code = st.compile()
print(code)
res = eval(code)
print(res)

compiler = Tk()
compiler.title('Welcome to my Compiler')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python3 Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python3 Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Program ran successfully, you can save the code')
        text.pack()
        return
    command = f'python3 {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Execute', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
