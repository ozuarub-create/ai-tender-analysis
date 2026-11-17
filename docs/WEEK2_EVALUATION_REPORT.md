# Week 2 Evaluation Report

The benchmark contains 90 labeled requirement-bid pairs: 30 tender requirements across three bidders. The evaluation reports exact status agreement, per-status accuracy, and a five-class confusion matrix.

The supplied deterministic benchmark is designed to exercise paraphrases, contradictory statements, omissions, exclusions, delivery deviations, warranty gaps, alternative proposals, and scope-based not-applicable decisions.

Acceptance checks include:
- exact status agreement >= 85%
- zero mandatory requirements marked met without supporting evidence
- all seeded exclusions surfaced
- all seeded contradictions surfaced
- missing responses classified as not evidenced
- each clarification linked to bidder and requirement ID
