# wifi-block-bypass
A program for **Windows** devices that allows you to bypass parental internet restrictions (block)

# How to use
1. Run `WifiBlockBypass_v1.x.x` as Administrator. Make sure that you're **trying** to connect to the WiFi. You don't need to have connection.
2. Close the program and restart your computer.
3. Repeat these steps this program every time you shut down / restart your computer (if your internet remains unblocked).

# How it works
The executable will create a key in your Regedit (Windows Registry) called `NetworkAddress` if one doesn't already exist.
If one does exist, it will increment the value of that key by 1 every time you run it.
This is crucial, as your internet provider updates it's status on your device upon it being restarted.
That's why the program has to change the value every time you restart your PC in order for the bypass to work.
A simple solution to this (to avoid restarting your PC right after you've already restarted it) is to run the executable right before you're shutting down your device.

*Note: This is a known solution to fix internet restrictions and all this program does is automate the process, making it much simpler.
