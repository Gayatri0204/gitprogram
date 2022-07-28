choice=int(input("Enter The Chioce:"))
match choice:
    case 1:
      def circle(R):
        Pi=3.14
        print(f"Area of Circle {Pi*R*R}")
      if __name__ =="__main__":
        radius=float(input("Enter The Radius:"))
        circle(radius)
    case 2:
      def Square(s):
        print(f"Area of square {s*s}")
      if __name__ =="__main__":
        side=int(input("Enter the side :"))
        Square(side)
    case 3:
      def Rectangle(l,b):
        print(f"Area of rectangle {l*b}")
      if __name__ =="__main__":
        Length=int(input("Enter the length:"))
        Breadth=int(input("Enter the breadth:"))
        Rectangle(Length,Breadth)
    case _:
      print("Please Correct no")