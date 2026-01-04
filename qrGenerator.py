import qrcode

def genQR(url, filepath):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save(filepath)

def main():
    url = input('Enter the URL: ').strip()
    if not url:
        print('URL cannot be empty')
        return
    file_name = input('Enter output file name (default: qrcode.png): ').strip()
    file_name = file_name if file_name else 'qrcode.png'

    genQR(url, file_name)
    print(f'QR Code generated succesfully: {file_name}')

if __name__=="__main__":
    main()