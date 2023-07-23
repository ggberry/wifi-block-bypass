# wifi-block-bypass
A program for **Windows** devices that allows you to bypass parental internet restrictions (block)

# How to use
1. Run `WifiBlockBypass_v1.x.x` as Administrator. Make sure that you're **trying** to connect to the WiFi. You don't need to have connection.
2. Close the program and restart your computer.
3. Repeat these steps this program every time you shut down / restart your computer (if your internet remains unblocked).

# How it works
The executable will create a key in your Regedit (Windows Registry) called `NetworkAddress` if one doesn't already exist.<br />
If one does exist, it will increment the value of that key by 1 every time you run it.<br />
This is crucial, as your internet provider updates it's status on your device upon it being restarted.<br />
That's why the program has to change the value every time you restart your PC in order for the bypass to work. Simple switching between two values doesn't work either, since you can only use new values. This is fine however, as there is a sufficient ammount of combinations to last for a life time.<br />
To avoid restarting your PC right after you've already restarted it, run the executable right before you're shutting down your device.<br /><br />

*Note: This is a known solution to fix internet restrictions and all this program does is automate the process, making it much simpler.
