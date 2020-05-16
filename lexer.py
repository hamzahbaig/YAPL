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
    'LCB',
    'RCB',
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
    'True',
    'False',
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
    "NE",
    "DO",
    "WHILE",
    "STRUCT",
    "DOT"
)

t_EQUALEQUAL = r'=='
t_GE = r'>='
t_GT = r'>'
t_LE = r'<='
t_LT = r'<'
t_NE = r'!='
t_SEMICOLON = r';'

t_DOT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='

t_LRB = r'\('
t_RRB = r'\)'
t_LCB = r'\{'
t_RCB = r'\}'
t_COMMA = r'\,'
t_ignore = ' \t\v\r\n'


def t_STRUCT(t):
    r'STRUCT'
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


def t_WHILE(t):
    r'WHILE'
    return t


def t_AND(t):
    r'AND'
    return t


def t_DO(t):
    r'DO'
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


def t_True(t):
    r'True'
    return t


def t_False(t):
    r'False'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-z_][a-zA-Z_0-9]*'
    return t


def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


lexer = lex.lex()
