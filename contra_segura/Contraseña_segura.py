password = input("Dame una contraseña (debe tener al menos 5 caracteres, una mayúscula, una minúscula, un número y un carácter especial): ").strip()

def requisitosFaltantes(password):
    faltantes = []
    hayLetraMayuscula = False
    hayLetraMinuscula = False
    hayNumero = False
    hayCaracterEspecial = False

    if len(password) < 5:
        faltantes.append("al menos 5 caracteres")

    for i in password:
        if i.isalpha():
            if i.isupper():
                hayLetraMayuscula = True
            else:
                hayLetraMinuscula = True
        else:
            if i.isdigit():
                hayNumero = True
            else:
                hayCaracterEspecial = True

    if not hayLetraMayuscula:
        faltantes.append("una letra mayúscula")
    if not hayLetraMinuscula:
        faltantes.append("una letra minúscula")
    if not hayNumero:
        faltantes.append("un número")
    if not hayCaracterEspecial:
        faltantes.append("un carácter especial")

    return faltantes
            
faltantes = requisitosFaltantes(password)

if not faltantes:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")
    print("Le falta: " + ", ".join(faltantes) + ".")

#Este programa ayuda a los usuarios a crear contraseñas seguras al verificar si cumplen con ciertos requisitos de seguridad. Si la contraseña no cumple con alguno de los requisitos, el programa informa al usuario qué elementos faltan para que la contraseña sea considerada segura.