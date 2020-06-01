#sub_counter

sub_counter is a project which utilizes a Raspberry Pi and an 
LED matrix to display a subscriber number from a social media
site profile. 

The python file can be set up to fetch subscriber information
from an API at a given interval (every second, every hour, every
day) and then display it to the matrix.

This project uses the luma library to create the virtual image
for the LED matrix and then draw that image to the LED matrix.

The idea for this project hit me when I was in Belgium a few
years ago in a bar in Brussels and noticed that the bar had
a subscriber counter for their Instagram account. It was hanging
on the wall and analog-based, like an old clock radio where the
numbers switch via small plastic flappers in real-time. You could
pull out your phone and follow/unfollow the bar and watch the
count change. Curious about this, I looked up these devices 
online to find that they cost several 1000s of dollars! 

I thought it would be fun to make a simple, cost effective 
one. With all of the parts included, depending on what Raspberry
Pi unit you have, this would cost at most $50, although you might 
want to spend additional money on a some sort of case. Also, 
depending on how big of a display you want, and how many 
subscribers you want to display, you may need to cascade several
of the display units together.

I used the HiLetGo MAX7219 Dot Matrix Module for this project.
They are $8.50 USD on Amazon:
https://www.amazon.com/s?k=8x8+LED+Matrix

I am using the Raspberry Pi 4 4GB for prototyping but any unit
with GPIO pins for the LED matrix and Internet connectivity will
work well.

Special thanks to Wayne at devscover.com for inspiring this
project.
