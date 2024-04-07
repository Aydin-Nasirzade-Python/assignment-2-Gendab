#import libraries here

def main():
  a="AprilMay"
  b="JulyAugust"
  c="OctoberNovember"
  ay=input("Enter name of the month [ex. June]: ")
  gun=int(input("Enter the day [ex. 5]: "))
  if ay=="march" and gun>=20 or ay=="June" and gun<21 or ay in a:
      print(f"{ay} {gun} is in Spring")
  elif ay=="June" and gun>=21 or ay=="September" and gun<22 or ay in b:
      print(f"{ay} {gun} is in Summer")
  elif ay=="September" and gun>=22 or ay=="December" and gun<21 or ay in c:
      print(f"{ay} {gun} is in Fall")
  else:
      print(f"{ay} {gun} is in Winter")
  pass

if __name__ == "__main__":
  main()
