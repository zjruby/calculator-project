import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self,root):
        self.root=root
        self.root.title("加减计算器")
        self.root.geometry("500x200")

    #创建输入框
        self.num1_entry = ttk.Entry(root,width=10,font=('Arial',12))
        self.num1_entry.grid(row=0,column=0,padx=10,pady=10)

    #创建运算符选择
        self.operator=tk.StringVar(value="+")
        operator_frame=ttk.Frame(root)
        operator_frame.grid(row=0,column=1,padx=10)
        #为Radiobutton添加grid布局显示
        ttk.Radiobutton(operator_frame,text="+",variable=self.operator,value="+").grid(row=0,column=0)
        ttk.Radiobutton(operator_frame,text="-",variable=self.operator,value="-").grid(row=1,column=0)

    #第二个数字输入框
        self.num2_entry=ttk.Entry(root,width=10,font=('Arial',12))
        self.num2_entry.grid(row=0,column=2,padx=10,pady=20)

    #等号按钮
        ttk.Button(root,text="=",command=self.calculate).grid(row=0,column=3,padx=10)

    #显示结果
        self.result_var=tk.StringVar(value="结果")
        ttk.Label(root,textvariable=self.result_var, font=('Arial',12)).grid(row=1,column=0,columnspan=4,pady=10)

    def calculate(self):
        try:
            num1=float(self.num1_entry.get())
            num2=float(self.num2_entry.get())
            op=self.operator.get()

            if op=="+":
                result=num1+num2
            else:
                result=num1-num2

            self.result_var.set(f"结果:{result}")
        except ValueError:
            self.result_var.set("请输入有效数字")

if __name__=="__main__":
    root=tk.Tk()
    app=CalculatorApp(root)
    root.mainloop()