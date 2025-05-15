import qrcode #library 

text = input("Enter the text or Url to be converted in Qrcode: ")

filename = input ("Enter filename to save the qrcode image : ")


def generate_qr_code(text, filename):
    
    #convert text or url to qrcode
    
    image_qrcode = qrcode.make(text) #qr code image converter and save that
    
    #save the qrcode image
    
    image_qrcode.save(filename)
    
generate_qr_code(text, filename)