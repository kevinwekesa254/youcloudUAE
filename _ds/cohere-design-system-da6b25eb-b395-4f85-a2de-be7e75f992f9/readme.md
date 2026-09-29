# Cohere Design System

A recreation of Cohere's enterprise-AI brand system — austere black-and-white UI punctuated by tactile brand imagery, dark product bands, and editorial coral/blue accents. Built for generating well-branded Cohere interfaces, marketing surfaces, and prototypes.

> **Sources.** This system was authored from a written brand/design specification only — **no codebase or Figma file was attached**. All color, type, spacing, and component definitions come from that spec and from Cohere's publicly observable web presence. If you have the production codebase, Figma library, or proprietary font files, attach them and this system can be tightened to match exactly.

---

## Brand context

Cohere is an enterprise AI platform. Its products center on **Command** (models for agentic enterprise tasks), **Embed / Rerank** (retrieval), and **North** (a secure AI workspace). The web presence reads like a sober "AI command center with editorial restraint": a monumental typographic claim on white, then photography, dark product mockups, monochrome trust logos, and generous empty space that make AI infrastructure feel *controlled* rather than speculative.

Three surface tones recur:
- **Marketing** — white editorial canvases, huge display headlines, split hero compositions.
- **Product** — deep green-black (`#003c33`) and dark navy (`#071829`) full-width bands.
- **Editorial** (blog / research) — publishing-system clarity: large coral taxonomy chips, blue links, thin rules, dense rule-separated lists.

---

## Content fundamentals

How Cohere copy is written:

- **Voice:** confident, plain, enterprise-credible. It sells control, security, and grounding — not hype or AGI speculation. Claims are concrete ("Your data never leaves your control") rather than visionary.
- **Person:** addresses the reader as **you / your** ("inside your business", "your stack"); the company is **we / Cohere**. First person plural is used sparingly and only for commitments.
- **Casing:** sentence case nearly everywhere — headlines, buttons, nav. **Uppercase is reserved for mono category/system labels** (e.g. `RESEARCH`, `SECURITY FIRST`). Product names keep their capitalization (Command, North, Embed).
- **Headlines:** short, declarative, often a full claim — "Secure AI agents for the modern enterprise". One oversized headline per section, then restraint.
- **CTAs:** verb-led and specific — "Request a demo", "Explore products", "Read the security overview", "Read the docs". The single primary action is a pill; the companion is an underlined text link.
- **Length & rhythm:** lead paragraphs run ~1–2 sentences at 18px; supporting copy at 16px. Editorial titles can be longer and descriptive.
- **Emoji:** none. The brand does not use emoji in UI or marketing. Do not introduce them.
- **Numbers/metrics:** used only when real and load-bearing (context window, languages, SOC 2). Avoid invented stats and "data slop".
- **Vibe:** research-lab cadence — measured, technical, trustworthy. Slightly austere; never playful or salesy.

---

## Visual foundations

**Color.** White (`#ffffff`) is the default canvas. Color does **not** come from decorative UI fills — it arrives through (a) dark product bands (deep green `#003c33`, navy `#071829`, near-black `#17171c`), (b) photography and abstract 3D media, (c) editorial accents (coral `#ff7759` taxonomy chips, action-blue `#1863dc` links). Warm neutrals (stone `#eeece7`) and pale washes (`#edfce9`, `#f1f5ff`) carry quiet section blocks. Never turn coral or blue into broad surface colors.

**Type.** A display/body/mono split: **CohereText** (→ Space Grotesk) for monumental headlines, **Unica77** (→ Hanken Grotesk) for body/UI, **CohereMono** (→ Space Mono) for uppercase technical labels. Display is huge, tight, near-monospaced in spirit, with negative tracking (96px / -1.92px at hero). Weights stay light — **400 for display and most headings, 500 max for UI**; size, spacing, and surface contrast do the hierarchy work, not bold weight. Body settles into restrained 16–24px.

**Spacing & layout.** 8px base with documented one-offs (2, 6, 10, 22, …). Dramatic vertical breathing room between bands (80px section rhythm); dense layout only where IA demands it (research rows, blog grids, forms). Three-zone nav (logo / centered menu / actions). Hero is centered text above a two-card media composition. Feature grids are 3-up on desktop, collapsing 3→2→1.

**Backgrounds.** Flat fields, not textures or patterns. No repeating motifs, no hand-drawn illustration backgrounds. **Gradients are media-led only** — reserved for large hero/CTA media panels and abstract 3D renders, never as normal UI fills. Imagery skews warm-to-deep (coral → navy/green) and is always presented as a rounded card with visible corners, not a full-bleed text backdrop (except deliberate CTA bands).

**Elevation & depth.** Mostly flat. Depth comes from **surface alternation, media contrast, rounded corners, and thin 1px borders** (`#d9d9dd` / `#e5e7eb`, or `rgba(255,255,255,0.14)` on dark) — **not drop shadows**. Reserve soft shadows for floating UI only (dialogs, menus). Cards never carry a drop shadow.

**Corner radii.** Rounded but not cute. Major media cards: **22px**. Cards/chips: **8px**. Medium product blocks: 16px. Pill CTAs: **32px**. Filter/topic pills: 30px. Never round major media below 8px.

