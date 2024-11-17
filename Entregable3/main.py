import ply.lex as lex
import ply.yacc as yacc
import re

tokens = (
    'SELECT', 'FROM', 'WHERE', 'GROUP_BY', 'JOIN', 'ON', 'DISTINCT', 'COUNT',
    'INSERT_INTO', 'VALUES', 'UPDATE', 'SET', 'DELETE_FROM', 'ORDER_BY', 'LIMIT',
    'HAVING', 'IN', 'BETWEEN', 'LIKE', 'AND', 'TODO',  
    'ALTER_TABLE', 'ADD_COLUMN', 'DROP_COLUMN', 'CREATE_TABLE', 'DEFAULT', 'UNIQUE',
    'PRIMARY_KEY', 'FOREIGN_KEY', 'NOT_NULL', 'NAME', 'NUMB', 'DOT', 'EQUALS', 'GREATER','SEMI', 'LPAREN',
    'RPAREN', 'COMMA', 'ASTERISK', 'VARCHAR', 'OR', 'LESSER'
)

t_VARCHAR = r'VARCHAR'
t_SELECT = r'TRAEME|SELECT'
t_FROM = r'DELATABLA|FROM'
t_WHERE = r'DONDE|WHERE'
t_GROUP_BY = r'AGRUPANDOPOR|GROUP BY'
t_JOIN = r'MEZCLANDO|JOIN'
t_ON = r'EN|ON'
t_DISTINCT = r'LOSDISTINTOS|DISTINCT'
t_COUNT = r'CONTANDO|COUNT'
t_INSERT_INTO = r'METEEN|INSERT INTO'
t_VALUES = r'LOS VALORES|VALUES'
t_UPDATE = r'ACTUALIZA|UPDATE'
t_SET = r'SETEA|SET'
t_DELETE_FROM = r'BORRADELA|DELETE FROM'
t_ORDER_BY = r'ORDENA POR|ORDER BY'
t_LIMIT = r'COMO\s+MUCHO|LIMIT'
t_HAVING = r'WHEREDELGROUPBY|HAVING'
t_IN = r'EN\s+ESTO|IN'
t_BETWEEN = r'ENTRE|BETWEEN'
t_LIKE = r'PARECIDOA|LIKE'
t_AND = r'Y|AND'
t_OR = r'O|OR'
t_ALTER_TABLE = r'CAMBIALATABLA|ALTER\s+TABLE'
t_ADD_COLUMN = r'AGREGALACOLUMNA|ADD\s+COLUMN'
t_DROP_COLUMN = r'ELIMINALACOLUMNA|DROP\s+COLUMN'
t_CREATE_TABLE = r'CREALATABLA|CREATE\s+TABLE'
t_DEFAULT = r'PORDEFECTO|DEFAULT'
t_UNIQUE = r'UNICO|UNIQUE'
t_PRIMARY_KEY = r'CLAVEPRIMA|PRIMARY\s+KEY'
t_FOREIGN_KEY = r'CLAVEREFERENTE|FOREIGN\s+KEY'
t_NOT_NULL = r'NONULO|NOT\s+NULL'
t_TODO = r'TODO'  # Token para el equivalente de *
t_NAME = r'[a-z_][a-z0-9_]*'
t_NUMB = r'\d+'

t_DOT = r'\.'
t_EQUALS = r'='
t_GREATER = r'>'
t_LESSER = r'<'
t_SEMI = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ASTERISK = r'\*'  

t_ignore = ' \t'
t_ignore_COMILLAS = r"\'"


def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_query(p):
    '''
    query : select_statement
          | insert_statement
          | update_statement
          | delete_statement
          | create_table_statement
          | alter_table_statement
    '''
    print("Consulta válida:", p[1])

def p_select_statement(p):
    '''
    select_statement : SELECT selection FROM NAME join_clause where_clause group_by_clause having_clause order_by_clause limit_clause SEMI
    '''
    p[0] = ('SELECT', p[2], p[4], p[5], p[6], p[7], p[8], p[9])

def p_selection(p):
    '''
    selection : DISTINCT NAME
              | TODO
              | COUNT LPAREN NAME RPAREN
              | COUNT LPAREN TODO RPAREN
              | ASTERISK
              | NAME
    '''

    if p[1] == '*':
        p[0] = '*'
    else:
        p[0] = p[1]

