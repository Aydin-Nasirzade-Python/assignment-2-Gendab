#import libraries here

def main():
  il=int(input("Enter the year [ex. 2021]: "))
  if il<0: print("Invalid year!")
  elif il==2000 or (il-2000)%12==0:
      print(f"{il} is the year of the Dragon")
  elif il==2001 or (il-2001)%12==0:
      print(f"{il} is the year of the Snake")
  elif il==2002 or (il-2002)%12==0:
      print(f"{il} is the year of the Horse")
  elif il==2003 or (il-2003)%12==0:
      print(f"{il} is the year of the Sheep")
  elif il==2004 or (il-2004)%12==0:
      print(f"{il} is the year of the Monkey")
  elif il==2005 or (il-2005)%12==0:
      print(f"{il} is the year of the Rooster")
  elif il==2006 or (il-2006)%12==0:
      print(f"{il} is the year of the Dog")
  elif il==2007 or (il-2007)%12==0:
      print(f"{il} is the year of the Pig")
  elif il==2008 or (il-2008)%12==0:
      print(f"{il} is the year of the Rat")
  elif il==2009 or (il-2002)%12==0:
      print(f"{il} is the year of the Ox")
  elif il==2010 or (il-2010)%12==0:
      print(f"{il} is the year of the Tiger")   
  else:
      print(f"{il} is the year of the Hare")
  pass

if __name__ == "__main__":
  main()
