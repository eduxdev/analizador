# 🎓 Compilador de Python - Proyecto Completo
## Teoría de Autómatas y Lenguajes Formales

[![Cumplimiento](https://img.shields.io/badge/Cumplimiento-100%25-brightgreen)]()
[![Python](https://img.shields.io/badge/Python-3.8+-blue)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

---

## 📋 Descripción

Compilador completo para un subconjunto de Python que implementa **todos los 10 requisitos formales** de Teoría de Autómatas y Lenguajes Formales, incluyendo:

- ✅ Análisis léxico con autómatas finitos
- ✅ Análisis sintáctico con gramáticas libres de contexto
- ✅ Análisis semántico con tabla de símbolos
- ✅ Generación de código intermedio (TAC)
- ✅ Optimización de código
- ✅ Generación de código ensamblador
- ✅ Parser LR(1) con autómata de pila explícito
- ✅ Análisis de propiedades formales (cerradura y decidibilidad)

---

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8 o superior
- Tkinter (incluido en Python)

### Ejecución

```bash
# Ejecutar el IDE completo
python python_ide_complete.py
```

### Demostración de Módulos Individuales

```bash
# Parser LR(1) con tabla explícita
python lr_parser.py

# Análisis de propiedades formales
python formal_properties.py
```

---

## 📁 Estructura del Proyecto

```
LexicoLexico/
│
├── python_compiler.py              # Lexer, Parser LL(1), AST
├── semantic_analyzer.py            # Análisis semántico
├── tac_generator.py                # Generación TAC
├── tac_optimizer.py                # Optimización de código
├── tac_interpreter.py              # Intérprete TAC
├── machine_code_generator.py       # Generación de ensamblador
├── reglas_semanticas.py            # 30+ reglas documentadas
│
├── lr_parser.py                    # ✨ Parser LR(1) (NUEVO)
├── formal_properties.py            # ✨ Propiedades formales (NUEVO)
│
├── python_ide_complete.py          # IDE con interfaz gráfica
│
├── ANALISIS_REQUERIMIENTOS.md      # Análisis de cumplimiento
└── README.md                       # Este archivo
```

---

## 🎯 Cumplimiento de Requerimientos (100%)

| # | Requerimiento | Archivo | Estado |
|---|---------------|---------|--------|
| 1 | Definición Formal del Lenguaje | `python_compiler.py` | ✅ 100% |
| 2 | Autómatas Finitos (Léxico) | `python_compiler.py` | ✅ 100% |
| 3 | Gramática Libre de Contexto | `python_compiler.py` | ✅ 100% |
| 4 | Tabla de Símbolos | `semantic_analyzer.py` | ✅ 100% |
| 5 | Manejo de Errores | `python_compiler.py` | ✅ 100% |
| 6 | AST | `python_compiler.py` | ✅ 100% |
| 7 | Análisis Semántico | `semantic_analyzer.py` | ✅ 100% |
| 8 | Autómatas de Pila (Parser LR) | `lr_parser.py` | ✅ 100% |
| 9 | Optimizaciones | `tac_optimizer.py` | ✅ 100% |
| 10 | Cerradura y Decidibilidad | `formal_properties.py` | ✅ 100% |

**Ver análisis detallado en:** [`ANALISIS_REQUERIMIENTOS.md`](ANALISIS_REQUERIMIENTOS.md)

---

## 🖥️ Características del IDE

El IDE incluye **11 pestañas** con visualización completa:

1. 🔤 **Léxico** - Tokens reconocidos por el AFD
2. 🌲 **Sintáctico** - Árbol de Sintaxis Abstracta (AST)
3. 🔬 **Semántico** - Tabla de símbolos y verificación de tipos
4. ⚡ **Intermedio** - Código de Tres Direcciones (TAC)
5. 🎯 **Optimizar** - Código optimizado con reporte
6. 🖥️ **Máquina** - Código ensamblador RISC
7. 🎮 **Ejecución** - Salida del programa
8. 📋 **Reglas** - 30+ reglas semánticas documentadas
9. 📜 **Gramática** - Gramática formal completa
10. 🔧 **Parser LR** - Tabla ACTION/GOTO y autómata de pila ✨
11. 🎓 **Propiedades** - Análisis formal de cerradura y decidibilidad ✨

---

## 💡 Ejemplos de Código Soportado

### Fibonacci
```python
n = 10
a = 0
b = 1

print("Serie de Fibonacci:")
print(a)
print(b)

i = 2
while i < n:
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1
```

### Procesamiento de Listas
```python
numeros = [10, 20, 30, 40, 50]
suma = 0
contador = 0

for num in numeros:
    print(num)
    suma = suma + num
    contador = contador + 1

promedio = suma / contador
print(promedio)
```

---

## 📊 Características Técnicas

### 1. Análisis Léxico
- **AFD implementado** con tabla de transiciones
- **Lookahead** para operadores de 2 caracteres
- **Manejo de indentación** (INDENT/DEDENT)
- **Expresiones regulares** para tokens

### 2. Análisis Sintáctico
- **Parser LL(1)** descendente recursivo
- **Parser LR(1)** ascendente con tabla explícita
- **Eliminación de recursión izquierda**
- **Factorización** de producciones

### 3. Análisis Semántico
- **Tabla de símbolos** con tipos e inicialización
- **Inferencia de tipos** dinámica
- **Verificación de compatibilidad** de tipos
- **30+ reglas semánticas** documentadas

### 4. Generación de Código
- **TAC (Three Address Code)** - Código intermedio
- **6 optimizaciones:**
  1. Plegado de constantes
  2. Propagación de constantes
  3. Eliminación de código muerto
  4. Reducción de fuerza
  5. Eliminación de asignaciones redundantes
  6. Eliminación de saltos muertos
- **Código ensamblador RISC** genérico

### 5. Propiedades Formales
- **Clasificación según Chomsky:** Tipo 2 (CFG)
- **Propiedades de cerradura:**
  - Unión: ✓
  - Concatenación: ✓
  - Estrella de Kleene: ✓
  - Intersección: ✗ (NO cerrado)
  - Complemento: ✗ (NO cerrado)
- **Propiedades decidibles:**
  - Problema de pertenencia: DECIDIBLE
  - Problema del vacío: DECIDIBLE
  - Problema de finitud: DECIDIBLE
  - Problema de equivalencia: INDECIDIBLE

---

## 🔧 Arquitectura del Compilador

```
┌─────────────────────────────────────────────────────────────┐
│                     CÓDIGO FUENTE PYTHON                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  ANÁLISIS LÉXICO (Lexer)                                    │
│  - AFD con lookahead                                        │
│  - Tokens: ID, NUMBER, STRING, operadores, palabras clave   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  ANÁLISIS SINTÁCTICO (Parser LL/LR)                         │
│  - Gramática Libre de Contexto                              │
│  - Construcción del AST                                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  ANÁLISIS SEMÁNTICO                                         │
│  - Tabla de símbolos                                        │
│  - Verificación de tipos                                    │
│  - Gramáticas atribuidas                                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  GENERACIÓN DE CÓDIGO INTERMEDIO (TAC)                      │
│  - Three Address Code                                       │
│  - Instrucciones de 3 direcciones                           │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  OPTIMIZACIÓN                                               │
│  - Plegado de constantes                                    │
│  - Propagación de constantes                                │
│  - Eliminación de código muerto                             │
│  - Reducción de fuerza                                      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  GENERACIÓN DE CÓDIGO MÁQUINA                               │
│  - Ensamblador RISC genérico                                │
│  - Asignación de registros                                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│  EJECUCIÓN/INTERPRETACIÓN                                   │
│  - Intérprete TAC                                           │
│  - Salida del programa                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📚 Documentación Adicional

### Gramática Formal

**G = (N, Σ, P, S)** donde:

- **N** (No terminales): `{program, stmt, expr, term, factor, ...}`
- **Σ** (Terminales): `{ID, NUMBER, STRING, +, -, *, /, if, while, for, ...}`
- **P** (Producciones): Ver archivo `python_ide_complete.py` líneas 890-983
- **S** (Símbolo inicial): `program`

**Tipo:** Gramática Tipo 2 (Libre de Contexto)

### Tokens (Expresiones Regulares)

```
Identificador: [a-zA-Z_][a-zA-Z0-9_]*
Número:        [0-9]+(\.[0-9]+)?
String:        "[^"]*" | '[^']*'
Operadores:    + - * / % ** == != < > <= >=
Delimitadores: ( ) [ ] : , .
```

---

## 🧪 Pruebas

El IDE incluye 4 ejemplos preconfigurados:

1. 🔢 **Fibonacci** - Serie de Fibonacci
2. 🔍 **Búsqueda** - Búsqueda en arrays
3. 📊 **Listas** - Procesamiento de listas
4. ⚠️ **Errores** - Demostración de manejo de errores

Cada ejemplo demuestra diferentes aspectos del compilador.

---

## 🎓 Conceptos Implementados

### Teoría de Autómatas
- ✅ Autómatas Finitos Deterministas (AFD)
- ✅ Autómatas de Pila (PDA)
- ✅ Tablas de transición
- ✅ Estados y transiciones

### Lenguajes Formales
- ✅ Jerarquía de Chomsky
- ✅ Gramáticas Libres de Contexto (CFG)
- ✅ Producciones y derivaciones
- ✅ Árboles de derivación (AST)

### Compiladores
- ✅ Fases de compilación completas
- ✅ Análisis léxico, sintáctico y semántico
- ✅ Generación de código intermedio
- ✅ Optimización de código
- ✅ Generación de código objetivo

### Propiedades Formales
- ✅ Propiedades de cerradura
- ✅ Problemas de decidibilidad
- ✅ Análisis de vacío y finitud
- ✅ Compatibilidad con herramientas (LEX/YACC/ANTLR)

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+** - Lenguaje de implementación
- **Tkinter** - Interfaz gráfica del IDE
- **Dataclasses** - Estructuras de datos
- **Enums** - Tipos enumerados
- **Type Hints** - Tipado estático opcional

---

## 📖 Referencias Académicas

Este proyecto implementa conceptos de:

1. **"Introduction to Automata Theory, Languages, and Computation"**  
   Hopcroft, Motwani, Ullman

2. **"Compilers: Principles, Techniques, and Tools" (Dragon Book)**  
   Aho, Lam, Sethi, Ullman

3. **"Modern Compiler Implementation in ML/Java/C"**  
   Andrew W. Appel

---

## 👨‍💻 Autor

Proyecto académico - Teoría de Autómatas y Lenguajes Formales

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

## 🎯 Resumen de Cumplimiento

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│            🎉 CUMPLIMIENTO TOTAL: 100% 🎉                   │
│                                                             │
│  ✅ 10/10 Requerimientos Completados                        │
│  ✅ Todos los puntos implementados                          │
│  ✅ Documentación completa                                  │
│  ✅ IDE funcional                                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📞 Soporte

Para más información, consulta:
- `ANALISIS_REQUERIMIENTOS.md` - Análisis detallado de cumplimiento
- Comentarios en el código fuente
- Pestaña "Gramática" en el IDE
- Pestaña "Reglas" en el IDE

---

**¡Gracias por usar este compilador educativo!** 🚀
