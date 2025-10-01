import re

lexemas = [
    ("PRINCIPAL",   r'principal'),
    ("FUNCAO",      r'funcao'),
    ("TIPO_VAR",    r'int|real|cadeia|car|booleano|vazio'),
    ("SENAO",       r'senao'),
    ("SE",          r'se'),
    ("ENQUANTO",    r'enquanto'),
    ("FACA",        r'faca'),
    ("PARA",        r'para'),
    ("RETORNO",     r'retornar'),
    ("BOOLEANO",    r'verdadeiro|falso'),
    ("NUMERO_REAL", r'\d+\.\d+'),
    ("NUMERO_INT",  r'\d+'),
    ("CARACTERE",   r'\'.\''),
    ("PALAVRA",     r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\''),
    ("IDENT",       r'[a-zA-Z_]\w*'),
    ("COMPAR",      r'[<>]=?|==|!='),
    ("OPER_ARIT",   r'[+\-*/%]'),
    ("OPER_LOGI",   r'&&|\|\||!'),
    ("ATRIB",       r'='),
    ("LPAREN",      r'\('),
    ("RPAREN",      r'\)'),
    ("LCHAVE",      r'\{'),
    ("RCHAVE",      r'\}'),
    ("VIRGULA",     r','),
    ("PONTOVIRG",   r';'),
    ("IGNORAR",     r'[ \t\n]+'),
    ("INCOMPAT",    r'.'),
    ("EOF",         r'EOF'),
]

def scanner(codigo):
    tokens = []
    regex = "|".join(f"(?P<{nome}>{expr})" for nome, expr in lexemas)

    print("[", end="")
    for match in re.finditer(regex, codigo):
        tipo = match.lastgroup
        valor = match.group()
        if tipo == "IGNORAR":
            continue
        elif tipo == "INCOMPAT":
            print((tipo, valor), end="")
            print("]")
            raise RuntimeError(f"Caractere inesperado: {valor}")
        tokens.append((tipo, valor))
        print(tokens[-1], end=", ")
    tokens.append(("EOF", 'EOF'))
    print(tokens[-1], end="")
    print("]")

    return tokens