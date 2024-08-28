def main():
    a, b, c = get_coeficients()
    # Delta
    delta = b**2 - 4*a*c
    # Delta = 0
    if delta == 0:
        x = -b/(2*a)
        print("x = ", round(x, 4))
        print("uma raiz real")
    else:
        # Delta > 0
        if delta > 0:
            x1 = (-b + delta**(1/2))/(2*a)
            x2 = (-b - delta**(1/2))/(2*a)
            print("x1 = ", round(x1, 4))
            print("x2 = ", round(x2, 4))
            print("duas raizes reais")
        # Delta < 0
        else:
            xr = -b/(2*a)
            xim = (-delta)**(1/2)/(2*a)
            print("x1 = ", round(xr, 4), " + ",round(xim, 4), "i")
            print("x2 = ", round(xr, 4), " - ",round(xim, 4), "i")
            print("duas raizes complexas")

# Prompt for coeficients of quadratic function
def get_coeficients():
  while True:
    try:
        a = float(input("coeficiente a: "))
        b = float(input("coeficiente b: "))
        c = float(input("coeficiente c: "))
        return a, b, c
    except ValueError:
        print("Not a float")

main()
