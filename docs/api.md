---
title: API Reference
nav_order: 4
---

# API Reference

This page documents the `Value` class and its methods.

---

## Import

from explainmath import Value

---

## Class: Value

`Value(number, status=VALID, reason=None)`

Represents a number with safety tracking.

### Attributes

| Attribute | Description |
|----------|-------------|
| `.value` | Underlying Python number (only available if valid) |
| `.is_valid()` | Returns True/False |
| `.explanation` | Human-readable reason when invalid |
| `.require()` | Raises `SemanticError` if invalid |

---

## Methods

| Method | Description |
|-------|-------------|
| `add(other)` | Safe addition |
| `sub(other)` | Safe subtraction |
| `mul(other)` | Safe multiplication |
| `div(other)` | Safe divide — invalid when dividing by zero |
| `pow(other)` | Power operation — tracks invalid states |

---

## Example Usage

from explainmath import Value

a = Value(6)
b = Value(2)

print(a.mul(b).value)      # 12
print(a.div(Value(0)))     # Invalid result object

try:
    a.div(Value(0)).require()
except Exception as e:
    print(e)               # "Division by zero"
