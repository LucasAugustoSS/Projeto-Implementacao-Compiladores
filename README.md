# Interpretador LIN (Mini Linguagem)

Este projeto implementa um **analisador léxico e sintático** para uma linguagem fictícia chamada **LIN**, composta por variáveis, atribuições, expressões aritméticas, condicionais e chamadas de funções.  

## 📂 Estrutura do Projeto

```
.
├── main.py       # Arquivo principal para rodar o analisador
├── parser.py     # Parser (analisador sintático)
├── scanner.py    # Scanner (analisador léxico)
└── codigo/
    └── app.lin   # Código-fonte exemplo escrito em LIN
```

---

## 🚀 Como Executar

1. **Clone ou copie os arquivos do projeto.**  
2. Garanta que você tenha **Python 3.8+** instalado.  
3. Execute no terminal:

```bash
python main.py
```

O programa irá:
- Ler o código-fonte em `codigo/app.lin`.
- Gerar os tokens correspondentes.
- Verificar a sintaxe do programa.  
- Exibir se o programa está **correto** ou **apontar erros de sintaxe**.

---

## 🧩 Funcionamento

### 🔹 Scanner (scanner.py)
- Usa expressões regulares para **tokenizar** o código.  
- Reconhece:
  - **Tipos de variáveis**: `int`, `real`, `cadeia`, `booleano`, `car`
  - **Palavras reservadas**: `se`, `senao`, `verdadeiro`, `falso`
  - **Literais**: inteiros, reais, cadeias, caracteres, booleanos
  - **Operadores**: `+ - * / %`, comparações (`==`, `<`, `>`, `<=`, `>=`)
  - **Delimitadores**: `() { } , ;`
- Ignora espaços, tabulações e quebras de linha.

### 🔹 Parser (parser.py)
- Implementa a **análise sintática descendente**.  
- Estruturas reconhecidas:
  - **Declarações de variáveis**:  
    ```lin
    int x = 10;
    ```
  - **Atribuições**:  
    ```lin
    x = x + 5;
    ```
  - **Condições if/else**:  
    ```lin
    se (x > 10) {
        y = 20;
    } senao {
        y = 5;
    }
    ```
  - **Chamadas de função**:  
    ```lin
    print(x, "texto", verdadeiro);
    ```

### 🔹 Main (main.py)
- Abre o arquivo `codigo/app.lin`.
- Executa `scanner` e `parser`.
- Mostra mensagem de sucesso ou erro.

---

## 📖 Exemplo de Código (app.lin)

```lin
int x = 5;
int y = 10;

se (x < y) {
    x = x + 1;
} senao {
    y = y - 1;
}

print(x, y);
```

---
## ✅ Saída Esperada

Se o código não tiver erros:
```
Programa executado sem problemas de sintaxe.
```

Se houver erro, será exibida uma mensagem como:
```
SyntaxError: Esperado ;, encontrado ('IDENT', 'y')
```

---

## 🔧 Próximos Passos

- Implementar **laços de repetição** (`enquanto`, `para`).  
- Criar uma etapa de **análise semântica** (tipagem, variáveis não declaradas).  
- Adicionar um **interpretador** para executar os comandos.  
