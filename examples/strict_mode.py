from explainmath import Value, SemanticError

a = Value(10)
b = Value(0)

try:
    a.div(b).require()
except SemanticError as e:
    print("Error caught:", e)
