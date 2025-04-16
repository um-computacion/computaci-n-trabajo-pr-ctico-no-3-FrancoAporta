from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    try:
        numero = float(input("Ingrese un número: "))
        
        # Si el número es negativo, tira la excepción con el mensaje predeterminado
        if numero < 0:
            raise NumeroDebeSerPositivo()
        return numero

    except ValueError:
        print("Error: La entrada debe ser un número válido")
    except NumeroDebeSerPositivo as e:
        print(f"Error: {e}")
