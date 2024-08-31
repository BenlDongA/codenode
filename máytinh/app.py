import tkinter as tk

# Hàm để thực hiện phép toán
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')

# Hàm để thêm ký tự vào màn hình
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Hàm để xóa màn hình
def clear_display():
    entry.delete(0, tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Máy Tính")

# Tạo trường nhập liệu
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Tạo các nút máy tính
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Đặt các nút vào lưới và gán hành động
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        b = tk.Button(root, text=button, width=5, height=2, command=evaluate_expression)
    elif button == 'C':
        b = tk.Button(root, text=button, width=5, height=2, command=clear_display)
    else:
        b = tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b))
    b.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Chạy ứng dụng
root.mainloop()