def p_condition_list(p):
    '''
    condition_list : condition
                   | condition AND condition_list
                   | condition OR condition_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1], p[2]] + p[3]

def p_join_clause(p):
    '''
    join_clause : JOIN NAME ON NAME DOT NAME EQUALS NAME DOT NAME
                | empty
    '''
    p[0] = p[1]

def p_where_clause(p):
    '''
    where_clause : WHERE condition_list
                 | empty
    '''
    p[0] = p[1] if p[1] != 'empty' else None

def p_group_by_clause(p):
    '''
    group_by_clause : GROUP_BY NAME
                    | empty
    '''
    p[0] = p[1]

def p_having_clause(p):
    '''
    having_clause : HAVING condition
                  | empty
    '''
    p[0] = p[1]

def p_order_by_clause(p):
    '''
    order_by_clause : ORDER_BY NAME
                    | empty
    '''
    p[0] = p[1]

def p_limit_clause(p):
    '''
    limit_clause : LIMIT NUMB
                 | empty
    '''
    p[0] = p[1]

def p_insert_statement(p):
    '''
    insert_statement : INSERT_INTO NAME LPAREN value_list RPAREN VALUES LPAREN value_list RPAREN SEMI
    '''
    p[0] = ('INSERT_INTO', p[2], p[4], p[8])

def p_value_list(p):
    '''
    value_list : value_list COMMA NAME
               | NAME COMMA NAME
               | NAME COMMA NUMB
               | NAME
               | NUMB
    '''
    if len(p) == 2:  
        p[0] = [p[1]]
    elif len(p) == 4:  
        p[0] = p[1] if isinstance(p[1], list) else [p[1]]
        p[0].append(p[3])


def p_update_statement(p):
    '''
    update_statement : UPDATE NAME SET NAME EQUALS NAME where_clause SEMI
                    | UPDATE NAME SET NAME EQUALS NUMB where_clause SEMI
    '''
    p[0] = ('UPDATE', p[2], p[4], p[6], p[7])

def p_delete_statement(p):
    '''
    delete_statement : DELETE_FROM NAME where_clause SEMI
    '''
    p[0] = ('DELETE_FROM', p[2], p[3])

def p_create_table_statement(p):
    '''
    create_table_statement : CREATE_TABLE NAME '(' column_definitions ')'
    '''
    p[0] = ('CREATE_TABLE', p[2], p[4])

def p_column_definitions(p):
    '''
    column_definitions : column_definitions ',' column_definition
                       | column_definition
    '''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_column_definition(p):
    '''
    column_definition : NAME type constraints
    '''
    p[0] = (p[1], p[2], p[3])

def p_type(p):
    '''
    type : NAME
         | VARCHAR LPAREN NUMB RPAREN 
    '''
    p[0] = p[1]

def p_constraints(p):
    '''
    constraints : constraints constraint
                | empty
    '''
    p[0] = p[1]

def p_constraint(p):
    '''
    constraint : NOT_NULL
               | UNIQUE
               | PRIMARY_KEY
               | FOREIGN_KEY
               | DEFAULT NAME
    '''
    p[0] = p[1:]

def p_alter_table_statement(p):
    '''
    alter_table_statement : ALTER_TABLE NAME add_drop_column SEMI
    '''
    p[0] = ('ALTER_TABLE', p[2], p[3])

def p_add_drop_column(p):
    '''
    add_drop_column : ADD_COLUMN NAME type not_null_option
                    | DROP_COLUMN NAME
    '''
    if len(p) == 5:  
        p[0] = (p[1], p[2], p[3], p[4])  
    else:  
        p[0] = p[1:]

def p_not_null_option(p):
    '''
    not_null_option : NOT_NULL
                    | empty
    '''
    p[0] = p[1] if p[1] else None  


# Condiciones
def p_condition(p):
    '''
    condition : NAME EQUALS NUMB
              | NAME EQUALS NAME
              | NAME BETWEEN NUMB AND NUMB
              | NAME LIKE NAME
              | NAME GREATER NUMB
              | NAME IN '(' value_list ')'
              | NAME DOT NAME EQUALS NUMB
              | NAME DOT NAME EQUALS NAME
              | COUNT LPAREN TODO RPAREN GREATER NUMB
              | NAME LESSER NUMB
              | COUNT LPAREN TODO RPAREN LESSER NUMB
    '''
    p[0] = p[1:]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    raise SyntaxError("Error de sintaxis")

parser = yacc.yacc()

if __name__ == "__main__":
    a = []
    a.append("TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;")
    a.append("TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad ='madrid';")
    a.append("METE EN usuarios (nombre, edad) LOSVALORES ('juan', 25);")
    a.append("ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';")
    a.append("TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'barcelona';")
    a.append("TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO(TODO) > 5;")
    a.append("BORRA DE LA tabla clientes DONDE edad ENTRE 18 Y 25;")
    a.append("CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;")
    a.append("CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;")
    a.append("TRAEME TODO DE LA TABLA usuarios DONDE edad > 18 Y puesto = 'ingeniero';")
    num = 0
    for i in a:
        a[num] = "".join(a[num].split(" "))  # Eliminación de espacios para la prueba
        print(a[num])
        lexer.input(a[num])
        print("Tokens reconocidos:")
        for tok in lexer:
            print(tok)
        parser.parse(a[num])
        num += 1
