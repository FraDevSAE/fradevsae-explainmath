---
title: Getting Started
nav_order: 2
---

# Getting Started

This guide shows how to install and use ExplainMath for the first time.

---

## Install

Open a terminal and run:

pip install explainmath

---

## Basic Use

from explainmath import Value

a = Value(5)
b = Value(3)

result = a.add(b)
print(result.value)  # 8

---

## What happens with invalid math?

from explainmath import Value

x = Value(10)
y = Value(0)

z = x.div(y)

print(z.is_valid())     # False
print(z.explanation)    # "Division by zero while evaluating 10 / 0"

This is the core purpose: invalid results don't hide.
