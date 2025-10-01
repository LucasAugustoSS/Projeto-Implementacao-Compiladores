from scanner import scanner

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def atual(self):
        return self.tokens[self.pos]

    def proximo(self):
        return self.tokens[self.pos+1]

    def consumir(self, token_type):
        if self.atual()[0] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Esperado {token_type}, encontrado {self.atual()[1]}")

    def parse(self):
        self.parse_programa()
        print("\nPrograma sem problemas de sintaxe.\n")

    def parse_programa(self):
        while self.atual()[0] != "EOF":
            if self.atual()[0] == "FUNCAO":
                self.parse_funcao()
            else:
                self.consumir("PRINCIPAL")
                self.consumir("LCHAVE")
                while self.atual()[0] != "RCHAVE":
                    self.parse_instrucao()
                self.consumir("RCHAVE")

    def parse_instrucao(self):
        if self.atual()[0] == "TIPO_VAR":
            self.parse_declaracao()
            self.consumir("PONTOVIRG")
        elif self.atual()[0] == "SE":
            self.parse_se()
        elif self.atual()[0] == "ENQUANTO":
            self.parse_enquanto()
        elif self.atual()[0] == "FACA":
            self.parse_faca_enquanto()
            self.consumir("PONTOVIRG")
        elif self.atual()[0] == "PARA":
            self.parse_para()
        elif self.atual()[0] == "FUNCAO":
            self.parse_funcao()
        elif self.atual()[0] == "RETORNO":
            self.parse_retorno()
            self.consumir("PONTOVIRG")
        elif self.atual()[0] == "IDENT" and self.proximo()[0] == "LPAREN":
            self.parse_funcao_chamado()
            self.consumir("PONTOVIRG")
        else:
            self.parse_atribuicao()
            self.consumir("PONTOVIRG")

    def parse_declaracao(self):
        self.consumir("TIPO_VAR")
        self.consumir("IDENT")
        if self.atual()[0] == "ATRIB":
            self.consumir("ATRIB")
            self.parse_expressao()

    def parse_atribuicao(self):
        self.consumir("IDENT")
        self.consumir("ATRIB")
        self.parse_expressao()

    def parse_expressao(self):
        self.parse_termo()
        while self.atual()[0] in ("OPER_ARIT", "OPER_LOGI", "COMPAR"):
            self.consumir(self.atual()[0])
            self.parse_termo()

    def parse_termo(self):
        if self.atual()[0] == "OPER_LOGI" and self.atual()[1] == "!":
            self.consumir("OPER_LOGI")
            self.parse_termo()
        elif self.atual()[0] in ("IDENT", "NUMERO_INT", "NUMERO_REAL", "PALAVRA", "CARACTERE", "BOOLEANO"):
            if self.atual()[0] == "IDENT" and self.proximo()[0] == "LPAREN":
                self.parse_funcao_chamado()
            else:
                self.consumir(self.atual()[0])
        elif self.atual()[0] == "LPAREN":
            self.consumir("LPAREN")
            self.parse_expressao()
            self.consumir("RPAREN")
        else:
            raise SyntaxError(f"Valor inesperado: {self.atual()[1]}")

    def parse_parametros(self):
        self.consumir("TIPO_VAR")
        self.consumir("IDENT")

        while self.atual()[0] == "VIRGULA":
            self.consumir("VIRGULA")
            self.consumir("TIPO_VAR")
            self.consumir("IDENT")

    def parse_argumentos(self):
        self.parse_expressao()

        while self.atual()[0] == "VIRGULA":
            self.consumir("VIRGULA")
            self.parse_expressao()

    def parse_se(self):
        self.consumir("SE")
        self.consumir("LPAREN")
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

    def parse_enquanto(self):
        self.consumir("ENQUANTO")
        self.consumir("LPAREN")
        self.parse_expressao()
        self.consumir("RPAREN")
        self.consumir("LCHAVE")
        while self.atual()[0] != "RCHAVE":
            self.parse_instrucao()
        self.consumir("RCHAVE")

    def parse_faca_enquanto(self):
        self.consumir("FACA")
        self.consumir("LCHAVE")
        while self.atual()[0] != "RCHAVE":
            self.parse_instrucao()
        self.consumir("RCHAVE")
        self.consumir("ENQUANTO")
        self.consumir("LPAREN")
        self.parse_expressao()
        self.consumir("RPAREN")

    def parse_para(self):
        self.consumir("PARA")
        self.consumir("LPAREN")
        if self.atual()[0] == "TIPO_VAR":
            self.parse_declaracao()
        else:
            self.parse_atribuicao()
        self.consumir("PONTOVIRG")
        self.parse_expressao()
        self.consumir("PONTOVIRG")
        self.parse_atribuicao()
        self.consumir("RPAREN")
        self.consumir("LCHAVE")
        while self.atual()[0] != "RCHAVE":
            self.parse_instrucao()
        self.consumir("RCHAVE")

    def parse_funcao(self):
        self.consumir("FUNCAO")
        self.consumir("TIPO_VAR")
        self.consumir("IDENT")
        self.consumir("LPAREN")
        if self.atual()[0] != "RPAREN":
            self.parse_parametros()
        self.consumir("RPAREN")
        self.consumir("LCHAVE")
        while self.atual()[0] != "RCHAVE":
            self.parse_instrucao()
        self.consumir("RCHAVE")

    def parse_funcao_chamado(self):
        self.consumir("IDENT")
        self.consumir("LPAREN")
        if self.atual()[0] != "RPAREN":
            self.parse_argumentos()
        self.consumir("RPAREN")

    def parse_retorno(self):
        self.consumir("RETORNO")
        if self.atual()[0] != "PONTOVIRG":
            self.parse_expressao()

def analisar(codigo):
    tokens = scanner(codigo)
    parser = Parser(tokens)
    parser.parse()