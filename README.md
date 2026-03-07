# Samsung-DeX-for-PC-with-scrcpy
Get Samsung DeX on your PC bypassing the One UI 6.1 and earlier restriction and stuff!

Hi there! Today we are going to show you how to run Samsung DeX on DeX supported devices with your Laptop or a PC!

(BTW Github please don't sue me for copying other projects or really it's just other project but I give credits by giving links to their repository!)

## Getting Started

Here are the things you need:

● A Samsung DeX supported phone

● A Laptop or a Computer with a USB-A Port (USB 3.0 works better but if your Laptop or Computrr doesn't have it. Then what Computer is it? BTW no offense intended for MacBooks hehe just get a type c hub idk.)

● A Usb-A to Type-C (or whatever your port is) cable
## Preparing the files

First let's get the files! Click on the links or follow the instructions to get the files.

● [Scrcpy](https://github.com/Genymobile/scrcpy)

● The .bat file
To get the .bat file to run scrcpy, first you will need to go to the very top and click on the green Code button. A menu will appear. Click Download ZIP and we will extract it later.

## Setting up the devices
● DeX supported phone
1. Open the control center and find DeX or Wireless DeX to make sure your device supports Samsung Dex
2. Open Settings and go to About phone.
3. Go to Software information and click the Bulid Number exactly 7 times. Type in your password.
4. Go back to the main settings page (not the about phone sub page!) and Go to Developer Options.
5. Scroll down until you find USB Debugging.
6. Switch it on and a warning will appear. Click OK.

● The Laptop or Computer
Windows 7/8/8.1/10/11
1. Press ⊞+X on your Keyboard and press M.
2. A window will pop up. Now click on Universal Serial Bus controllers.
3. Now right click USB Root Hub (USB 3.0) or other listed USB Root Hubs and click Update driver.
4. Click on Search automatically for drivers.
5. If The best drivers for your device are already installed shows up, you can go on to the next main steps.
6. Now for people with errors or if needs to update click Update The latest Drivers from (Your manufacturer for your PC)
7. Once done  right click the driver again and click Disable device.
8. Now use your touchpad or Bluetooth mouse to right click again and click Enable device. (If your mouse is wired and you don't know how to use the touchpad you cab click the bottom right corner of the touchpad or for some laptops you can find two buttons like me so just click on the right one.![12112](https://github.com/user-attachments/assets/22733be1-f6c2-4f5e-8f7a-eefc7b45aeae)

● macOS users and Linux users. You are my best friend now cuz you don't need to do and now scram onto the next step!

## Extracting and running

1. Put both .zip files into a safe folder or place (Like the Documents Folder)
2. First extract the scrcpy file.
3. Then move the code zip into the insides of scrcpy where you can find lots of confusing .bats .exe files and stuff.
4. Now extract the zip and make sure to tell the OS to not extract in a subfolder. (On Windows, this is usually done by removing the folder name and the \ after the main structure. For example:
![12115](https://github.com/user-attachments/assets/1c000282-4433-493e-96d3-b77c34fe35b5)
(Also don't do this on scrcpy cause I wrote this before I uploaded the files.)

5.Now after extracting you can find a file called Start_DeX.bat in the scrcpy folder or the Start_DeX.command or Start_DeX.py. Now, continue the steps with your OS.

● Windows

6.  Right click on the Start_DeX.bat and select Open in Notepad. A Notepad window will appear. The window should look like this.

````@cmd && scrcpy --new-display=[YOUR DISPLAY RES]/160 --mouse=uhid --keyboard=uhid````

Now right click on your desktop and click Display Settings.

8. Scroll down until you find Display resolution. The number under it will be your Display size for example let's assume your Display is 1366 x 768

9. Open Notepad and find the line with --new-display=[YOUR DISPLAY RES]/160 and change the [YOUR DISPLAY RES] part into the numbers you found. For example: --new-display=1366x768/160
10. Click File on the top bar then click Save

●macOS

6. Right click the Start_DeX and Hover Open with and select TextEdit. If TextEdit isn't listed, click on Other instead and click on the enable dropdown and click All Applications and find TextEdit and click it.

7. Now click the Apple Menu and click System Settings. Go to Displays. ​You will see a list of icons like "Larger Text" or "More Space." Hover your mouse over your current selection, and a pop-up will show the exact pixel numbers. For example, let's assume it shows 1440 x 900.
8. Go back to TextEdit and find the line with --new-display=[YOUR DISPLAY RES]/160 and change the [YOUR DISPLAY RES] part into the numbers you found. For example: --new-display=1440x900/160 and on the top menu click File and click Save.

● Linux
