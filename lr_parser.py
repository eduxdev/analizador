"""
Parser LR(1) con Tabla de Análisis Explícita
Implementa autómata de pila para análisis sintáctico ascendente
Completa el Punto 8: Autómatas de Pila para Análisis Sintáctico
"""

from python_compiler import *
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict, Set


class Action(Enum):
    """Tipos de acciones en la tabla LR"""
    SHIFT = "shift"      # Desplazar
    REDUCE = "reduce"    # Reducir
    ACCEPT = "accept"    # Aceptar
    ERROR = "error"      # Error


@dataclass
class LRAction:
    """Acción de la tabla LR"""
    action_type: Action
    value: int = None  # Número de estado para shift, número de producción para reduce
    
    def __str__(self):
        if self.action_type == Action.SHIFT:
            return f"s{self.value}"
        elif self.action_type == Action.REDUCE:
            return f"r{self.value}"
        elif self.action_type == Action.ACCEPT:
            return "acc"
        else:
            return "err"


@dataclass
class Production:
    """Producción de la gramática"""
    id: int
    lhs: str  # Lado izquierdo (no terminal)
    rhs: List[str]  # Lado derecho (terminales y no terminales)
    
    def __str__(self):
        return f"{self.lhs} → {' '.join(self.rhs) if self.rhs else 'ε'}"


