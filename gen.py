import qrcode
import image
from colorama import Fore

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/channel/UCillU39POZVNHLLkKo2iD6w')
qr.make(fit=True)

print(Fore.RED + '''
    ╔════════════════════════════════════════════╗
    ║                                            ║ 
    ║       QR CODE GENERATO CON SUCCESSO!       ║ 
    ║                                            ║ 
    ╚════════════════════════════════════════════╝
				''',Fore.RED, Fore.WHITE, Fore.BLACK)


img = qr.make_image()
img.save("testqr.png")
