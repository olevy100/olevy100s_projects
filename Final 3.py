import psutil
import screen_brightness_control as sbc
import time
        
def set_brightness(level):
    sbc.set_brightness(level)

x = int(input("Set battery percentage at which you would like to change screen brightness: "))
y = int(input("Set screen brightness percentage to change to at set battery percentage: "))

print("Please do not close the window or it won't work")

while True:
    battery = psutil.sensors_battery()
        
    
    if battery.percent <= x:
        set_brightness(y)
    else:
        time.sleep(5)
