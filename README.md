# 🚀 DT Fellowship Assignment: Daily Reflection Tree

## 📋 Overview
**Deterministic employee reflection tool** - No LLM at runtime. Guides users through 3 psychological axes via fixed-choice questions with branching reflections.

**Status:** Part A **COMPLETE** (28 nodes, meets all requirements)

## 📁 Repository Structure
daily-reflection-tree/
├── tree/
│   ├── reflections-tree.json    # 28 nodes, 9 questions (3 axes)
│   └── tree-diagram.png         # Mermaid flowchart
├── agent/                       # Part B (optional - time constrained)
├── transcripts/                 # Part B sample runs
└── write-up.md                  # Design rationale + psych sources

## 🎯 Tree Specifications (All Met)
| Requirement | Delivered |
|-------------|-----------|
| Total nodes | **28+** ✓ |
| Questions | **9** (3 axes) ✓ |
| Decision nodes | **4+** ✓ |
| Reflections | **5+** ✓ |
| Bridges | **2** ✓ |
| Summary | **1** ✓ |

## 🧠 Psychological Axes Covered
1. **Locus of Control** (Rotter 1954): Victim vs Victor
2. **Contribution vs Entitlement** (Campbell 2004)  
3. **Self vs Team Focus** (Maslow Self-Transcendence)

## 🔍 How to Navigate Tree
**JSON Format:** `id | parentId | type | text | options | target | signal`

**Sample Path:**
Tough day → "Blamed others" → External locus reflection → Axis 2
Productive → "My preparation" → Internal locus → Axis 2
## ⏱️ Time Constraint Note
Prioritized **question quality (35% weight)** over Part B coding. Tree is production-ready - any developer can build agent from this data.

## 📧 Submission Ready
**DT-CultureTech Fellowship Assignment - Part A Complete**
**Candidate:** [Prashansa Choubey]
**Deadline:** April 23, 2026

---

**Ready for review!** All mandatory deliverables included.
