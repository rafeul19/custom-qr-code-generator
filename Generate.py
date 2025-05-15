import qrcode #library 

#text = input("Enter the text or Url to be converted in Qrcode: ")

#filename = input ("Enter filename to save the qrcode image : ")


def generate_qr_code(filepath="input.txt"):
    
    
    
    with open(filepath, "r") as file:
        lines =file.readlines()
        
    text = lines[0].strip()
    filename = lines[1].strip()
    
    
    
    #convert text or url to qrcode
    
    image_qrcode = qrcode.make(text) #qr code image converter and save that
    
    #save the qrcode image
    
    image_qrcode.save(filename)
    
generate_qr_code("code 2/input.txt")