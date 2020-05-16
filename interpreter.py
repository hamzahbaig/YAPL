
import ply.yacc as yacc
from myParser import parser


variableValues = {}


def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == "^":
            return run(p[1]) ** run(p[2])
        elif p[0] == "==":
            return run(p[1]) == run(p[2])
        elif p[0] == "!=":
            return run(p[1]) != run(p[2])
        elif p[0] == "<":
            return run(p[1]) < run(p[2])
        elif p[0] == "<=":
            return run(p[1]) <= run(p[2])
        elif p[0] == ">":
            return run(p[1]) > run(p[2])
        elif p[0] == ">=":
            return run(p[1]) >= run(p[2])
        elif p[0] == "AND":
            return run(p[1]) and run(p[2])
        elif p[0] == "OR":
            return run(p[1]) or run(p[2])
        elif p[0] == "not":
            return (not run(p[1]))
        elif p[0] == "++":
            ans = run(p[1])
            if p[1][0] == "var":
                ans += 1
                variableValues[p[1][1]]["value"] = ans
                return ans
            elif p[1][0] == "const":
                ans += 1
                return ans
        elif p[0] == "--":
            ans = run(p[1])
            if p[1][0] == "var":
                ans -= 1
                variableValues[p[1][1]]["value"] = ans
                return ans
            elif p[1][0] == "const":
                ans -= 1
                return ans
        elif p[0] == '=':
            if p[2] not in variableValues:
                variableValues[p[2]] = {"type": p[1], "value": run(p[3])}
            else:
                return "Redeclaration Error"
        elif p[0] == 'var':
            if p[1] not in variableValues:
                return "Undeclared Variable Found"
            else:
                return variableValues[p[1]]['value']
        elif p[0] == "const":
            return p[1]
        elif p[0] == "bool":
            if p[1] == "True":
                return True
            elif p[1] == "False":
                return False
        elif p[1] == "print":
            tobePrinted = ""
            for arg in p[2]:
                tobePrinted += str(run(arg)) + " "
            print(tobePrinted)

    else:
        return p


while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    result = parser.parse(s)
    print("result: ", result)
    print(run(result[1]))
