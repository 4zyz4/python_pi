import decimal
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("计算圆周率")
        self.geometry("400x300")
        self.minsize(400, 300)

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.label = ttk.Label(
            self.main_frame, text="输入需要计算的位数：", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = ttk.Entry(
            self.main_frame, width=30, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.button = ttk.Button(
            self.main_frame, text="开始计算", command=self.compute_pi)
        self.button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(
            self.main_frame, orient=tk.HORIZONTAL, mode='determinate')
        self.progress_bar.pack(pady=10, fill=tk.X, padx=20)

        self.result_text = tk.Text(self.main_frame, font=("Arial", 10))
        self.scroll_bar = tk.Scrollbar(self.main_frame)
        self.scroll_bar.config(command=self.result_text.yview)
        self.result_text.config(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def compute_pi(self):
        decimal.getcontext().prec = int(self.entry.get())+1

        pi_generator = self.calculate_pi()
        a = next(pi_generator)
        sss=0
        self.result_text.configure(state='normal')  # 启用
        for i in range(int(self.entry.get())+1):
            sss+=1
            if sss%100==0:
                self.progress_bar['value'] = i / int(self.entry.get()) * 100
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, "正在计算……,临时值："+str(a))
                self.update()
            b = a
            a = next(pi_generator)
            if a == b:
                self.progress_bar['value'] = 100
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, "结果是："+str(next(pi_generator)))
                tkinter.messagebox.showinfo(title='计算完毕',message='此次计算已经成功完成！')
                self.result_text.configure(state='disabled')  # 禁用
                break


    def calculate_pi(self):
        pi = decimal.Decimal(0)
        k = 0
        while True:
            pi += decimal.Decimal(1) / (16 ** k) * (
                decimal.Decimal(4) / (8 * k + 1) -
                decimal.Decimal(2) / (8 * k + 4) -
                decimal.Decimal(1) / (8 * k + 5) -
                decimal.Decimal(1) / (8 * k + 6))
            k += 1
            yield pi

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
