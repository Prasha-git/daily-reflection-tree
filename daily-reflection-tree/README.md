# DT Fellowship Assignment: Daily Reflection Tree

## Part A: Tree Design (Complete)

**Files:**
- `tree/reflections-tree.json` - 28 nodes, 9 questions covering all 3 axes
- `tree/tree-diagram.png` - Mermaid flowchart visualization  
- `write-up.md` - Design rationale + psychological sources

**Structure:** Deterministic decision tree with fixed options, no LLM at runtime.

## How to Read Tree
Columns: `id | parentId | type | text | options | target | signal`
- **question**: User picks from 4 options
- **decision**: Routes by prior answer
- **reflection**: Interpolates user choices
- Axes flow: Locus → Orientation → Radius → Summary

## Paths Example
Tough day → "Blame others" → external locus reflection
Productive → "My preparation" → internal locus reflection
**Part B (Agent)**: Empty - focused on core tree quality per time constraint.