# Camera thing
This code works by using a USB camera plugged in to any device that can run python (in my case a raspberry pi 1).
In config you can select how many seconds to sample background and the interval at which to check for differences and save images. 
You can also change the allowed threshold in config as well as what area to check.
Images will be saved to /images

## Run script
You can run camera script as a cron job but I recomend you run it as a systemd service instead as that makes the script run at a time when you are sure camera is initialized and a service can also restart script for you in the case of crashes. **Make sure** to set the working directory in the service to that of the directory the script is in as else the script will get confused when trying to save images and loading config file.

## Recomended cron jobs
* `@reboot cd <dir here> && python3 server.py` start image server in bootup (not needed necessarily)
* `@midnight tar -zcvf "/<dir here>/backups/$(date '+%Y-%m-%d').tar.gz" /<dir here>/images --remove-files` save images as compressed tar every day at 00:00. Will save memory

## connect to image server
if your computer is on same network you can simply open `http://<HOSTNAME HERE>:3000` in any browser. 
If your computer has no ethernet or wifi connected you can plug in an iPhone for example and turn on hotspot and click "trust this computer". After that is done navigate to `http://<HOSTNAME HERE>.local:3000`