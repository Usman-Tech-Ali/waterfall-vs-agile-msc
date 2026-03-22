# Methodology Decision-Support Scoring Matrix
**Based on Primary Simulation + Literature Review**

---

## Overview

This document explains the scoring logic used in the decision-support tool to recommend Agile, Waterfall, or Hybrid methodologies based on project characteristics.

---

## Scoring Factors

### 1. Requirements Volatility (1-10 scale)
- **1 = Fully fixed requirements** (e.g., government contract with frozen scope)
- **10 = Highly volatile requirements** (e.g., startup MVP, AI-driven innovation)

**Agile Advantage:** +7 points per volatility point (max +70)
- Agile thrives on changing requirements through iterative development
- Backlog-driven approach enables seamless requirement evolution

**Waterfall Advantage:** +(10 - volatility) × 7 points (max +70)
- Waterfall excels with stable requirements
- Upfront planning reduces rework when requirements are fixed

**Rationale:** Simulation showed Agile absorbed 3 change requests with zero schedule impact, while Waterfall required formal change control and regression testing.

### 2. Regulatory Intensity
- **None:** No compliance requirements
- **Low:** Some documentation/audit requirements (e.g., internal standards)
- **High:** Strict compliance (e.g., HIPAA, SOX, PCI-DSS)

**Waterfall Advantage:**
- None: 0 points
- Low: +10 points
- High: +25 points

**Agile Penalty:**
- None: 0 points
- Low: 0 points
- High: -15 points

**Rationale:** Waterfall's formal documentation and change control are valuable in regulated environments. Agile's continuous integration may conflict with compliance requirements.

### 3. Team Size
- **Solo:** Single developer
- **Small:** 2-5 developers
- **Large:** 6+ developers

**Agile Advantage:**
- Solo: +10 points (minimal coordination overhead)
- Small: +10 points (easy communication)
- Large: 0 points (coordination overhead increases)

**Waterfall Advantage:**
- Solo: 0 points
- Small: 0 points
- Large: +15 points (upfront planning reduces coordination overhead)

**Rationale:** Agile's iterative approach works well for small teams with easy communication. Waterfall's upfront planning helps large distributed teams coordinate.

### 4. Team Distribution
- **Co-located:** All team members in same location
- **Hybrid:** Mix of co-located and remote
- **Remote:** Fully distributed team

**Agile Penalty:**
- Co-located: 0 points
- Hybrid: -5 points
- Remote: -10 points

**Waterfall Advantage:**
- Co-located: 0 points
- Hybrid: +5 points
- Remote: +10 points

**Rationale:** Agile relies on frequent communication and collaboration, which is harder in distributed teams. Waterfall's documentation reduces communication needs.

### 5. Project Type
- **Fixed-scope:** Well-defined, bounded project (e.g., data migration)
- **Cloud-native:** Modern cloud architecture (e.g., microservices, serverless)
- **AI-integrated:** Machine learning or AI components
- **Mixed:** Combination of above

**Waterfall Advantage:**
- Fixed-scope: +15 points
- Others: 0 points

**Agile Advantage:**
- Cloud-native: +20 points
- AI-integrated: +20 points
- Mixed: +10 points

**Rationale:** Cloud-native and AI projects benefit from Agile's iterative approach and continuous deployment. Fixed-scope projects benefit from Waterfall's upfront planning.

### 6. Timeline Pressure (1-10 scale)
- **1 = Flexible timeline** (e.g., internal tool, no deadline pressure)
- **10 = Extremely tight timeline** (e.g., market window, competitive pressure)

**Agile Advantage:** +timeline × 4 points (max +40)
- Agile delivers working software incrementally, enabling early value delivery
- Iterative approach allows prioritization of high-value features

**Waterfall Penalty:** -timeline × 1 point if timeline > 7 (max -30)
- Waterfall's upfront planning delays initial delivery
- Tight timelines conflict with comprehensive documentation phase

**Rationale:** Simulation showed Agile delivered working features after Sprint 1 (Week 8), while Waterfall had no working features until Week 7.

---

## Scoring Algorithm

### Step 1: Calculate Base Scores

