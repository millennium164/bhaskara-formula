def main():
    a, b, c = get_coeficients()
    # Delta
    delta = b**2 - 4*a*c
    # Delta = 0
    if delta == 0:
        x = -b/(2*a)
        print("x = ", round(x, 4))
        print("one real solution")
    else:
        # Delta > 0
        if delta > 0:
            x1 = (-b + delta**(1/2))/(2*a)
            x2 = (-b - delta**(1/2))/(2*a)
            print("x1 = ", round(x1, 4))
            print("x2 = ", round(x2, 4))
            print("two real solutions")
        # Delta < 0
        else:
            xr = -b/(2*a)
            xim = (-delta)**(1/2)/(2*a)
            print("x1 = ", round(xr, 4), " + ",round(xim, 4), "i")
            print("x2 = ", round(xr, 4), " - ",round(xim, 4), "i")
            print("two complex solutions")

# Prompt for coeficients of quadratic function
def get_coeficients():
  while True:
    try:
        a = float(input("coeficient a: "))
        b = float(input("coeficient b: "))
        c = float(input("coeficient c: "))
        return a, b, c
    except ValueError:
        print("Not a float")

main()
