qr_text = "hari bist" 
import qrcode
img = qrcode.make(qr_text)
type(img)  # qrcode.image.pil.PilImage
img.save("HAri.png")
print(" QR code generated successfully")