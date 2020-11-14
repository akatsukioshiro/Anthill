
######### IMPORT/DECLARATION #######

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import ubinascii

print("Started ESP")

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Aswathy'
password = 'viju@1967'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
led = Pin(2, Pin.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

####################################
############## RE-USABLE ###########

def send_header(conn,http_code,http_status):
  conn.send('HTTP/1.1 '+str(http_code)+' '+str(http_status)+'\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Access-Control-Allow-Origin: *\n')
  conn.send('Access-Control-Allow-Headers: Authorization, Content-Type\n')
  conn.send('Access-Control-Allow-Methods: GET\n')
  conn.send('Connection: close\n\n')

def send_content(conn,response):
  conn.sendall(response)

def receive_content():
  conn, addr = s.accept()
  request = str(conn.recv(1024))
  return [conn,request]

####################################
############### SETUP ##############

def update_status():
  if led.value() == 1:
    resp="ON"
  else:
    resp="OFF"
  return resp

def web_page():
  with open("webpage.html","r") as f:
    html=f.read().replace("**STATUS**",update_status())
  return html

def web_interface(conn):
  response = web_page()
  send_content(conn,response)

####################################
############### LOOP ###############

def get_mac(conn,request):
  mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
  show_mac= request.find('/?mac=show')
  if show_mac == 6:
    send_header(conn,200,"OK")
    send_content(conn,mac)

def led_control(conn,request):
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  led_status=""
  if led_on == 6:
    print('LED ON')
    led_status='LED ON'
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led_status='LED OFF'
    led.value(0)
  send_header(conn,200,"OK")
  send_content(conn,led_status)

def control_center():
  global toggler,series
  connect=receive_content()
  if connect[1].find('/?') != 6:
    web_interface(connect[0])
  else:
    if connect[1].find('/?led') == 6:
      led_control(connect[0],connect[1])
    elif connect[1].find('/?mac') == 6:
      get_mac(connect[0],connect[1])
  connect[0].close()

####################################

while True:
  control_center()

