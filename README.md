# MB Claude Skills

Free Claude skills for the Maurice Blackburn marketing team: brand reference, brand-vs-competitor comparison, on-brand social content creation, and SEO/GEO work, ready to use in any Claude conversation. One plugin, **mb-marketing**, 11 skills.

## What are Skills?

Skills are markdown files that give Claude specialised knowledge and a workflow for a specific task. Once installed, Claude recognises when you're doing brand, social, or SEO/GEO work for MB and applies the right MB-specific frameworks, voice, and compliance rules automatically, without you having to explain them each time.

## How Skills Work Together

Skills reference each other and build on shared context, rather than working in isolation. `brand-mb` is the foundation of the whole marketing ecosystem, every other skill checks it first to understand MB's positioning, audience, and voice before doing anything.

```
                                 brand-mb
                (read by every other skill first: MB's
             positioning, audience, voice, and practice areas)
                                     |
              ________________________________________________
             |              |               |                 |
             v              v               v                 v
        Brand & Social    SEO Content   SEO Research      SEO Technical
        --------------    -----------   -----------       -------------
        brand-analyst-mb  seo-content-mb  seo-gap-mb       seo-audit-mb
        post-writer-mb                    seo-competitor-mb
        post-grader-mb                    seo-backlinks-mb
        viral-hooks-mb
        repurpose-mb
```

Skills cross-reference each other:
```
  post-writer-mb     -> viral-hooks-mb (hook)   -> post-grader-mb (grade)
  repurpose-mb       -> viral-hooks-mb (hook)   -> post-grader-mb (grade)
  brand-analyst-mb   -> brand-mb (MB's own side, before researching a competitor)
  seo-competitor-mb  -> seo-gap-mb (feeds the opportunity list)
  seo-gap-mb         -> seo-content-mb (hands off the brief)
  seo-content-mb    <-> seo-audit-mb (writes the schema; validates it after publish)
```

See each skill's own "When NOT to Use" and cross-link notes in its SKILL.md for the full dependency map.

## Install (claude.ai / Cowork)

1. Open **Extensions** → **Browse extensions**.
2. Go to the **Plugins** tab.
3. Click **Add GitHub**.
4. Paste `ttjahjadi-mb/mb-claude-skills` into the URL field and click **Sync**.
5. Find **Maurice Blackburn Marketing Skills** in the list and install/enable it, one plugin, all 11 skills included.

That's it, no downloading, no manual file uploads. Installing only pulls the repo's current state at that moment, it does **not** auto-update later. When the brand tokens, tone of voice, or skill logic change here, remove the plugin (⋮ menu → Remove) and re-add it via the same steps to pick up the latest version.

## Install (Claude Code)

```
/plugin marketplace add ttjahjadi-mb/mb-claude-skills
/plugin install mb-marketing@mb-claude-skills
```

Then just mention brand, social-content, or SEO/GEO work in conversation, the skills trigger automatically when relevant. `/plugin update` refreshes it later.

## What's inside

**Brand and social:**

| Skill | When it kicks in |
| --- | --- |
| `brand-mb` | Building anything MB-branded (site component, deck, dashboard, document) that needs exact colours/fonts/logo, or writing content that needs to sound like MB rather than a generic assistant |
| `brand-analyst-mb` | Asking "how does our brand compare to [competitor]" — a quick, conversational brand-vs-competitor read |
| `post-writer-mb` | "Write me a post about X for [platform]" — produces a hook + body + CTA, on-brand, compliance-checked, and graded before you see it |
| `post-grader-mb` | "Is this post compliant/any good?" — scores a draft and lists the top 3 fixes; checks legal-marketing compliance as a hard pass/fail gate before anything else |
| `viral-hooks-mb` | Needs a strong opening line — a curated hook library filtered for a law firm's voice and compliance obligations (no fake urgency, no fabricated confessions) |
| `repurpose-mb` | "Turn this case update into a week of content" — one long input becomes a batch of platform-native posts across LinkedIn, Instagram, TikTok, and Meta |

**SEO and GEO:**

