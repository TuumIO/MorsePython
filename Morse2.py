Dot = 1
Line = 3*Dot
Space = Dot
SpaceLetters = 3*Dot
SpaceWords = 5*Dot
MorseLetters = {"A":[Dot, Line],"B":[Line, Dot, Dot],"C":[Line, Dot, Line, Dot],"D":[Line, Dot, Dot],"E":[Dot],"F":[Dot, Dot, Line, Dot],"G":[Line, Line, Dot],"H":[Dot, Dot, Dot, Dot],"I":[Dot, Dot],"J":[Dot, Line, Line, Line],"K":[Line, Dot, Line],"L":[Dot, Line, Dot, Dot],"M":[Line, Line],"N":[Line, Dot],"O":[Line, Line, Line],"P":[Dot, Line, Line, Dot],"Q":[Line, Line, Dot, Line],"R":[Dot, Line, Dot],"S":[Dot, Dot, Dot],"T":[Line],"U":[Dot, Dot, Line],"J":[Dot, Dot, Dot, Line],"W":[Dot, Line, Line],"J":[Line, Dot, Dot, Line],"Y":[Line, Dot, Line, Line],"Z":[Line, Line, Dot, Dot]}
MorseNumbers = {"1":[Dot, Line, Line, Line, Line],"2":[Dot, Dot, Line, Line, Line],"3":[Dot, Dot, Dot, Line, Line],"4":[Dot, Dot, Dot, Dot, Line],"5":[Dot, Dot, Dot, Dot, Dot],"6":[Line, Dot, Dot, Dot, Dot],"7":[Line, Line, Dot, Dot, Dot],"8":[Line, Line, Line, Dot, Dot],"9":[Line, Line, Line, Line, Dot],"0":[Line, Line, Line, Line, Line]}
while 1==1:
  request = input("Palabra: ")
  try:
    var = float(request)
    print(MorseNumbers[request.upper()])
  except ValueError:
    i = 0
    palabra = []
    while i < len(request): 
      try:
        print(MorseLetters[request[i].upper()])
        palabra = palabra + MorseLetters[request[i].upper()]
        i = i + 1
      except KeyError:
        print("Caracter no identificado")
        i = i + 1
  print(palabra)
  print("Listo!")
