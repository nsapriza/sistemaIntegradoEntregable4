import ply.lex as lex

# Lista de tokens
tokens = (
    'SELECT', 'FROM', 'WHERE', 'GROUP_BY', 'JOIN', 'ON', 'DISTINCT', 'COUNT',
    'INSERT_INTO', 'VALUES', 'UPDATE', 'SET', 'DELETE_FROM', 'ORDER_BY', 'LIMIT',
    'HAVING', 'EXISTS', 'IN', 'BETWEEN', 'LIKE', 'IS_NULL', 'ALTER_TABLE',
    'ADD_COLUMN', 'DROP_COLUMN', 'CREATE_TABLE', 'DROP_TABLE', 'DEFAULT', 'UNIQUE',
    'PRIMARY_KEY', 'FOREIGN_KEY', 'NOT_NULL', 'CAST', 'NAME', 'NUMB','SYM'
)

# Reglas de los tokens
t_SELECT = r'TRAEME'
t_FROM = r'DELATABLA'
t_WHERE = r'DONDE'
t_GROUP_BY = r'AGRUPANDOPOR'
t_JOIN = r'MEZCLANDO'
t_ON = r'EN'
t_DISTINCT = r'LOSDISTINTOS'
t_COUNT = r'CONTANDO'
t_INSERT_INTO = r'METEEN'
t_VALUES = r'LOSVALORES'
t_UPDATE = r'ACTUALIZA'
t_SET = r'SETEA'
t_DELETE_FROM = r'BORRADELA'
t_ORDER_BY = r'ORDENAPOR'
t_LIMIT = r'COMOMUCHO'
t_HAVING = r'WHEREDELGROUPBY'
t_EXISTS = r'EXISTE'
t_IN = r'ENESTO'
t_BETWEEN = r'ENTRE'
t_LIKE = r'PARECIDOA'
t_IS_NULL = r'ESNULO'
t_ALTER_TABLE = r'CAMBIALATABLA'
t_ADD_COLUMN = r'AGREGALACOLUMNA'
t_DROP_COLUMN = r'ELIMINALACOLUMNA'
t_CREATE_TABLE = r'CREALATABLA'
t_DROP_TABLE = r'TIRALATABLA'
t_DEFAULT = r'PORDEFECTO'
t_UNIQUE = r'UNICO'
t_PRIMARY_KEY = r'CLAVEPRIMA'
t_FOREIGN_KEY = r'CLAVEREFERENTE'
t_NOT_NULL = r'NONULO'
t_CAST = r'TRANSFORMAA'
t_NAME = r'[a-z_][a-z0-9_]*'
t_NUMB = r'[0-9_][0-9_]*'
t_SYM = r'<|>|=|(==)'

# Regla para ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
data = 'TRAEME LOS DISTINTOS DE LA TABLA DONDE edad > 30'
data = "".join(data.split(" "))
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
