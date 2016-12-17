# text from https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html

def sleep(ms):
    """sleep for the given number of milliseconds."""

def running_time():
    """returns the number of milliseconds since the micro:bit was last switched on."""

def panic(error_code):
   """makes the micro:bit enter panic mode (this usually happens when the DAL runs out of memory, and causes a sad face to be drawn on the display). The error # code can be any arbitrary integer value."""

def reset():
    """resets the micro:bit."""

class Button:
    def is_pressed():
        """returns True or False to indicate if the button is pressed at the time of the method call."""
    def was_pressed():
        """returns True or False to indicate if the button was pressed since the device started or the last time this method was called."""
    def get_presses():
        """returns the running total of button presses, and resets this counter to zero"""

button_a = Button()
button_b = Button()

class Display:
    def get_pixel(x, y):
        """gets the brightness of the pixel (x,y). Brightness can be from 0 (the pixel is off) to 9 (the pixel is at maximum brightness)."""
    def set_pixel(x, y, val):
        """sets the brightness of the pixel (x,y) to val (between 0 [off] and 9 [max brightness], inclusive)."""
    def clear():
        """clears the display."""
    def show(image, delay=0, wait=True, loop=False, clear=False):
        """shows the image."""
    def show(iterable, delay=400, wait=True, loop=False, clear=False):
        """shows each image or letter in the iterable, with delay ms. in between each."""
    def scroll(string, delay=400):
        """scrolls a string across the display (more exciting than display.show for written messages)."""

display = Display()

class MicroBitPin:
    def write_digital(value):
        """value can be 0, 1, False, True"""
    def read_digital():
        """returns either 1 or 0"""
    def write_analog(value):
        """value is between 0 and 1023"""
    def read_analog():
        """returns an integer between 0 and 1023"""
    def set_analog_period(int):
        """sets the period of the PWM output of the pin in milliseconds (see https://en.wikipedia.org/wiki/Pulse-width_modulation)"""
    def set_analog_period_microseconds(int):
        """sets the period of the PWM output of the pin in microseconds (see https://en.wikipedia.org/wiki/Pulse-width_modulation)"""
    def is_touched():
        pass

pin1 = MicroBitPin()
pin2 = MicroBitPin()
pin3 = MicroBitPin()
pin4 = MicroBitPin()
pin5 = MicroBitPin()
pin6 = MicroBitPin()
pin7 = MicroBitPin()
pin8 = MicroBitPin()
pin9 = MicroBitPin()
pin10 = MicroBitPin()
pin11 = MicroBitPin()
pin12 = MicroBitPin()
pin13 = MicroBitPin()
pin14 = MicroBitPin()
pin15 = MicroBitPin()
pin16 = MicroBitPin()
pin19 = MicroBitPin()
pin20 = MicroBitPin()

# to do: Images
# to do: The accelerometer
# to do: The compass
# to do: I2C bus
# to do: UART