**Cards.** Flat surface + optional hairline border + generous padding. Warm "stone" product cards use 8px radius, a divider line, and checkmark bullet rows. Signature media cards use 22px and contain a mockup or abstract render.

**Animation.** Quiet. Short opacity/color transitions (~0.15s ease) for hover; no bounces, no decorative infinite loops, no parallax gimmicks. Motion serves clarity, not spectacle.

**Hover / press states.** Hover = subtle **opacity reduction** (~0.82) on pill CTAs, or a rule/underline shift on text links and nav. Active filters invert (fill flips to near-black or coral). No scale/shrink press effects.

**Borders & rules.** Thin hairlines separate research rows and contain forms. Lists are rule-driven, not boxed. Trust logos have no borders at all — wide spacing only.

**Transparency & blur.** Used sparingly: a translucent blurred nav bar (`backdrop-filter: blur`), and `rgba(255,255,255,0.06–0.14)` translucent cards/borders inside dark product bands. Not a general aesthetic.

---

## Iconography

- **System:** Cohere uses custom thin-line geometric illustrations and a proprietary icon font, paired with abstract 3D media. The interface itself is sparse on icons — text links and pills do most of the work.
- **Substitution (flagged):** the proprietary icon font/illustrations are **not bundled** (no codebase/Figma supplied). For implementation, use a **thin-line geometric** icon set as the nearest match — **[Lucide](https://lucide.dev)** (consistent 1.5–2px stroke, geometric, no fills) loaded from CDN: `<script src="https://unpkg.com/lucide@latest"></script>` then `lucide.createIcons()`, or the `lucide-react` package in React. Keep stroke weight light to match Cohere's thin-line feel. **Replace with the real icon font when available.**
- **In this system:** the few glyphs used (checkmarks, arrows, status dots, close ✕) are simple Unicode / CSS shapes rather than a heavy icon set, matching the restrained UI. Status is shown with small colored dots, not iconography.
- **Emoji:** never. Not part of the brand.
- **Logo:** `assets/cohere-logo.svg` (ink wordmark) and `assets/cohere-logo-white.svg` (reversed). These are **text wordmark placeholders** in the substitute display font — swap for the official logo files in production.

---

## Index / manifest

**Root**
- `styles.css` — global entry point; `@import`s every token + font file. Consumers link this one file.
- `tokens/` — `fonts.css`, `colors.css`, `typography.css`, `spacing.css`, `radius.css`, `elevation.css`.
- `assets/` — `cohere-logo.svg`, `cohere-logo-white.svg`.
- `readme.md` — this guide. `SKILL.md` — portable Agent Skill wrapper.

**Components** (`components/<group>/` — React primitives, namespace `window.CohereDesignSystem_da6b25`)
- `actions/Button` — pill CTA system: `primary` (filled) · `secondary` (underlined link) · `outline` (taxonomy pill); `light`/`dark` tones; sm/md/lg.
- `data-display/Chip` — oversized coral blog taxonomy chip.
- `data-display/MonoLabel` — uppercase mono technical label.
- `data-display/Badge` — small status / integration chip.
- `forms/Input` — labeled rectangular text field, violet focus, error/hint.
- `surfaces/Card` — flat surface container (white / warm / green / navy / dark).
- `surfaces/ProductCard` — warm stone product/model summary with checkmark bullets.
- `marketing/AnnouncementBar` — full-width black announcement strip.
- `marketing/TrustLogoStrip` — quiet monochrome customer-logo strip.

**Foundations** (`foundations/` — Design System tab specimen cards)
- Colors: Brand & Accent · Surfaces · Text/Rules/Semantic.
- Type: Display · Body/UI · Mono Labels.
- Spacing: Spacing Scale · Radius Scale.
- Brand: Logo · Elevation & Depth.

**UI kits** (`ui_kits/`)
- `website/` — interactive Cohere.com recreation: announcement bar, three-zone nav, home (hero + agent-console mockup + trust strip + dark security band + product cards + contact form), blog index (coral taxonomy + post grid), research index (topic pills + rule-separated paper list), dark footer with newsletter. Entry: `ui_kits/website/index.html`.

---

## Do's & Don'ts

**Do** — white canvas default; dark green/navy for product bands; near-black pill CTAs; 22px radius on major media; coral for editorial taxonomy only; monochrome trust logos with wide spacing; thin-line icons; let photography/mockups carry color while the shell stays restrained.

**Don't** — turn coral/blue into broad surface fills; add drop shadows to cards; make every section a card (use rules + open space); round major media below 8px; collapse the display/body/mono split into one generic sans; use saturated gradients as normal UI backgrounds; use emoji.

## Known gaps / substitutions

- **Fonts:** proprietary CohereText / Unica77 / CohereMono not bundled → substituted with Space Grotesk / Hanken Grotesk / Space Mono via Google Fonts (`tokens/fonts.css`). Flag and replace with real files.
- **Icons:** proprietary icon font not bundled → use Lucide (thin-line) as nearest match.
- **Logo:** wordmark recreated as text in the substitute font, not the official mark.
- **No codebase/Figma** was provided; components are faithful to the written spec but not pixel-verified against production source.
