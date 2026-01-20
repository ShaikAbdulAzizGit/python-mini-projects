
import qrcode
from PIL import Image
import os 
def customized_qr_code_generator(data,title,size=10,border=4,fill_color="black",back_color="white"):
    try:
        qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,#Sets error correction to the highest level (H), which allows the QR code to be read even if up to 30% of the data is damaged.
        box_size=size,#Sets the size of each box in the QR code grid (pixels).
        border=border)#Sets the thickness of the border (measured in boxes).

        qr.add_data(data)
        qr.make(fit=True)


        img=qr.make_image(fill_color=fill_color,back_color=back_color)

        img.show()
        validity=input("If you want to save this qr code then press (Y) in your key board \n other wise press (N) it will be cancelled  ->:")
        if validity=="Y" or validity=="y":
            folder="Generated_qrcodes"
            os.makedirs(folder,exist_ok=True)

            file_path=os.path.join(folder,f"{title}.png")
            img.save(file_path)
            print("Qr code created and saved successfully")
        else:
            print("Qr code not saved")
            return
    except Exception as e : 
        print("some error occured please try again carefully :->",e)
    
if __name__ == "__main__":
    print("welcome to advance qr code generator ")
    data=input("Enter the url,text to generate the qr code : ").strip()
    if not data: 
        print("Data cannot be empty ")
        exit()
    title=input("Enter the title for the qr code ").replace(" ","").strip()
    if not title:
        print("Title cannot be empty ")
        exit()
    print("Qr code customizations : ")
    size=int(input("Enter the box size (default:10)")or 10)
    border=int(input("Enter the border size (default:4)")or 4)
    fill_color=input("Enter the qr code color (default:black)").lower().strip()
    back_color=input("Enter the background color (default:white)").lower().strip()

    customized_qr_code_generator(data,title,size,border,fill_color,back_color)