| Skill | When it kicks in |
| --- | --- |
| `seo-audit-mb` | "Audit this page/site for SEO": full technical + structured-data audit: crawlability, canonicals, hreflang, redirects, Core Web Vitals, AI-crawler access, JSON-LD validation |
| `seo-content-mb` | "Write an SEO page for X" / "make this GEO-ready": writes a page in MB's real brand voice (`brand-mb`) to rank AND be cited by AI answer engines, with a full SEO brief, a YMYL/E-E-A-T read, a compliance gate, and delivery as HTML, a schema file, and two copywriter-ready docs |
| `seo-gap-mb` | "Where are our SEO gaps" / "why does ChatGPT cite a competitor and not us": keyword, topic, and AI-citation gap analysis, ranked into a briefable opportunity list |
| `seo-competitor-mb` | "How do we compare to [competitor] on search": keyword gap, Share of Voice, and Share of Model (AI-answer visibility) benchmarking |
| `seo-backlinks-mb` | "Audit our backlinks" / "find link-building targets": backlink health, toxic-link flagging (disavow always held for human sign-off), and a competitor link-gap outreach list |

All 11 skills ship in the one **mb-marketing** plugin. `post-writer-mb`, `post-grader-mb`, `viral-hooks-mb`, and `repurpose-mb` all read `brand-mb`'s tone-of-voice, brand guidelines, and a shared legal-marketing guardrails file, bundled together so that dependency is never an issue. The SEO/GEO skills are built for a law firm's SEO/GEO work specifically: named competitor benchmarking, YMYL E-E-A-T weighting, and a legal-marketing compliance gate on anything `seo-content-mb` writes or recommends. Some SEO/GEO capabilities (keyword volume, backlink data, AI-answer share of voice) need a live SEMrush/BrightEdge/Profound/DataForSEO connector or a pasted CSV export; each skill states plainly which parts it can automate on the spot versus which need that data supplied.

## Try it — example prompts

**brand-mb** (triggers automatically, no need to ask for it by name):

- "Build me a one-pager in our brand colours for the new claims process."
- "Draft an EDM about the Dr Simon Gordon gynaecological investigation." — writes in the Courageous Ally voice, uses the real case history.
- "Write social copy for a class action update." — applies the audience split (familiar vs. not familiar with the law), uses the person's name instead of "our client"/"the plaintiff."
- "What's MB's brand personality?"
- "When was MB founded?" — sourced facts, not a guess.

**brand-analyst-mb** (ask for a brand comparison directly):

- "How does our brand compare to Slater and Gordon?" — live research on their site/positioning, scored against MB's documented voice/colours.
- "What's Shine Lawyers doing differently on their homepage?"

Good live demo: pick a real competitor name in the room and run `brand-analyst-mb` on the spot — it researches fresh each time rather than relying on memory of what a firm's brand used to look like.

**Social content skills** (post-writer-mb, post-grader-mb, viral-hooks-mb, repurpose-mb):

- "Write me a LinkedIn post about the Dr Simon Gordon investigation."
- "Give me a hook for a post about workplace injury claims."
- "Is this post compliant?" (paste a draft) — checks for outcome guarantees, misleading claims, and consent issues before it even scores the writing.
- "Turn this case update into posts for our channels." — produces a batch across LinkedIn, Instagram, TikTok, and Meta.

Compliance is a hard gate on every one of these — a post that scores well but makes an outcome guarantee or skips a required trigger warning will not be returned as-is. MB's house style permits the em dash and these skills apply it by default; the only thing they'll ask you to confirm is the CTA (Free claim check, Ask Morry AI, Chat with Morry AI, Request a callback, or Get in touch).

**SEO and GEO skills** (seo-audit-mb, seo-content-mb, seo-gap-mb, seo-competitor-mb, seo-backlinks-mb):

- "Run a technical SEO audit on our TPD claims page."
- "Write an SEO and GEO optimised page about workers compensation claims in Victoria." Full SEO brief + page draft, delivered as HTML, a schema file, and two copywriter-ready docs.
- "What SEO gaps do we have against Shine Lawyers on road injury content?"
- "How does our Share of Voice compare to Slater and Gordon?"
- "Audit our backlink profile and flag anything toxic."

Same rule as the rest: mention the right thing and the right skill triggers, no need to name it. Every skill will ask plainly whether SEMrush, BrightEdge, Profound, or a GSC export is available before falling back to an estimated read, so answer for all of them, not just the first one you think of.

## What's *not* in this public repo

Two things are deliberately left out of `brand-mb` here, both for licensing/sensitivity reasons:

- **Reader Pro**, MB's licensed display font — not ours to redistribute publicly. Headings fall back to a serif system font instead. If you're working from inside MB's internal Claude workspace, the full font files are bundled there.
- **The internal "Brand guidelines" writing-guide PDF** — the source document behind `tone-of-voice.md`. The distilled summary in this skill is safe to share publicly; the original internal PDF isn't.

Everything else (colours, type scale, logo, the full tone-of-voice and brand-history summaries) is complete and accurate here.