class LRParser:
    """
    Parser LR(1) con tabla de análisis explícita
    Implementa un autómata de pila para análisis sintáctico ascendente
    """
    
    def __init__(self):
        self.productions = self._create_productions()
        self.action_table = self._create_action_table()
        self.goto_table = self._create_goto_table()
        self.stack = []  # Pila del autómata
        self.input_buffer = []
        self.parse_trace = []  # Traza del análisis
    
    def _create_productions(self) -> List[Production]:
        """
        Define las producciones de la gramática
        Gramática simplificada para Python
        """
        return [
            # 0: S' → program
            Production(0, "S'", ["program"]),
            
            # 1: program → stmt_list
            Production(1, "program", ["stmt_list"]),
            
            # 2-3: stmt_list → stmt stmt_list | stmt
            Production(2, "stmt_list", ["stmt", "stmt_list"]),
            Production(3, "stmt_list", ["stmt"]),
            
            # 4-8: stmt → assign | print | if | while | for
            Production(4, "stmt", ["assign"]),
            Production(5, "stmt", ["print"]),
            Production(6, "stmt", ["if"]),
            Production(7, "stmt", ["while"]),
            Production(8, "stmt", ["for"]),
            
            # 9: assign → ID = expr
            Production(9, "assign", ["ID", "=", "expr"]),
            
            # 10: print → print ( expr )
            Production(10, "print", ["print", "(", "expr", ")"]),
            
            # 11: if → if expr : block
            Production(11, "if", ["if", "expr", ":", "block"]),
            
            # 12: while → while expr : block
            Production(12, "while", ["while", "expr", ":", "block"]),
            
            # 13: for → for ID in expr : block
            Production(13, "for", ["for", "ID", "in", "expr", ":", "block"]),
            
            # 14: block → INDENT stmt_list DEDENT
            Production(14, "block", ["INDENT", "stmt_list", "DEDENT"]),
            
            # 15-16: expr → expr + term | term
            Production(15, "expr", ["expr", "+", "term"]),
            Production(16, "expr", ["term"]),
            
            # 17-18: term → term * factor | factor
            Production(17, "term", ["term", "*", "factor"]),
            Production(18, "term", ["factor"]),
            
            # 19-21: factor → ( expr ) | NUMBER | ID
            Production(19, "factor", ["(", "expr", ")"]),
            Production(20, "factor", ["NUMBER"]),
            Production(21, "factor", ["ID"]),
        ]
    
    def _create_action_table(self) -> Dict[Tuple[int, str], LRAction]:
        """
        Crea la tabla de acciones ACTION[estado, terminal]
        
        Tabla LR(1) simplificada para demostración
        En una implementación completa, esto se generaría automáticamente
        mediante el algoritmo de construcción LR(1)
        """
        action_table = {}
        
        # Estado 0
        action_table[(0, "ID")] = LRAction(Action.SHIFT, 5)
        action_table[(0, "print")] = LRAction(Action.SHIFT, 6)
        action_table[(0, "if")] = LRAction(Action.SHIFT, 7)
        action_table[(0, "while")] = LRAction(Action.SHIFT, 8)
        action_table[(0, "for")] = LRAction(Action.SHIFT, 9)
        
        # Estado 1 - Aceptación
        action_table[(1, "$")] = LRAction(Action.ACCEPT)
        
        # Estado 2 - Reducción program → stmt_list
        action_table[(2, "$")] = LRAction(Action.REDUCE, 1)
        
        # Estado 3 - Reducción stmt_list → stmt
        action_table[(3, "ID")] = LRAction(Action.SHIFT, 5)
        action_table[(3, "print")] = LRAction(Action.SHIFT, 6)
        action_table[(3, "if")] = LRAction(Action.SHIFT, 7)
        action_table[(3, "while")] = LRAction(Action.SHIFT, 8)
        action_table[(3, "for")] = LRAction(Action.SHIFT, 9)
        action_table[(3, "$")] = LRAction(Action.REDUCE, 3)
        action_table[(3, "DEDENT")] = LRAction(Action.REDUCE, 3)
        
        # Estados adicionales para expresiones
        action_table[(5, "=")] = LRAction(Action.SHIFT, 10)
        action_table[(6, "(")] = LRAction(Action.SHIFT, 11)
        
        # Más entradas de la tabla...
        # (En implementación completa, esto se genera automáticamente)
        
        return action_table
    
    def _create_goto_table(self) -> Dict[Tuple[int, str], int]:
        """
        Crea la tabla GOTO[estado, no_terminal]
        
        Define las transiciones entre estados para símbolos no terminales
        """
        goto_table = {}
        
        # Transiciones desde estado 0
        goto_table[(0, "program")] = 1
        goto_table[(0, "stmt_list")] = 2
        goto_table[(0, "stmt")] = 3
        goto_table[(0, "assign")] = 4
        goto_table[(0, "print")] = 4
        goto_table[(0, "if")] = 4
        goto_table[(0, "while")] = 4
        goto_table[(0, "for")] = 4
        
        # Transiciones para expresiones
        goto_table[(10, "expr")] = 15
        goto_table[(11, "expr")] = 16
        
        # Más transiciones...
        # (En implementación completa, esto se genera automáticamente)
        
        return goto_table
    
    def parse(self, tokens: List[Token]) -> bool:
        """
        Realiza el análisis sintáctico LR usando la pila
        
        Args:
            tokens: Lista de tokens del análisis léxico
            
        Returns:
            True si la entrada es aceptada, False en caso contrario
        """
        # Inicializar
        self.stack = [0]  # Pila comienza con estado 0
        self.input_buffer = self._prepare_input(tokens)
        self.parse_trace = []
        
        # Agregar marcador de fin de entrada
        self.input_buffer.append(Token(TokenType.EOF, "$", 0, 0))
        
        ip = 0  # Índice del token actual
        
        while True:
            state = self.stack[-1]  # Estado en el tope de la pila
            current_token = self.input_buffer[ip]
            terminal = self._get_terminal_symbol(current_token)
            
            # Obtener acción de la tabla
            action = self.action_table.get((state, terminal))
            
            if action is None:
                # Error de sintaxis
                self._record_trace(f"ERROR: No hay acción para estado {state} y símbolo '{terminal}'")
                return False
            
            # Registrar traza
            self._record_trace(
                f"Estado: {state}, Símbolo: {terminal}, Acción: {action}, Pila: {self.stack}"
            )
            
            if action.action_type == Action.SHIFT:
                # DESPLAZAR: empujar token y nuevo estado a la pila
                self.stack.append(terminal)
                self.stack.append(action.value)
                ip += 1
                
            elif action.action_type == Action.REDUCE:
                # REDUCIR: aplicar producción
                production = self.productions[action.value]
                
                # Sacar 2 * |rhs| elementos de la pila (símbolo y estado)
                for _ in range(len(production.rhs) * 2):
                    if self.stack:
                        self.stack.pop()
                
                # Estado en el tope después de reducir
                state = self.stack[-1] if self.stack else 0
                
                # Consultar GOTO
                goto_state = self.goto_table.get((state, production.lhs))
                if goto_state is None:
                    self._record_trace(f"ERROR: No hay GOTO para estado {state} y no-terminal '{production.lhs}'")
                    return False
                
                # Empujar no-terminal y nuevo estado
                self.stack.append(production.lhs)
                self.stack.append(goto_state)
                
                self._record_trace(f"REDUCE por producción {action.value}: {production}")
                
            elif action.action_type == Action.ACCEPT:
                # ACEPTAR: análisis exitoso
                self._record_trace("ACEPTADO")
                return True
            
            else:
                # ERROR
                self._record_trace(f"ERROR: Acción de error en estado {state}")
                return False
    
    def _prepare_input(self, tokens: List[Token]) -> List[Token]:
        """Prepara la entrada filtrando tokens irrelevantes"""
        return [t for t in tokens if t.type not in (TokenType.NEWLINE, TokenType.EOF)]
    
    def _get_terminal_symbol(self, token: Token) -> str:
        """Convierte un token a símbolo terminal de la gramática"""
        if token.type == TokenType.IDENTIFIER:
            return "ID"
        elif token.type == TokenType.NUMBER:
            return "NUMBER"
        elif token.type == TokenType.STRING:
            return "STRING"
        elif token.type == TokenType.PRINT:
            return "print"
        elif token.type == TokenType.IF:
            return "if"
        elif token.type == TokenType.WHILE:
            return "while"
        elif token.type == TokenType.FOR:
            return "for"
        elif token.type == TokenType.IN:
            return "in"
        elif token.type == TokenType.ASSIGN:
            return "="
        elif token.type == TokenType.PLUS:
            return "+"
        elif token.type == TokenType.MULTIPLY:
            return "*"
        elif token.type == TokenType.LPAREN:
            return "("
        elif token.type == TokenType.RPAREN:
            return ")"
        elif token.type == TokenType.COLON:
            return ":"
        elif token.type == TokenType.INDENT:
            return "INDENT"
        elif token.type == TokenType.DEDENT:
            return "DEDENT"
        elif token.type == TokenType.EOF:
            return "$"
        else:
            return token.value if token.value else token.type.name
    
    def _record_trace(self, message: str):
        """Registra un paso del análisis"""
        self.parse_trace.append(message)
    
    def get_trace(self) -> str:
        """Retorna la traza completa del análisis"""
        return "\n".join(self.parse_trace)
    
    def print_parsing_table(self) -> str:
        """
        Genera una representación en texto de las tablas ACTION y GOTO
        """
        output = "TABLA DE ANÁLISIS LR(1)\n"
        output += "=" * 100 + "\n\n"
        
        output += "PRODUCCIONES DE LA GRAMÁTICA:\n"
        output += "-" * 100 + "\n"
        for prod in self.productions:
            output += f"  {prod.id}: {prod}\n"
        
        output += "\n" + "=" * 100 + "\n"
        output += "TABLA ACTION (estado, terminal) → acción\n"
        output += "-" * 100 + "\n"
        
        # Agrupar por estado
        states = sorted(set(state for state, _ in self.action_table.keys()))
        for state in states[:10]:  # Mostrar primeros 10 estados
            output += f"\nEstado {state}:\n"
            for (s, term), action in sorted(self.action_table.items()):
                if s == state:
                    output += f"  {term:15} → {action}\n"
        
        output += "\n" + "=" * 100 + "\n"
        output += "TABLA GOTO (estado, no_terminal) → estado\n"
        output += "-" * 100 + "\n"
        
        for state in states[:10]:  # Mostrar primeros 10 estados
            output += f"\nEstado {state}:\n"
            for (s, nonterm), goto_state in sorted(self.goto_table.items()):
                if s == state:
                    output += f"  {nonterm:15} → {goto_state}\n"
        
        return output
    
    def visualize_stack(self) -> str:
        """Visualiza el estado actual de la pila"""
        output = "PILA DEL AUTÓMATA:\n"
        output += "┌" + "─" * 30 + "┐\n"
        
        for i in range(len(self.stack) - 1, -1, -1):
            item = self.stack[i]
            output += f"│ {str(item):28} │\n"
        
        output += "└" + "─" * 30 + "┘\n"
        output += "  (Tope arriba)\n"
        
        return output


def demo_lr_parser():
    """Demostración del parser LR con tabla explícita"""
    print("=" * 80)
    print("DEMOSTRACIÓN DEL PARSER LR(1) CON AUTÓMATA DE PILA")
    print("=" * 80)
    
    parser = LRParser()
    
    # Mostrar tabla de parsing
    print("\n" + parser.print_parsing_table())
    
    # Ejemplo de código simple
    code = "x = 5"
    print(f"\n\nANALIZANDO: {code}\n")
    
    # Tokenizar
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    # Parsear con LR
    result = parser.parse(tokens)
    
    print("\nTRAZA DEL ANÁLISIS:")
    print("-" * 80)
    print(parser.get_trace())
    
    print("\n" + "=" * 80)
    if result:
        print("✅ ANÁLISIS EXITOSO")
    else:
        print("❌ ERROR DE SINTAXIS")
    print("=" * 80)


if __name__ == "__main__":
    demo_lr_parser()
