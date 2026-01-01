---
title: ExplainMath
nav_order: 1
---

# 🔢 ExplainMath

> **Safe numeric operations for Python — no silent NaN or infinite propagation.**  
> Clear errors. Traceable failures. Math you can trust.

[Get Started](getting-started.md){ .btn .btn-primary }
[Examples](examples.md){ .btn }
[API Docs](api.md){ .btn }

---

## 🚀 Install

```bash
pip install explainmath
💡 Why ExplainMath?
In plain Python:

python
Copy code
x = 10 / 0         # crashes
y = float("nan")   # silently spreads
Silent numeric failures make debugging guesswork.

ExplainMath stops that.

python
Copy code
from explainmath import Value

a = Value(10)
b = Value(0)
c = a.div(b)

print(c.is_valid())      # False
print(c.explanation)     # "Division by zero while evaluating 10 / 0"
🧪 Strict Mode
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
See more examples here:
🔗 https://github.com/FraDevSAE/fradevsae-explainmath/tree/main/examples

📈 Roadmap
Version	Feature
v0.2	Operation history & provenance tracking
Pro	Visual trace graphs + error reports
Future	SAE Semantic Engine integration

🌐 Links
PyPI: https://pypi.org/project/explainmath

GitHub: https://github.com/FraDevSAE/fradevsae-explainmath

Minimal. Safe. Transparent.
For developers tired of chasing NaN through pipelines.