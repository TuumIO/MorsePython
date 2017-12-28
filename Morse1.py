Dot = 1
Line = 3*Dot
Space = Dot
SpaceLetters = 3*Dot
SpaceWords = 5*Dot
morse = {"A":[Dot, Line],"B":[Line, Dot, Dot],"C":[Line, Dot, Line, Dot],"D":[Line, Dot, Dot],"E":[Dot],"F":[Dot, Dot, Line, Dot],"G":[Line, Line, Dot],"H":[Dot, Dot, Dot, Dot],"I":[Dot, Dot], "J":[Dot, Line, Line, Line]}
request = input("letra:")
print(morse[request])
