#import libraries here

def main():
  ay=input("Enter name of the month [ex. June]: ")
  gun=input("Enter the day [ex. 5]: ")
  if ay=="march" and gun=="20":
      print("March 20 is in Spring")
  elif ay=="June" and gun=="21":
      print("June 21 is in Summer")
  elif ay=="September" and gun=="22":
      print("September 22 is in Fall")
  elif ay=="December" and gun=="21":
      print("December 21 is in Winter")
  pass

if __name__ == "__main__":
  main()
