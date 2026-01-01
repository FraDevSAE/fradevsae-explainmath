from explainmath import Value

a = Value(10)
b = Value(0)
c = a.div(b)

print("Valid:", c.is_valid())          # False
print("Reason:", c.reason)             # Reason.DivisionByZero
print("Explanation:", c.explanation)   # Human readable message
