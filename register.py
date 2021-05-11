from kakaopy.httpApi import RequestPasscode, RegisterDevice
from main import Main

def register():
  check = str(input("Have you already registered? (y/n) "))
  ID = "Your phone number"
  PW = "Your password"
  device_name = "Any string type"
  uuid = "HSYISYWWYA=="
  
  if check == 'n':
    RequestPasscode(ID, PW, device_name, uuid)
    
    print("Go ahead and check the authentication number on KakaoTalk.")
    Authentication_number = str(input("Authentication_number : "))
    
    RegisterDevice(ID, PW, device_name, uuid, Authentication_number)
    
  client = Main(device_name, uuid)
  client.run(ID, PW)
