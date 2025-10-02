# Interpretador Brick (Mini Linguagem)

Este projeto implementa um **analisador léxico e sintático** para uma linguagem fictícia chamada **Brick**.

## 📂 Estrutura do Projeto

```
.
├── main.py       # Arquivo principal para rodar o analisador
├── parser.py     # Parser (analisador sintático)
├── scanner.py    # Scanner (analisador léxico)
└── codigo/
    └── app.br    # Código-fonte exemplo escrito em Brick
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
- Ler o código-fonte em `codigo/app.br`.
- Gerar os tokens correspondentes.
- Verificar a sintaxe do programa.  
- Exibir se o programa está **correto** ou apontar **erros léxicos e sintáticos**.

---

## 🧩 Funcionamento

### 🔹 Scanner (scanner.py)
- Usa expressões regulares para **tokenizar** o código.  
- Reconhece:
  - **Tipos de variáveis**: `int`, `real`, `cadeia`, `booleano`, `car`, `vazio`
  - **Palavras reservadas**: `principal`, `se`, `enquanto`, `funcao`, `verdadeiro`, `retornar`
  - **Literais**: inteiros, reais, cadeias, caracteres, booleanos
  - **Operadores**: aritméticos (`+ - * / %`), lógicos (`&& || !`) comparações (`== < > <= >=`)
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
  - **Laços de repetição**:  
    ```lin
    enquanto (x < 20) {
        x = x + 1;
    }
    
    faca {
        y = y - 1;
    } enquanto (y > 0);
    
    para (int z = 0; z < 5; z = z + 1) {
        escrever(z);
    }
    ```
  - **Criação de função**:  
    ```lin
    funcao real soma(real x, real y) {
        retornar x + y;
    }
    ```
  - **Chamadas de função**:  
    ```lin
    escrever(x, "texto", verdadeiro);
    ```

### 🔹 Main (main.py)
- Abre o arquivo `codigo/app.br`.
- Executa `scanner` e `parser`.
- Mostra mensagem de sucesso ou erro.

---

## 📖 Exemplo de Código (app.br)

```lin
principal {
    int x = 5;
    real y = 10.0;
    
    se (x < y) {
        x = x + 1;
    } senao {
        y = y - 1;
    }
    
    escrever(x, y);
}
```

---
## ✅ Saída Esperada

Se o código não tiver erros:
```
Programa sem problemas de sintaxe.
```

Se houver erro, será exibida uma mensagem como:
```
SyntaxError: Esperado PONTOVIRG, encontrado real
```

---

## 🔧 Próximos Passos
 
- Criar uma etapa de **análise semântica** (tipagem, variáveis não declaradas).  
- Adicionar um **interpretador** para executar os comandos.  
