# text from https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html

def sleep(ms):
    """sleep for the given number of milliseconds."""

def running_time():
    """returns the number of milliseconds since the micro:bit was last switched on."""

def panic(error_code):
   """makes the micro:bit enter panic mode (this usually happens when the DAL runs out of memory, and causes a sad face to be drawn on the display). The error # code can be any arbitrary integer value."""

def reset():
    """resets the micro:bit."""

class _Button:
    def is_pressed():
        """returns True or False to indicate if the button is pressed at the time of the method call."""
    def was_pressed():
        """returns True or False to indicate if the button was pressed since the device started or the last time this method was called."""
    def get_presses():
        """returns the running total of button presses, and resets this counter to zero"""

button_a = _Button()
button_b = _Button()

class _Display:
    def get_pixel(self, x, y):
        """ARTASASD the brightness of the pixel (x,y). Brightness can be from 0 (the pixel is off) to 9 (the pixel is at maximum brightness)."""
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

display = _Display()

class _MicroBitPin:
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

pin1 = _MicroBitPin()
pin2 = _MicroBitPin()
pin3 = _MicroBitPin()
pin4 = _MicroBitPin()
pin5 = _MicroBitPin()
pin6 = _MicroBitPin()
pin7 = _MicroBitPin()
pin8 = _MicroBitPin()
pin9 = _MicroBitPin()
pin10 = _MicroBitPin()
pin11 = _MicroBitPin()
pin12 = _MicroBitPin()
pin13 = _MicroBitPin()
pin14 = _MicroBitPin()
pin15 = _MicroBitPin()
pin16 = _MicroBitPin()
pin19 = _MicroBitPin()
pin20 = _MicroBitPin()

# to do: Images
# to do: The accelerometer
# to do: The compass
# to do: I2C bus
# to do: UART
