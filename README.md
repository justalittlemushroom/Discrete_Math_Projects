# Computational Mathematics Projects

A collection of Python implementations for fundamental computational mathematics and computer science algorithms, including SAT solving, game theory, and combinatorial mathematics.

## 🧮 Projects Overview

### 1. SAT Solver (Boolean Satisfiability)
Implementation of a SAT solver using unit propagation and backtracking to determine if a given Boolean formula in CNF (Conjunctive Normal Form) is satisfiable.

**Key Features:**
- Converts CNF formulas to implication graphs
- Uses BFS traversal for conflict detection
- Implements backtracking for variable assignment
- Handles unsatisfiable formulas gracefully

**Algorithm Approach:**
- Unit propagation through implication graphs
- Systematic variable assignment with conflict resolution
- Backtracking when contradictions are detected

### 2. Nim Game with Optimal Strategy
Interactive implementation of the classic Nim game with computer opponent using optimal game theory strategy.

**Key Features:**
- Visual board representation with binary display
- Human vs. Computer gameplay
- Optimal strategy calculation using XOR (nimber) operations
- Real-time move validation and board updates

**Game Theory Implementation:**
- Calculates game balance using bitwise XOR operations
- Implements winning strategy based on nimber theory
- Provides optimal moves to maintain winning positions

### 3. Combinatorial Pairing Problem
Mathematical analysis of valid brother-sister pairing arrangements with multiple algorithmic approaches.

**Key Features:**
- **Brute Force Approach**: Generates all permutations and validates constraints
- **Recurrence Relations**: Two different mathematical formulations using:
  - R(n) and T(n) recurrence with binomial coefficients
  - Simplified T(n) recurrence with direct calculation
- Comparative analysis of different solution methods

## 🛠 Technical Implementation

**Language**: Python 3.x

**Core Algorithms:**
- Graph traversal (BFS for SAT solver)
- Backtracking and constraint satisfaction
- Game theory and optimal strategy calculation
- Combinatorial enumeration and recurrence relations
- Bitwise operations and mathematical optimization

**Data Structures:**
- Dictionaries for variable assignments and implications
- Lists for clause representation and game state
- Permutation generation using itertools

## 🎯 Mathematical Concepts Demonstrated

### SAT Solving
- Boolean algebra and logical satisfiability
- Constraint satisfaction problems
- Graph theory applications in logic

### Game Theory
- Nimber arithmetic and XOR operations
- Optimal strategy calculation
- Zero-sum game analysis

### Combinatorics
- Permutation and combination calculations
- Recurrence relation formulation
- Mathematical proof verification through computation

## 🚀 Usage Examples

### SAT Solver
```python
# Input: CNF formula in text file format
# Output: Variable assignments or "FALSE" if unsatisfiable
python sat_solver.py
```

### Nim Game
```python
# Interactive gameplay with optimal computer opponent
python nim_game.py
# Enter number of rows and squares per row
# Take turns removing squares until game ends
```

### Pairing Problem
```python
# Analyzes brother-sister pairing arrangements
python pairing_problem.py
# Enter number of pairs to analyze
# Compares three different solution approaches
```

## 🔧 Key Technical Features

### Efficient Algorithms
- Optimized graph traversal for SAT solving
- Mathematical optimization in game strategy
- Multiple algorithmic approaches for comparison

### Error Handling
- Input validation for all user interactions
- Graceful handling of edge cases
- Clear feedback for invalid operations

### Mathematical Accuracy
- Precise combinatorial calculations
- Correct implementation of game theory principles
- Verified results through multiple solution methods

## 🎯 Learning Outcomes

- **Algorithm Design**: Implementation of classic CS algorithms
- **Mathematical Programming**: Translation of mathematical concepts to code
- **Optimization Techniques**: Efficient problem-solving approaches
- **Game Theory Application**: Practical implementation of optimal strategies
- **Combinatorial Analysis**: Multiple approaches to counting problems

---

*Built to demonstrate computational mathematics concepts, algorithm implementation, and mathematical problem-solving through programming.*