```
Agile Score = 0
Agile Score += volatility × 7
Agile Score += (timeline × 4)
Agile Score += 20 if project_type in [Cloud-native, AI-integrated]
Agile Score += 10 if team_size in [Solo, Small]
Agile Score -= 15 if regulatory == High
Agile Score -= 10 if distribution == Remote

Waterfall Score = 0
Waterfall Score += (10 - volatility) × 7
Waterfall Score += 25 if regulatory == High
Waterfall Score += 15 if project_type == Fixed-scope
Waterfall Score += 10 if team_size == Large
Waterfall Score -= 10 if timeline > 7

Hybrid Score = (Agile Score + Waterfall Score) / 2 + 10
```

### Step 2: Cap Scores

```
Agile Score = min(100, max(0, Agile Score))
Waterfall Score = min(100, max(0, Waterfall Score))
Hybrid Score = min(100, max(0, Hybrid Score))
```

### Step 3: Determine Winner

```
Winner = methodology with highest score
Confidence = score_difference between winner and second place
  - High: difference >= 20
  - Medium: difference 10-19
  - Low: difference < 10
```

---

## Worked Example

### Scenario: Cloud-native startup with evolving requirements

**Inputs:**
- Requirements Volatility: 8/10 (highly volatile)
- Regulatory Intensity: None
- Team Size: Small (3 developers)
- Team Distribution: Co-located
- Project Type: Cloud-native
- Timeline Pressure: 9/10 (very tight)

**Calculation:**

```
Agile Score = 0
  + (8 × 7) = 56
  + (9 × 4) = 36
  + 20 (cloud-native) = 20
  + 10 (small team) = 10
  - 0 (no regulatory)
  - 0 (co-located)
  = 122 → capped at 100

Waterfall Score = 0
  + ((10 - 8) × 7) = 14
  + 0 (no regulatory)
  + 0 (not fixed-scope)
  + 0 (small team)
  - 10 (timeline > 7)
  = 4

Hybrid Score = (100 + 4) / 2 + 10 = 62
```

**Result:**
- **Recommendation: AGILE**
- **Confidence: High** (100 - 62 = 38 point difference)
- **Explanation:** High volatility (8/10) and cloud-native project type strongly favor Agile. Small co-located team enables effective iterative development. Tight timeline (9/10) benefits from Agile's incremental delivery approach.

---

## Interpretation Guide

### Agile Recommendation (Winner by 20+ points)
- **Best for:** Startups, innovation projects, cloud-native applications, evolving requirements
- **Key benefits:** Flexibility, early delivery, continuous feedback
- **Risks:** Requires strong team communication, may struggle with regulatory compliance

### Waterfall Recommendation (Winner by 20+ points)
- **Best for:** Fixed-scope projects, regulated industries, large distributed teams
- **Key benefits:** Predictability, comprehensive documentation, formal change control
- **Risks:** Inflexible to requirement changes, delayed delivery of working software

### Hybrid Recommendation (Winner or close second)
- **Best for:** Projects with mixed characteristics, moderate volatility, some regulatory requirements
- **Key benefits:** Combines Waterfall's planning with Agile's flexibility
- **Approach:** Use Waterfall for initial planning and architecture, Agile for iterative development

### Low Confidence Recommendation (< 10 point difference)
- **Interpretation:** Project characteristics don't strongly favor one methodology
- **Recommendation:** Consider hybrid approach or team preference
- **Action:** Consult with team and stakeholders on methodology choice

---

## Limitations and Caveats

1. **Single simulation basis:** Scoring is based on one controlled simulation of a small project. Real-world projects may have different characteristics.

2. **Simplified factors:** The tool uses 6 key factors but real projects may have additional considerations (e.g., organizational maturity, legacy system integration, DevOps capability).

3. **No team maturity factor:** The tool assumes teams are equally capable with both methodologies. In reality, organizational maturity with Agile practices significantly impacts success.

4. **No integration complexity:** The tool doesn't account for integration with existing systems, which may favor Waterfall's upfront planning.

5. **Hybrid not fully modeled:** The tool recommends hybrid but doesn't provide detailed guidance on hybrid implementation (e.g., Waterfall for planning, Agile for development).

---

## References

- Simulation findings: Waterfall vs Agile comparative analysis (2026)
- Standish CHAOS Report (2020-2025): Agile 42-50% success vs Waterfall 13-26%
- Digital.ai 18th State of Agile (2025): 74% hybrid adoption
- PMI Pulse of the Profession (2025): Hybrid methodologies growing