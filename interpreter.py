
import ply.yacc as yacc
from myParser import parser
import sys
import copy

variableValues = {}
structDict = {}


def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            try:
                return run(p[1]) + run(p[2])
            except:
                print("TypeError")
                sys.exit(1)
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
                variableValues[p[2]] = {"type": p[1],
                                        "value": run(p[3])}  # FOR NOW
                return "Redeclaration Error"
        elif p[0] == 'var':
            if p[1] not in variableValues:
                return "Undeclared Variable Found"
            else:
                return variableValues[p[1]]['value']
        elif p[0] == "structVar":
            if p[2] not in structDict[p[1]]:
                return ("AttributeError")
            return structDict[p[1]][p[2]]['value']
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
        elif p[0] == "dowhile":
            expression = p[2]
            while run(p[1]):
                for exp in expression:
                    run(exp)
        elif p[0] == "assign":
            return (p[1], p[2])
        elif p[0] == "structAssign":
            if p[1] in structDict:
                structDict[p[2]] = copy.deepcopy(structDict[p[1]])
        elif p[0] == "struct":
            structDict[p[1]] = {}
            for exp in p[2]:
                t, n = run(exp)
                structDict[p[1]][n] = {"type": t, "value": None}
        elif p[0] == "structDec":
            structName = p[1]
            varName = p[2]
            value = run(p[3])
            structDict[structName][varName]["value"] = value

    else:
        return p


filename = sys.argv[1]
f = open(filename, 'r')
lines = f.readlines()
command = ""
for line in lines:
    line = line.strip('\n')
    command += line + " "

# print(command)


result = parser.parse(command)
for tree in result[1]:
    run(tree)


# while True:
#     try:
#         s = input('>> ')
#     except EOFError:
#         break
#     result = parser.parse(s)
#     print("result: ", result)
#     for tree in result[1]:
#         (run(tree))
