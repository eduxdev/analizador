# 🚀 INSTRUCCIONES DE EJECUCIÓN
## Compilador de Python - Guía Completa

---

## ✅ Pre-requisitos

### Software Necesario
- **Python 3.8 o superior** (Verificar con `python --version`)
- **Tkinter** (Incluido en la instalación estándar de Python)

### Verificar Instalación
```bash
# En Windows (PowerShell o CMD)
python --version

# En macOS/Linux
python3 --version
```

---

## 📦 Archivos del Proyecto

Asegúrate de tener todos estos archivos en la misma carpeta:

```
LexicoLexico/
├── python_compiler.py              ✅ Requerido
├── semantic_analyzer.py            ✅ Requerido
├── tac_generator.py                ✅ Requerido
├── tac_optimizer.py                ✅ Requerido
├── tac_interpreter.py              ✅ Requerido
├── machine_code_generator.py       ✅ Requerido
├── reglas_semanticas.py            ✅ Requerido
├── lr_parser.py                    ✅ Requerido (NUEVO)
├── formal_properties.py            ✅ Requerido (NUEVO)
├── python_ide_complete.py          ✅ Requerido (PRINCIPAL)
```

---

## 🎮 OPCIÓN 1: Ejecutar el IDE Completo (Recomendado)

### Paso 1: Abrir Terminal/CMD
```bash
# Navegar a la carpeta del proyecto
cd C:\Users\EDu\Documents\LexicoLexico
```

### Paso 2: Ejecutar el IDE
```bash
python python_ide_complete.py
```

### Paso 3: Usar el IDE
1. **El IDE se abrirá automáticamente**
2. **Verás 11 pestañas** en el panel derecho
3. **Código de ejemplo** ya está cargado (Fibonacci)
4. **Click en "🚀 COMPILAR"** para ejecutar

### Lo que verás:
```
┌──────────────────────────────────────────────────────────────┐
│  ⚡ Compilador Python Avanzado                               │
│  🔬 Análisis Completo: Léxico → ... → Propiedades           │
├──────────────────────────────────────────────────────────────┤
│  [🚀 COMPILAR] [🧹 Limpiar]  Ejemplos: [Fibonacci] ...      │
├──────────────────────────────────────────────────────────────┤
│ EDITOR │                    SALIDAS (11 pestañas)           │
│        │  1. 🔤 Léxico                                       │
│ Código │  2. 🌲 Sintáctico                                   │
│ fuente │  3. 🔬 Semántico                                    │
│        │  4. ⚡ Intermedio                                    │
│        │  5. 🎯 Optimizar                                    │
│        │  6. 🖥️ Máquina                                     │
│        │  7. 🎮 Ejecución                                    │
│        │  8. 📋 Reglas                                       │
│        │  9. 📜 Gramática                                    │
│        │ 10. 🔧 Parser LR    ← ✨ NUEVO                      │
│        │ 11. 🎓 Propiedades  ← ✨ NUEVO                      │
└──────────────────────────────────────────────────────────────┘
```

---

## 🧪 OPCIÓN 2: Ejecutar Módulos Individuales

### A. Parser LR(1) con Tabla Explícita
```bash
python lr_parser.py
```

**Salida esperada:**
```
===============================================================================
DEMOSTRACIÓN DEL PARSER LR(1) CON AUTÓMATA DE PILA
===============================================================================

TABLA DE ANÁLISIS LR(1)
================================================================================

PRODUCCIONES DE LA GRAMÁTICA:
--------------------------------------------------------------------------------
  0: S' → program
  1: program → stmt_list
  2: stmt_list → stmt stmt_list
  ...

TABLA ACTION (estado, terminal) → acción
--------------------------------------------------------------------------------
Estado 0:
  ID              → s5
  print           → s6
  if              → s7
  ...

TABLA GOTO (estado, no_terminal) → estado
--------------------------------------------------------------------------------
Estado 0:
  program         → 1
  stmt_list       → 2
  ...
```

