from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    try:
        numero = float(input("Ingrese un número: "))
        if numero < 0:
            raise NumeroDebeSerPositivo()  # Lanza la excepción si el número es negativo
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")  # Si no es un número válido
