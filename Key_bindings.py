import pyautogui
import keyboard
import tkinter as tk
from tkinter import messagebox
import json
import os

# 配置文件路径
CONFIG_FILE = "keybindings.json"

# 默认按键配置
DEFAULT_BINDINGS = {
    'ctrl+1': 'sswd',
    'ctrl+2': 'sawaa',
    'ctrl+3': 'qqqqq',
    'ctrl+4': 'wsdaw',
    'ctrl+5': 'wswsw',
    'ctrl+6': 'wswsw'
}

class KeyBindingApp:
    def __init__(self, root):
        # 初始化方法
        self.root = root
        # 设置窗口标题
        self.root.title("按键绑定工具")
        # 设置窗口大小为400x300像素
        self.root.geometry("400x300")
        
        # 加载配置
        self.bindings = self.load_config()
        
        # 创建界面
        self.create_widgets()
        
        # 注册热键
        self.register_hotkeys()
        
        # 窗口关闭时的事件
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        # 标题
        tk.Label(self.root, text="按键绑定配置 ヽ(✿ﾟ▽ﾟ)ノ", font=('Arial', 14)).pack(pady=10)
        
        # 创建输入框
        self.entries = {}
        for i, (hotkey, sequence) in enumerate(self.bindings.items()):
            frame = tk.Frame(self.root)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            tk.Label(frame, text=f"快捷键 {hotkey}:").pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.insert(0, sequence)
            entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            self.entries[hotkey] = entry
        
        # 保存按钮
        tk.Button(self.root, text="保存配置", command=self.save_config).pack(pady=10)
        
        # 状态标签
        self.status_label = tk.Label(self.root, text="注意：此程序完全开源免费。\n GitHub仓库地址: https://github.com/H-ycoor/python_Game_Keybindings", fg="gray")
        self.status_label.pack(pady=5)

    def register_hotkeys(self):
        # 取消所有已注册的热键
        keyboard.unhook_all()
        
        # 注册新的热键
        # 遍历self.bindings字典中的所有热键
        for hotkey in self.bindings.keys():
            keyboard.add_hotkey(hotkey, lambda h=hotkey: self.trigger_sequence(h))

    def trigger_sequence(self, hotkey):
        sequence = self.bindings.get(hotkey, "")
        if sequence:
            pyautogui.typewrite(sequence, interval=0.1)

    def load_config(self):
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"加载配置失败: {e}")
        return DEFAULT_BINDINGS.copy()

    def save_config(self):
        try:
            # 更新绑定
            for hotkey, entry in self.entries.items():
                self.bindings[hotkey] = entry.get()
            
            # 保存到文件
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.bindings, f, indent=4)
            
            # 重新注册热键
            self.register_hotkeys()
            
            messagebox.showinfo("成功", "配置已保存！")
        except Exception as e:
            messagebox.showerror("错误", f"保存配置失败: {e}")

    def on_close(self):
        if messagebox.askokcancel("退出", "确定要退出程序吗？"):
            keyboard.unhook_all()
            self.root.destroy()

    def run(self):
        # 后台监听ESC键
        # def check_esc():
        #     if keyboard.is_pressed('esc'):
        #         self.on_close()
        #     self.root.after(100, check_esc)
        
        # check_esc()
        self.root.mainloop()
    

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyBindingApp(root)
    app.run()
