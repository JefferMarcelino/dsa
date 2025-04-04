# Backtracking Exercises

This directory contains Python implementations of classic backtracking problems. Each script showcases a recursive approach that explores all possible configurations while **pruning** invalid ones — a core idea of backtracking.

## 🧠 What is Backtracking?

Backtracking is a problem-solving technique that builds candidates for a solution **incrementally**, and abandons ("backtracks") a candidate as soon as it determines that the candidate cannot possibly lead to a valid solution.

> Think of it as **"try → fail → undo → try something else"**.

### Each backtracking solution usually involves:
- A **recursive function** that explores the decision space.
- A **base case** that adds a valid solution.
- A way to **undo the last move** (backtrack) and try alternatives.

## 📘 Additional Concepts

- **Pruning**: Skipping paths that are known to lead to invalid or duplicate solutions.
- **Decision Tree**: Visualize backtracking as exploring a tree of decisions.
- **State Tracking**: Most problems involve keeping track of partial state (like current subset or board layout) and modifying it during recursion.
