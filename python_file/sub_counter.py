import time, json, urllib.request
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy.font import proportional, CP437_FONT
from luma.core.render import canvas
from luma.core.legacy import text

def sub_counter():
    
    #create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=32, height=8, block_orientation=-90, rotate=2, contrast=1)
    
    try:
        url = "{API_URL_FOR_YOUR_SOCIAL_MEDIA_PROFILE_GOES_HERE}"
        res = urllib.request.urlopen(url)
        data = json.load(res)
        subs = data['items'][0]['statistics']['subscriberCount']
    except:
        subs='err'

    #draw the display
    with canvas(device) as draw:
        print(subs)
        text(draw, (2, 1), subs, fill="white", font=proportional(CP437_FONT))

if __name__ == "__main__":
    try:
        while(True):
            sub_counter()
            time.sleep(10)
            print("End : %s" % time.ctime())
    except KeyboardInterrupt:
        print("Interrupted : %s" % time.ctime())
