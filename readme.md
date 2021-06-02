# Camera thing
This code works by using a USB camera plugged in to any device that can run python (in my case a raspberry pi 1).
In config you can select how many seconds to sample background and the interval at which to check for differences and save images. 
You can also change the allowed threshold in config as well as what area to check.
Images will be saved to /images

## Recomended cron jobs
* `@reboot python3 /<dir here>/main.py` start script at bootup
* `@reboot python3 /<dir here>/server.py` start image server in bootup (not needed necessarily)
* `@midnight tar -zcvf "/<dir here>/backups/$(date '+%Y-%m-%d').tar.gz" /<dir here>/images --remove-files` save images as compressed tar every day at 00:00. Will save memory

## connect to image server
if your computer is on same network you can simply open `http://<HOSTNAME HERE>:3000` in any browser. 
If your computer has no ethernet or wifi connected you can plug in an iPhone for example and turn on hotspot and click "trust this computer". After that is done navigate to `http://<HOSTNAME HERE>.local:3000`