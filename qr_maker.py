qr_text = "hello namskar"

import qrcode
img = qrcode.make(qr_text)
type(img)  # qrcode.image.pil.PilImage
img.save("brp.png")
print(" QR code generated successfully")