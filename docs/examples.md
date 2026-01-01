---
title: Examples
nav_order: 3
---

# Examples

Here are some small examples showing how to use ExplainMath.

---

## Basic Math

from explainmath import Value

Value(10).add(Value(5)).value      # 15  
Value(10).sub(Value(3)).value      # 7  
Value(4).mul(Value(2)).value       # 8

---

## Division

from explainmath import Value

Value(9).div(Value(3)).value       # 3  
Value(9).div(Value(0)).is_valid()  # False

---

## Strict Mode (raises errors)

from explainmath import Value, SemanticError

try:
    Value(10).div(Value(0)).require()
except SemanticError as e:
    print("Math failed safely:", e)
