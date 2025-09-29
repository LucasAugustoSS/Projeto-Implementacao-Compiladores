import re

lexemas = [
    ("TIPO_VAR",    r'int|real|cadeia|booleano|car'),
    ("SENAO",       r'senao'),
    ("SE",          r'se'),
    ("NUMERO_REAL", r'\d+\.\d+'),
    ("NUMERO_INT",  r'\d+'),
    ("CARACTERE",   r'\'.\''),
    ("PALAVRA",     r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\''),
    ("BOOLEANO",    r'verdadeiro|falso'),
    ("IDENT",       r'[a-zA-Z_]\w*'),
    ("OPER",        r'[+\-*/%]'),
    ("COMPAR",      r'[<>]=?|=='),
    ("ATRIB",       r'='),
    ("LPAREN",      r'\('),
    ("RPAREN",      r'\)'),
    ("LCHAVE",      r'\{'),
    ("RCHAVE",      r'\}'),
    ("VIRGULA",     r','),
    ("PONTOVIRG",   r';'),
    ("IGNORAR",     r'[ \t\n]+'),
    ("MISMATCH",    r'.'),
]

def scanner(codigo):
    tokens = []
    regex = '|'.join(f'(?P<{nome}>{expr})' for nome, expr in lexemas)

    for match in re.finditer(regex, codigo):
        tipo = match.lastgroup
        valor = match.group()
        if tipo == 'IGNORAR':
            continue
        elif tipo == 'MISMATCH':
            raise RuntimeError(f"Caractere inesperado: {valor}")
        tokens.append((tipo, valor))

    return tokens