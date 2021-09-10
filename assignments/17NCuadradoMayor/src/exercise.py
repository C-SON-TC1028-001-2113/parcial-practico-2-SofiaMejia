

def main():
    
    #escribe tu código abajo de esta línea
    numero = int(input("Escribe un numero : "))
    ans = 1

    while ans**2<=numero:
        ans += 1
    
    print(ans)

if __name__=='__main__':
    main()
