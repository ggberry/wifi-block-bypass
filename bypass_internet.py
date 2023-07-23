import sys
import winreg
import socket
import subprocess
import re

from contextlib import suppress

import pyuac
from pyuac import main_requires_admin


def get_class(root, target, path, hkey=winreg.HKEY_LOCAL_MACHINE, flags=0):
    with suppress(WindowsError), winreg.OpenKey(hkey, path, 0, winreg.KEY_READ | flags):
        for i in range(1, 13 + 1):
            f = f"000{i}"
            t = winreg.QueryValueEx(winreg.OpenKeyEx(root, path + "\\" + f), "NetCfgInstanceId")[0]
            if t == target:
                return f


def set_value_in_registry(target, subkey, type, value):
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, target, access=winreg.KEY_WRITE) as regkey:
        winreg.SetValueEx(regkey, subkey, 0, type, value)


def create_new_network_address(root, subkey, name, value="DE0000000000"):
    print("NetworkAddress file not found! Creating new one with default value: DE0000000000")
    with winreg.CreateKeyEx(root, subkey, 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)


def get_next_network_address(root, target, subfolder):
    subkey = target + "\\" + subfolder
    target_key = winreg.OpenKeyEx(root, subkey)

    try:
        winreg.QueryValueEx(target_key, "NetworkAddress")
    except:
        create_new_network_address(root, subkey, "NetworkAddress")

    current, type_ = winreg.QueryValueEx(target_key, "NetworkAddress")
    value = str(current[:-1]) + str(int(current[-1]) + 1)

    return {"value": value, "type": type_}

def main():
    try:
        input("Warning 1/3: Are you sure you want to proceed?")
        input("Warning 2/3: Are you sure you want to proceed?")
        input("Warning 3/3: Are you sure you want to proceed?")
        print("Proceeding.")

        HOST = socket.gethostname()
        GETMAC = str(subprocess.check_output(["getmac"]))
        TARGET = re.search("\{(.*?)}", GETMAC).group()

        root = winreg.ConnectRegistry(HOST, winreg.HKEY_LOCAL_MACHINE)
        target = r"SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}"
        subfolder = get_class(root, TARGET, target)
        nw_addr = get_next_network_address(root, target, subfolder)
        set_value_in_registry(target + "\\" + subfolder, "NetworkAddress", nw_addr["type"], nw_addr["value"])

        input("Successfully ticked NetworkAddress! Restart your PC to bypass the internet")

    except OSError as e:
        input(f"An error occurred: {e}")


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin! You can safely close this tab.")
        pyuac.runAsAdmin()
        sys.exit()
    else:
        main()
