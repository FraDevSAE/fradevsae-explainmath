---
title: ExplainMath
nav_order: 1
---

# ExplainMath

Safe numeric operations for Python.

ExplainMath prevents silent numeric failures such as NaN and infinity,
and explains *why* a calculation failed.

---

## Install

pip install explainmath

---

## Why ExplainMath?

In plain Python, numeric failures either crash or silently spread.

Example:

10 / 0        -> crash  
float("nan") -> silently spreads

ExplainMath makes failures explicit and traceable.

---

## Basic usage

from explainmath import Value

a = Value(10)
b = Value(0)

c = a.div(b)

c.is_valid()        -> False  
c.explanation       -> "Division by zero while evaluating 10 / 0"

---

## Strict mode

from explainmath import Value, SemanticError

Value(10).div(Value(0)).require()
# raises SemanticError

---

## Roadmap

v0.2 — history & provenance tracking  
ExplainMath Pro — visual traces & reports  
SAE integration — long-term vision

---

Links:
PyPI: https://pypi.org/project/explainmath  
GitHub: https://github.com/FraDevSAE/fradevsae-explainmath

