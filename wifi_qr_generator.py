qr_text = "WIFI:T:WAP;S:Namaste WiFi-2.4g-C301;P:9427D6F5;;" 
import qrcode
img = qrcode.make(qr_text)
type(img)  # qrcode.image.pil.PilImage
img.save("ntc_password.png")
print(" QR code generated successfully")