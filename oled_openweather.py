import requests
import json
import time
from io import BytesIO
from PIL import Image
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
# airvisualapi_key = "your_airvisual_api_key"
# openweatherapi_key = "your_openweather_api_key"
airvisualapi_key = "Your_key" #https://www.iqair.com/vietnam/da-nang  create an account
openweatherapi_key = "Your_key" #https://openweathermap.org/api  create an account

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

def get_data():
    # Get latitude and longitude of nearest city from Air Visual
    url = "http://api.airvisual.com/v2/nearest_city?key=" + airvisualapi_key
    response = requests.request('GET', url)
    raw_data = json.loads(response.text)
    measurements = []
    # print(raw_data)
    lon = raw_data["data"]["location"]["coordinates"][0]
    lat = raw_data["data"]["location"]["coordinates"][1]
    print("Latitude is ", lat, "Longitude is ", lon)
    # Get weather from OpenWeather using latitude and longitude from Air Visua;
    exclude = "current,minutely,daily"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}&units=metric".format(
        lat, lon, exclude, openweatherapi_key)
    response = requests.get(url)
    data = json.loads(response.text)
    # to make data more readable
    #data = json.dumps(data, indent=4) #This prints the json in a readable format
    #print(data)
    return data

weather_data = get_data()
print("Temp is",weather_data["hourly"][0]['temp'],"C")
print("Pressure is",weather_data["hourly"][0]['pressure'],"hPa")
print("Humidity is ",weather_data["hourly"][0]['humidity'],"%")


   # Write  text.

draw.text((x, top + 0),"Temp is " +str(weather_data["hourly"][0]['temp']) +" C", font=font, fill=255)
draw.text((x, top +12),"Pressure is " +str(weather_data["hourly"][0]['pressure']) +" mPa", font=font, fill=255)
draw.text((x,top +22),"Humidity is " +str(weather_data["hourly"][0]['humidity']) +" %", font=font, fill=255)
# Display image
disp.image(image)
disp.show()
time.sleep(5)
# Clear the display.  Always call show after changing pixels to make the display
# update visible!
disp.fill(0)
disp.show()