### B. Análisis de Propiedades Formales
```bash
python formal_properties.py
```

**Salida esperada:**
```
===============================================================================
ANÁLISIS DE PROPIEDADES FORMALES DEL LENGUAJE
===============================================================================

1. GRAMÁTICA FORMAL
--------------------------------------------------------------------------------
Gramática G = (N, Σ, P, S)
N = {program, stmt_list, stmt, ...}
Σ = {ID, NUMBER, STRING, +, -, *, ...}
S = program
P = {
    program → stmt_list
    stmt_list → stmt stmt_list
    ...
}

2. JERARQUÍA DE CHOMSKY
--------------------------------------------------------------------------------
Tipo de lenguaje: Libre de Contexto
Clasificación: Gramática Tipo 2 (Libre de Contexto)

3. PROPIEDADES DE CERRADURA
--------------------------------------------------------------------------------
El lenguaje es CERRADO bajo:
  ✓ Union: SÍ
  ✓ Concatenation: SÍ
  ✓ Kleene Star: SÍ
  ✗ Intersection: NO
  ✗ Complement: NO

4. PROPIEDADES DE DECIDIBILIDAD
--------------------------------------------------------------------------------
✓ Membership:
    El problema de pertenencia es DECIDIBLE mediante el algoritmo CYK o parsing

✓ Emptiness:
    El problema del vacío es DECIDIBLE mediante análisis de alcanzabilidad
    
...
```

---

## 📝 OPCIÓN 3: Probar Ejemplos

### 1. Ejemplo Fibonacci (Pre-cargado)
Ya está en el editor. Solo haz click en **COMPILAR**.

### 2. Ejemplo Búsqueda
1. Click en radio button **🔍 Búsqueda**
2. Click en **🚀 COMPILAR**

### 3. Ejemplo Listas
1. Click en radio button **📊 Listas**
2. Click en **🚀 COMPILAR**

### 4. Ejemplo con Errores
1. Click en radio button **⚠️ Con Errores**
2. Click en **🚀 COMPILAR**
3. Observa cómo se reportan los errores semánticos

---

## 🔍 Explorar las Pestañas

### Pestañas Principales (1-7):
1. **🔤 Léxico** - Ver todos los tokens reconocidos
2. **🌲 Sintáctico** - Árbol de sintaxis abstracta (AST)
3. **🔬 Semántico** - Tabla de símbolos y errores
4. **⚡ Intermedio** - Código TAC generado
5. **🎯 Optimizar** - Código optimizado + reporte
6. **🖥️ Máquina** - Código ensamblador RISC
7. **🎮 Ejecución** - Salida del programa

### Pestañas Documentación (8-9):
8. **📋 Reglas** - 30+ reglas semánticas por fase
9. **📜 Gramática** - Gramática formal completa

### Pestañas Nuevas (10-11): ✨
10. **🔧 Parser LR** - Tabla ACTION/GOTO explícita
11. **🎓 Propiedades** - Análisis de cerradura y decidibilidad

---

## 🎯 Verificar Cumplimiento de Requerimientos

### En el IDE:

1. **Punto 1-7:** Visibles en pestañas principales
2. **Punto 8:** Pestaña **🔧 Parser LR**
   - Ver tabla ACTION/GOTO
   - Ver producciones de la gramática
3. **Punto 10:** Pestaña **🎓 Propiedades**
   - Clasificación según Chomsky
   - Propiedades de cerradura
   - Propiedades de decidibilidad

### En el Documento:

```bash
# Ver análisis completo de cumplimiento
notepad ANALISIS_REQUERIMIENTOS.md

# O en cualquier editor de texto
```

---

## ⚙️ Troubleshooting

### Problema: "ModuleNotFoundError"
**Solución:** Asegúrate de estar en la carpeta correcta
```bash
cd C:\Users\EDu\Documents\LexicoLexico
python python_ide_complete.py
```

