import socket
import qrcode

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
finally:
    s.close()

url = f"http://{ip_address}:8080"

img = qrcode.make(url)
img.save("shared-files/qr.png")

print(f"QR Code generated for: {url}")