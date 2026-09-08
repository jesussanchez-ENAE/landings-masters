---
target: enae-executive-mba-directivos.html
total_score: 17
max_score: 36
na_heuristics: 7
p0_count: 2
p1_count: 2
target_identity: "file:/Users/jesus/Documents/GitHub/landings-masters/enae-executive-mba-directivos.html"
target_fingerprint: "sha256:b2637395ecdcccd186291c7b7b85f91377416f336d2a3ef2e4c24ad2f649c1b3"
target_path: /Users/jesus/Documents/GitHub/landings-masters/enae-executive-mba-directivos.html
timestamp: 2026-09-08T07-51-25Z
slug: enae-executive-mba-directivos-html
---
## Critique: ENAE Executive MBA para Directivos

**Method: dual-agent (A: design-review · B: detector-browser)**
**Target:** `enae-executive-mba-directivos.html` · Mode: **Persuade**

### Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | Reveal animations provide scroll feedback, but form has zero submit/loading/success state |
| 2 | Match System / Real World | 3 | Language fits director audience well; iconography (numerals, generic checkmarks) doesn't |
| 3 | User Control and Freedom | 3 | Simple single-page flow, no traps |
| 4 | Consistency and Standards | 1 | Two competing visual systems |
| 5 | Error Prevention | 2 | HTML5 required/type validation present, no inline guidance |
| 6 | Recognition Rather Than Recall | 2 | Numeral-icons and uncaptioned testimonial video |
| 7 | Flexibility and Efficiency | n/a | Single-purpose landing page |
| 8 | Aesthetic and Minimalist Design | 2 | Base system minimalist; override layer adds noise |
| 9 | Error Recovery | 1 | Form action="#" — submits nowhere |
| 10 | Help and Documentation | 1 | FAQ styled but absent from page |
| **Total** | | **17/36** | **Poor (47%)** |

### Design Specificity Verdict

Category-interchangeable, not ENAE-authored. The file contains an entire unused editorial design system (lines 1-712) with distinctive choices. None of it renders. What ships is the generic override layer.

Deterministic scan: 31 findings — 13 low-contrast, 7 undersized-ui-text, 7 cramped-padding, 2 gpt-thin-border-wide-shadow (slop), 1 all-caps-body, 1 clipped-overflow-container.

### Overall Impression

Split personality: distinctive editorial system underneath, generic SaaS template on top. Looks like an AI-generated landing template with ENAE's colors pasted in. The biggest opportunity: activate the editorial system that's already written.

### What's Working

1. Underlying editorial design system is genuinely distinctive (OggText/SFUIDisplay, tabular-nums KPIs, dashed rules, skewed patterns)
2. Real proof points (QS rankings, Forbes, alumni videos, physical address)
3. Clean scroll-reveal implementation (IntersectionObserver with unobserve)

### Priority Issues

[P0] Form submits nowhere — action="#", entire conversion goal is dead
[P0] Two colliding design systems — sharp/editorial base vs rounded/shadowed override, different radii/shadows/blacks
[P1] AI-startup hero motif — neural sphere + orbiting buzzwords = SaaS cliche, not 35-year-old business school
[P1] Repetitive "not X, but Y" headline formula — same rhetorical move 5-6 times = AI copywriting tic
[P2] Missing objection-handling content — FAQ, faculty, curriculum detail all styled but absent

### Persona Red Flags

Jordan (First-Timer): Misreads ENAE as AI company from hero. No price/schedule info. Form does nothing.
Riley (Stress-Tester): Form dead end. Random uncaptioned video. No faculty/curriculum/process info.
Casey (Mobile): Heavy animated hero, 10px orbit pills, rAF loop drains battery, button overflows 46px.

### Minor Observations

- Redundant tokens (--enae-rojo = --enae-granate)
- Two different "blacks" (#202221 vs #2D2D2D)
- Hero photo at 90% black overlay barely visible
- Checkmark SVG duplicated 4x inline instead of symbol/use
- Watermark SVGs at 3-5% opacity invisible on most monitors
- Float keyframes run on mobile where pills stack and overlap
