import os
import winreg as reg

def AddToRegistry():
    pth = os.path.dirname(os.path.realpath(__file__))
    # name of the python file with extension
    s_name = "downloads-cleanup.py"

    # joins the file name to end of path address
    # address = os.join(pth, s_name)
    address = pth + s_name
    # key we want to change is HKEY_CURRENT_USER
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    # open the key to make changes to
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)

    # modifiy the opened key
    reg.SetValueEx(open, "downloads_cleanup", 0, reg.REG_SZ, address)

    # now close the opened key
    reg.CloseKey(open)


# Driver Code
if __name__ == "__main__":
    AddToRegistry()