### Problema: "tkinter not found"
**Solución (Windows):** Reinstala Python con Tkinter
- Descargar desde python.org
- Durante instalación, marcar "tcl/tk and IDLE"

**Solución (Linux):**
```bash
sudo apt-get install python3-tk
```

**Solución (macOS):**
```bash
brew install python-tk
```

### Problema: Ventana no se abre
**Solución:** Verificar que Python tiene permisos de GUI
```bash
# Probar Tkinter
python -m tkinter
# Debe abrir una ventana de prueba
```

### Problema: Error de importación
**Solución:** Verificar que todos los archivos están presentes
```bash
dir  # En Windows
ls   # En macOS/Linux
```

Debes ver todos los archivos `.py` listados arriba.

---

## 📊 Casos de Prueba Sugeridos

### Caso 1: Código Correcto
```python
x = 5
y = 10
suma = x + y
print(suma)
```
**Resultado esperado:** ✅ Sin errores, salida: `15`

### Caso 2: Variable No Declarada
```python
print(variable_no_existe)
```
**Resultado esperado:** ❌ Error semántico reportado

### Caso 3: Tipos Incompatibles
```python
x = 5
y = "texto"
z = x + y
```
**Resultado esperado:** ❌ Error de tipo reportado

### Caso 4: Optimización
```python
x = 2 + 3  # Debe optimizarse a x = 5
print(x)
```
**Resultado esperado:** ✅ Ver optimización en pestaña "Optimizar"

---

## 📈 Niveles de Uso

### Nivel 1: Usuario Básico
- Ejecutar el IDE
- Probar ejemplos pre-cargados
- Ver salida en pestaña "Ejecución"

### Nivel 2: Usuario Intermedio
- Escribir código propio
- Explorar todas las pestañas
- Entender el proceso de compilación

### Nivel 3: Usuario Avanzado
- Revisar tabla de parsing LR
- Analizar propiedades formales
- Estudiar optimizaciones aplicadas
- Modificar ejemplos y ver resultados

### Nivel 4: Desarrollador
- Ejecutar módulos individuales
- Estudiar el código fuente
- Extender funcionalidad
- Agregar nuevas características

---

## 🎓 Uso Académico

### Para Presentaciones
1. Ejecutar `python python_ide_complete.py`
2. Seleccionar ejemplo Fibonacci
3. Click en COMPILAR
4. Mostrar cada pestaña explicando la fase

### Para Demostraciones
1. Mostrar IDE funcionando
2. Ejecutar `python lr_parser.py` en terminal
3. Ejecutar `python formal_properties.py` en terminal
4. Mostrar `ANALISIS_REQUERIMIENTOS.md`

### Para Evaluación
- Documento: `ANALISIS_REQUERIMIENTOS.md` (100% cumplimiento)
- Código fuente: Todos los archivos `.py`
- Demostración: IDE en ejecución

---

## 📞 Resumen Rápido

```bash
# EJECUTAR TODO
cd C:\Users\EDu\Documents\LexicoLexico
python python_ide_complete.py

# PROBAR PARSER LR
python lr_parser.py

# PROBAR PROPIEDADES FORMALES
python formal_properties.py

# VER ANÁLISIS DE CUMPLIMIENTO
notepad ANALISIS_REQUERIMIENTOS.md
```

---

## ✨ Características Destacadas

- ✅ **100% de cumplimiento** de requisitos
- ✅ **11 pestañas** de visualización
- ✅ **4 ejemplos** pre-configurados
- ✅ **Parser LR(1)** con tabla explícita
- ✅ **Análisis formal** de propiedades
- ✅ **30+ reglas** semánticas documentadas
- ✅ **6 optimizaciones** de código
- ✅ **Interfaz gráfica** profesional

---

**¡Listo para usar!** 🚀

Si tienes alguna duda, consulta:
- `README.md` - Documentación general
- `ANALISIS_REQUERIMIENTOS.md` - Análisis detallado
- Comentarios en el código fuente
