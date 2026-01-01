---
title: ExplainMath
nav_order: 1
---

# 🔢 ExplainMath

> **Safe numeric operations for Python — no silent NaN or infinite propagation.**  
> Clear errors. Traceable failures. Math you can trust.

---

## 🚀 Install

```bash
pip install explainmath
💡 Why ExplainMath?
Normal Python:
python
Copy code
x = 10 / 0         # crash
y = float("nan")   # silently spreads
Failures propagate, bugs stay hidden.

With ExplainMath:
python
Copy code
from explainmath import Value

a = Value(10)
b = Value(0)
c = a.div(b)

print(c.is_valid())      # False
print(c.explanation)     # "Division by zero while evaluating 10 / 0"
🧪 Strict Mode (safe-by-default)
python
Copy code
from explainmath import Value, SemanticError

try:
    Value(10).div(Value(0)).require()
except SemanticError as e:
    print("Error caught:", e)
📦 Quick Examples
python
Copy code
from explainmath import Value

Value(10).add(Value(5)).value      # 15
Value(10).div(Value(0)).is_valid() # False
📈 Roadmap
Feature	Status
v0.1.1 Core + PyPI published	✅ Done
v0.2 Provenance tracking	⏳ Next
ExplainMath Pro (visual trace)	Planned
SAE integration long-term	Vision

🌐 Links
🔗 PyPI: https://pypi.org/project/explainmath
🔗 GitHub: https://github.com/FraDevSAE/fradevsae-explainmath
🔗 Examples Folder: https://github.com/FraDevSAE/fradevsae-explainmath/tree/main/examples

Minimal. Transparent. Reliable math.