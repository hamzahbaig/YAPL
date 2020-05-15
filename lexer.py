import ply.lex as lex


tokens = (
    'INT',
    'PLUS',
    'EQUALS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LRB',  # (
    'RRB',  # )
    'PRINT',
    'SEMICOLON',  # ;
    'COMMA',  # ,
    'STRING',
    'IDENTIFIER',
    'DOUBLE',
    'TYPEINT',
    'TYPEDOUBLE',
    'TYPESTRING',
    'TYPEBOOL',
    'TRUE',
    'FALSE',
    'POWER',
    'INCREMENT',
    'DECREMENT',
    "AND",
    "EQUALEQUAL",
    "GE",
    "GT",
    "LE",
    "LT",
    "NOT",
    "OR",
    "NE"
)

t_EQUALEQUAL = r'=='
t_GE = r'>='
t_GT = r'>'
t_LE = r'<='
t_LT = r'<'
t_NE = r'!='

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='

t_LRB = r'\('
t_RRB = r'\)'
t_SEMICOLON = r';'
t_COMMA = r'\,'
t_ignore = r' '


def t_AND(t):
    r'AND'
    return t


def t_OR(t):
    r'OR'
    return t

def t_NOT(t):
    r'NOT'
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


def t_PRINT(t):
    r'PRINT'
    return t


def t_INCREMENT(t):
    r'\+\+'
    return t


def t_DECREMENT(t):
    r'\-\-'
    return t


def t_POWER(t):
    r'\^'
    return t


def t_DOUBLE(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_TRUE(t):
    r'TRUE'
    return t


def t_FALSE(t):
    r'FALSE'
    return t


def t_TYPEINT(t):
    r'INT'
    return t


def t_TYPESTRING(t):
    r'STRING'
    return t


def t_TYPEDOUBLE(t):
    r'DOUBLE'
    return t


def t_TYPEBOOL(t):
    r'BOOL'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-z_][a-zA-Z_0-9]*'
    return t


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()
