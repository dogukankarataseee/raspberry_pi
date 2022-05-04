import RPi.GPIO as GPIO # raspberry pi kütüphanesini import ediyoruz.
from time import sleep  # bekleme fonksiyonunu time kütüphanesinden import ediyoruz.

GPIO.setwarnings(False) # herhangi bir uyarı vermemesi için false yapıyoruz.
GPIO.setmode(GPIO.BCM)  # cipsete gore özgü olan pin dizilimini kullanmış oluruz.

GPIO.setup(27,GPIO.OUT)  # çıkış olarak alacağımız pini belirliyoruz.

for i in range(10):
    GPIO.output(27,GPIO.HIGH) # pine güç veriyoruz

    sleep(3) # bekletiyoruz

    GPIO.output(27,GPIO.LOW) # pinin gücünü kapatıyoruz
    
    sleep(3) # bekletiyoruz

GPIO.cleanup() # pinleri eski haline getiriyoruz.