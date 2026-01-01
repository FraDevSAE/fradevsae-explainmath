fradevsae-explainmath

🔢 ExplainMath

A small Python library that stops silent numeric failures and explains why math breaks.




🚀 Install

```bash pip install explainmath ```




💡 What problem does it solve?

In normal Python:

```python x = 10 / 0 # crash y = float("nan") # spreads silently

Silent numeric failures poison data pipelines. Debugging becomes guesswork.

```

ExplainMath catches failure at the moment it happens:

```python from explainmath import Value

a = Value(10) b = Value(0) c = a.div(b)

print(c.is_valid()) # False print(c.explanation) # "Division by zero while evaluating 10 / 0" ```




🧪 Strict Mode

```python from explainmath import Value, SemanticError

try: Value(10).div(Value(0)).require() except SemanticError as e: print("Error caught:", e) ```




📦 Examples

```python from explainmath import Value

Value(10).add(Value(5)).value # 15 Value(10).div(Value(0)).is_valid() # False

See more in examples/

```




📈 Roadmap

•
v0.2 → History & provenance tracking

•
ExplainMath Pro → Visual traces, report export

•
SAE SDK integration → long-term vision




🌐 Links

•
🔗 PyPI: https://pypi.org/project/explainmath

•
🔗 GitHub: https://github.com/FraDevSAE/fradevsae-explainmath




Made for developers who hate debugging NaN. Minimal. Safe. Clear.

