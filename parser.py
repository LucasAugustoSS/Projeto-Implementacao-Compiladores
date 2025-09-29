from scanner import scanner

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def atual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ("EOF", None)

    def proximo(self):
        return self.tokens[self.pos+1] if self.pos+1 < len(self.tokens) else ("EOF", None)

    def consumir(self, token_type):
        if self.atual()[0] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Esperado {token_type}, encontrado {self.atual()}")

    def parse(self):
        self.parse_programa()
        print("Programa executado sem problemas de sintaxe.")

    def parse_programa(self):
        while self.atual()[0] != "EOF":
            self.parse_instrucao()

    def parse_instrucao(self):
        if self.atual()[0] == "TIPO_VAR":
            self.parse_declaracao()
        elif self.atual()[0] == "SE":
            self.parse_se()
        elif self.atual()[0] == "IDENT" and self.proximo()[0] == "LPAREN":
            self.parse_funcao()
        else:
            self.parse_atribuicao()

    def parse_declaracao(self):
        self.consumir("TIPO_VAR")
        self.consumir("IDENT")
        self.consumir("ATRIB")
        self.parse_expressao()
        self.consumir("PONTOVIRG")

    def parse_atribuicao(self):
        self.consumir("IDENT")
        self.consumir("ATRIB")
        self.parse_expressao()
        self.consumir("PONTOVIRG")

    def parse_expressao(self):
        if self.atual()[0] in ("IDENT", "NUMERO_INT", "NUMERO_REAL", "PALAVRA", "CARACTERE", "BOOLEANO"):
            self.consumir(self.atual()[0])
            if self.atual()[0] == "OPER":
                self.consumir("OPER")
                self.parse_expressao()
        else:
            raise SyntaxError(f"Valor inválido na expressão: {self.atual()}")

    def parse_funcao(self):
        self.consumir("IDENT")
        self.consumir("LPAREN")
        if self.atual()[0] in ("PALAVRA", "CARACTERE", "NUMERO_INT", "NUMERO_REAL", "BOOLEANO", "IDENT"):
            self.consumir(self.atual()[0])
            while self.atual()[0] == "VIRGULA":
                self.consumir("VIRGULA")
                if self.atual()[0] in ("PALAVRA", "CARACTERE", "NUMERO_INT", "NUMERO_REAL", "BOOLEANO", "IDENT"):
                    self.consumir(self.atual()[0])
                else:
                    raise SyntaxError(f"Esperado argumento dentro de chamada de função, encontrado {self.atual()}")
        elif self.atual()[0] != "RPAREN":
            raise SyntaxError(f"Argumento inválido em chamada de função: {self.atual()}")
        self.consumir("RPAREN")
        self.consumir("PONTOVIRG")

    def parse_se(self):
        self.consumir("SE")
        self.consumir("LPAREN")
        self.parse_expressao()
        self.consumir("COMPAR")
        self.parse_expressao()
        self.consumir("RPAREN")
        self.consumir("LCHAVE")
        while self.atual()[0] != "RCHAVE":
            self.parse_instrucao()
        self.consumir("RCHAVE")
        if self.atual()[0] == "SENAO":
            self.consumir("SENAO")
            if self.atual()[0] == "SE":
                self.parse_se()
            else:
                self.consumir("LCHAVE")
                while self.atual()[0] != "RCHAVE":
                    self.parse_instrucao()
                self.consumir("RCHAVE")

def analisar(codigo):
    tokens = scanner(codigo)
    parser = Parser(tokens)
    parser.parse()
    