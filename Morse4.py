import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21

GPIO.setup(led, GPIO.OUT)

Dot = 0.5
Line = 3*Dot
Space = Dot
SpaceLetters = ["###"]
SpaceWords = ["#####"]
MorseLetters = {"A":[Dot, Line],"B":[Line, Dot, Dot],"C":[Line, Dot, Line, Dot],"D":[Line, Dot, Dot],"E":[Dot],"F":[Dot, Dot, Line, Dot],"G":[Line, Line, Dot],"H":[Dot, Dot, Dot, Dot],"I":[Dot, Dot],"J":[Dot, Line, Line, Line],"K":[Line, Dot, Line],"L":[Dot, Line, Dot, Dot],"M":[Line, Line],"N":[Line, Dot],"O":[Line, Line, Line],"P":[Dot, Line, Line, Dot],"Q":[Line, Line, Dot, Line],"R":[Dot, Line, Dot],"S":[Dot, Dot, Dot],"T":[Line],"U":[Dot, Dot, Line],"V":[Dot, Dot, Dot, Line],"W":[Dot, Line, Line],"X":[Line, Dot, Dot, Line],"Y":[Line, Dot, Line, Line],"Z":[Line, Line, Dot, Dot]}
MorseNumbers = {"1":[Dot, Line, Line, Line, Line],"2":[Dot, Dot, Line, Line, Line],"3":[Dot, Dot, Dot, Line, Line],"4":[Dot, Dot, Dot, Dot, Line],"5":[Dot, Dot, Dot, Dot, Dot],"6":[Line, Dot, Dot, Dot, Dot],"7":[Line, Line, Dot, Dot, Dot],"8":[Line, Line, Line, Dot, Dot],"9":[Line, Line, Line, Line, Dot],"0":[Line, Line, Line, Line, Line]}

def LedOn(val):
    GPIO.output(led,1)
    time.sleep(val)
    GPIO.output(led,0)

def letra(letr):
  result = []
  try:
    var = float(request)
    frase.append(MorseNumbers[letr.upper()])
    frase.append(SpaceLetters)
  except ValueError:
    try:
       frase.append(MorseLetters[letr.upper()])
       frase.append(SpaceLetters)
    except KeyError:
       print("Intente nuevamente, caracter no identificado")
  
while True:
  frase = []
  request = input("Frase: ")
  j = 0
  while j < len(request): 
    if request[j] != " ": 
      letra(request[j])
      j += 1
    else:
      frase.append(SpaceWords)
      j += 1 
  print(frase)

  for palabr in frase:
    for letr in palabr:
      try:
        temp = int(letr)
        LedOn(temp)
        time.sleep(Dot)
      except ValueError:
        if letr == "###":
          time.sleep(3*Dot)
        elif letr == "#####":
          time.sleep(5*Dot)
    
  print("Listo!")
