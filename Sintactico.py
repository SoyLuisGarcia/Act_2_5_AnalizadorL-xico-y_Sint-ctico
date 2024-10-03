import ply.yacc as yacc
from analizador_lexico import tokens

# resultado del analisis
resultado_gramatica = []


def p_expresion(p):
    '''
    expresion : RESERVADA PARIZQ RESERVADA IDENTIFICADOR ASIGNAR ENTERO PUNTOCOMA IDENTIFICADOR MENORIGUAL ENTERO PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER LLAIZQ SYSTEM PUNTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ COMDOB IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER
              | SYSTEM PUNTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ COMDOB IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR  DOSPUNTO COMDOB SUMA IDENTIFICADOR PARDER PUNTOCOMA LLADER
              | LLADER LLADER
    '''
    if len(p) == 32:  # Regla para la primera expresión
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18], p[19], p[20], p[21], p[22], p[23], p[24], p[25], p[26], p[27], p[28], p[29], p[30])
        print("El for-LOOP es correcto")
    elif len(p) == 15:  # Regla para la segunda expresión
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14],)
    else:  # Regla para la tercera expresión
        p[0] = (p[1],"loop")



def p_error(p):
    global resultado_gramatica
    if p:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(p.type), str(p.value))
        print(resultado)
    else:
        resultado = "Error sintactico: {}, EL CODIGO ES CORRECTO".format(p)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sintáctico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    if data.strip():
                gram = parser.parse(data)
                if gram:
                    resultado_gramatica.append(str(gram))
    else:
                print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica


if __name__ == '__main__':
    while True:
        try:
            s = input(''' for(int i = 1; i <= 10; i++){
  System.out.println("Número:" + i);
} ''')
        except EOFError:
            continue
        if not s:
            continue

        prueba_sintactica(s)


     