from plyer import notification
import time
if __name__ == '__main__':   # to sparate the codes
 
  while True:
      notification.notify(
        title='Yeah...Lets drink water !',
        message='Hydration fuels vitality.',
        app_icon='icon1.ico',
        timeout=5)   #Timefor stay
      time.sleep(10) #time for arrival


        
        
