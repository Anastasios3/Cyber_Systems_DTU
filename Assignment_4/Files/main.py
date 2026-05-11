import network  # type: ignore
import socket
import machine  # type: ignore
import ujson    # type: ignore
from machine import Pin, ADC, I2C  # type: ignore

AP_SSID = "ESP32-ANASTASIOS_TATARAKIS"
AP_PASSWORD = "yourpass1"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=AP_SSID, authmode=3, password=AP_PASSWORD)

btn1 = Pin(21, Pin.IN, Pin.PULL_UP)

led = Pin(13, Pin.OUT)
led.value(0)

rgb_r = Pin(32, Pin.OUT)
rgb_g = Pin(15, Pin.OUT)
rgb_b = Pin(14, Pin.OUT)
rgb_r.value(0)
rgb_g.value(0)
rgb_b.value(0)

pot_adc = ADC(Pin(33))
pot_adc.atten(ADC.ATTN_11DB)

i2c = I2C(0, scl=Pin(22), sda=Pin(23), freq=100000)
MCP_ADDR = 0x18

def read_pot():
    return pot_adc.read()

def read_temp():
    data = i2c.readfrom_mem(MCP_ADDR, 0x05, 2)
    raw = ((data[0] & 0x1F) << 8) | data[1]
    if raw > 4095:
        raw -= 8192
    temp_c = raw * 0.0625
    return temp_c

digital_pins = {
    "btn1": btn1,
    "led": led,
    "rgb_r": rgb_r,
    "rgb_g": rgb_g,
    "rgb_b": rgb_b,
}

sensors = {
    "pot": read_pot,
    "temp": read_temp,
}

def html_status_page():
    rows = ""
    for name, p in digital_pins.items():
        val = p.value()
        rows += "<tr><td>{}</td><td>{}</td></tr>".format(name, val)

    try:
        pot_val = read_pot()
        rows += "<tr><td>pot</td><td>{}</td></tr>".format(pot_val)
    except Exception as e:
        rows += "<tr><td>pot</td><td>ERROR: {}</td></tr>".format(e)

    try:
        temp_val = read_temp()
        rows += "<tr><td>temp</td><td>{:.2f} C</td></tr>".format(temp_val)
    except Exception as e:
        rows += "<tr><td>temp</td><td>ERROR: {}</td></tr>".format(e)

    html = """<!DOCTYPE html>
<html>
  <head><title>ESP32 status</title></head>
  <body>
    <h1>ESP32 IO status</h1>
    <table border="1">
      <tr><th>Name</th><th>Value</th></tr>
      {}
    </table>
  </body>
</html>
""".format(rows)
    return html

def http_response_header(code, content_type="text/html"):
    if code == 200:
        status_line = "HTTP/1.0 200 OK\r\n"
    elif code == 404:
        status_line = "HTTP/1.0 404 Not Found\r\n"
    else:
        status_line = "HTTP/1.0 500 Internal Server Error\r\n"
    headers = status_line + "Content-Type: {}\r\n\r\n".format(content_type)
    return headers

def handle_api(path_parts):
    if len(path_parts) == 2 and path_parts[1] == "pins":
        body = ujson.dumps({"pins": list(digital_pins.keys())})
        return 200, "application/json", body

    if len(path_parts) == 2 and path_parts[1] == "sensors":
        body = ujson.dumps({"sensors": list(sensors.keys())})
        return 200, "application/json", body

    if len(path_parts) == 3 and path_parts[1] == "pin":
        name = path_parts[2]
        pin = digital_pins.get(name)
        if pin is None:
            body = ujson.dumps({"error": "unknown pin"})
            return 404, "application/json", body
        value = pin.value()
        body = ujson.dumps({"name": name, "value": int(value)})
        return 200, "application/json", body

    if len(path_parts) == 3 and path_parts[1] == "sensor":
        name = path_parts[2]
        func = sensors.get(name)
        if func is None:
            body = ujson.dumps({"error": "unknown sensor"})
            return 404, "application/json", body
        value = func()
        body = ujson.dumps({"name": name, "value": value})
        return 200, "application/json", body

    if len(path_parts) == 5 and path_parts[1] == "pin" and path_parts[3] == "set":
        name = path_parts[2]
        action = path_parts[4]
        pin = digital_pins.get(name)
        if pin is None:
            body = ujson.dumps({"error": "unknown pin"})
            return 404, "application/json", body
        if action == "high":
            pin.value(1)
        elif action == "low":
            pin.value(0)
        else:
            body = ujson.dumps({"error": "unknown action"})
            return 404, "application/json", body
        body = ujson.dumps({"name": name, "value": int(pin.value())})
        return 200, "application/json", body

    if len(path_parts) == 5 and path_parts[1] == "rgb":
        try:
            r = int(path_parts[2])
            g = int(path_parts[3])
            b = int(path_parts[4])
        except ValueError:
            body = ujson.dumps({"error": "bad rgb values"})
            return 404, "application/json", body

        rgb_r.value(1 if r > 0 else 0)
        rgb_g.value(1 if g > 0 else 0)
        rgb_b.value(1 if b > 0 else 0)

        body = ujson.dumps({
            "rgb": [int(rgb_r.value()), int(rgb_g.value()), int(rgb_b.value())]
        })
        return 200, "application/json", body

    body = ujson.dumps({"error": "unknown resource"})
    return 404, "application/json", body

def run_server():
    addr_info = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr_info)
    s.listen(1)
    print("listening on", addr_info)

    while True:
        client_sock, client_addr = s.accept()
        try:
            print("client connected from", client_addr)
            client_file = client_sock.makefile("rwb", 0)
            request_line = client_file.readline()
            if not request_line:
                client_sock.close()
                continue
            
            while True:
                line = client_file.readline()
                if not line or line == b'\r\n':
                    break 

            try:
                request = request_line.decode("utf8")
            except:
                client_sock.close()
                continue

            print("request:", request.strip())
            parts = request.split()
            if len(parts) < 2:
                client_sock.close()
                continue

            method = parts[0]
            path = parts[1]

            if method != "GET":
                header = http_response_header(404)
                client_sock.send(header.encode("utf8"))
                client_sock.close()
                continue

            path_no_query = path.split("?", 1)[0]
            path_parts = path_no_query.split("/")

            if path_no_query == "/" or path_no_query == "/index.html":
                html = html_status_page()
                header = http_response_header(200, "text/html")
                client_sock.send(header.encode("utf8"))
                client_sock.send(html.encode("utf8"))
            else:
                code, ctype, body = handle_api(path_parts)
                header = http_response_header(code, ctype)
                client_sock.send(header.encode("utf8"))
                client_sock.send(body.encode("utf8"))

            client_sock.close()

        except Exception as e:
            try:
                header = http_response_header(500)
                client_sock.send(header.encode("utf8"))
                msg = "error: {}".format(e)
                client_sock.send(msg.encode("utf8"))
                client_sock.close()
            except:
                pass

run_server()