---
name: viral-hooks-mb
description: A curated library of proven hook frameworks, filtered for a plaintiff law firm's voice and compliance obligations. Picks the strongest hook pattern for a given topic and platform, fills it in with real MB specifics, generates variations, and runs the first-3-words test. Triggers on "give me a hook for X," "write hook options," "my intro is boring," or any request for an opening line. Auto-invoked by post-writer-mb and repurpose-mb to open every draft with a tested hook instead of a generic AI intro.
argument-hint: "[topic] [platform]"
allowed-tools: Read, Write, Edit, Glob, AskUserQuestion
---

# Viral Hooks (MB)

Adapted from a general-purpose 100-hook library, curated down for Maurice Blackburn: an Australian plaintiff law firm. Not every proven consumer-brand hook pattern belongs here — some create legal or reputational risk (false urgency toward vulnerable claimants, fabricated personal confessions, "insider secret" framing that implies special access). This skill keeps the categories that work for legal marketing and drops the rest. See `brand-mb/reference/legal-marketing-guardrails.md` for the compliance rules every hook must still pass.

## When to Activate

- "Give me a hook for [topic]"
- "Write hook options for my [platform] post"
- "My opening line is weak — fix it"
- Any time `post-writer-mb` or `repurpose-mb` needs to open a post or video script.

## Workflow

### Step 1: Get the topic and the angle

You need the topic and the angle: a strong result/number, an investigation, a common misunderstanding, a client story (consent-gated), or a practical "how to check eligibility" angle. If missing, ask — don't invent one.

### Step 2: Pick a category

| Angle | Best category |
|---|---|
| A result, number, or case statistic | The Receipt |
| An active investigation or "were you affected" callout | Audience Callout / Investigation |
| A common misunderstanding about the law or process | Negative Frame / Mistake Callout |
| An unanswered question | Curiosity Gap |
| A how-to or eligibility checklist | Listicle / Speed |
| A client outcome (consent on file) | Transformation / Story |
| A question that makes the reader stop | Question Hook |

When in doubt, prefer **The Receipt** or **Audience Callout / Investigation** — highest fit for MB's actual content (case results, class action/investigation call-outs like "Were you treated by Dr X?").

### Step 3: Fill in 2-3 variations

Fill placeholders with real specifics — a real number, a real matter name, a real firm/practitioner name already public in an active investigation. Generic fills kill the hook, but so does an unverified specific — never invent a number, name, or statistic. If a fact isn't confirmed, say so and use a safe generic instead ("a number of former patients" not an invented count).

### Step 4: Run the first-3-words test + compliance check

Read the first 3 words alone — do they create curiosity, surprise, or emotional pull without overpromising? Then check every variation against `brand-mb/reference/legal-marketing-guardrails.md` — no outcome guarantees, no absolute legal claims, trigger warning if the subject matter is distressing.

### Step 5: Return the best one

Return the strongest variation, name the category, offer 1-2 alternates.

## The Hook Library (curated categories)

### 1. The Receipt (proof, numbers, results)

1. [N] [people/clients] have come forward about [matter]. Here's what we're seeing.
2. We reviewed [N] cases like this. Here's what most people don't know.
3. Here's what happened when we investigated [matter].

> Example: "We've heard from over 200 people about this. Here's what they have in common."

### 2. Audience Callout / Investigation

The pattern behind MB's real "Were you treated by Dr X?" EDM — names the exact affected group and states an active investigation plainly.

4. Were you treated by [practitioner/company]?
5. If you [experienced X] at [place], this may affect you.
6. An investigation is underway into [matter]. Here's what it means for you.

> Example: "Were you treated by Dr Simon Gordon?"

### 3. Negative Frame / Mistake Callout

7. Don't sign [document] before you read this.
8. Here's the mistake most people make with [process].
9. [N] things to check before you [common action].

> Example: "Don't accept a settlement offer before you read this."

### 4. Curiosity Gap

10. Here's what most people don't know about [process/right].
11. Here's what changed in [area of law] that affects [group].

> Example: "Here's what most people don't know about their rights after a workplace injury."

### 5. Listicle / Speed / Eligibility Check

12. [N] signs you might have a claim.
13. Check your eligibility in [N] minutes.
14. [N] questions to ask before choosing a lawyer.

> Example: "3 signs you might have a claim you don't know about."

### 6. Question Hook

15. Have you ever wondered if you're entitled to compensation for [situation]?
16. What would you do if [situation] happened to you?

> Example: "What would you do if your employer ignored a safety complaint?"

### 7. Transformation / Story (consent-gated — real name only with consent on file)

17. Here's how we helped [client/description] get [outcome — worded without overpromising a typical result].
18. [Client/description]'s situation seemed [adjective]. Here's what happened next.

> Example: "Sarah thought nothing could be done about her case. Here's what changed."

## Categories deliberately dropped (do not use for MB)

- **Confession / Vulnerable** ("I almost shut down my business...") — fabricating personal vulnerability doesn't fit an institutional legal voice.
- **Urgency / FOMO** ("Don't scroll past this...") — pressuring people who may be vulnerable claimants toward a decision is a real risk, not just a style mismatch.
- **Stolen Lessons** ("I copied [competitor]...") — doesn't fit a law firm's voice or positioning.
- **Secret / Insider** ("Here's the secret they don't want you to know") — implies special/gated access in a way that can read as misleading for a regulated profession.

## Hook-Writing Rules

- **Specific beats abstract, but only if the specific is real.** Never invent a number, name, or statistic to make a hook stronger.
- **First word is the strongest word.** Cut "so," "okay," "today I want to talk about."
- **No filler.** Cut "really," "very," "just," "actually," "basically."
- **No generic AI openers.** Never "In today's fast-paced world," "Let me tell you," "Are you ready to."
- **Run every hook past the compliance guardrails before returning it** — this is not optional, even for a "just a hook" request.

## What NOT to Do

- Don't return a hook with placeholders left unfilled.
- Don't dump the whole library on the user. Return 1 strong hook plus 1-2 alternates.
- Don't use a dropped category even if it would score well on generic virality metrics — compliance and voice fit override virality ceiling here.
- Don't invent facts to make a hook land. If the real material is thin, say so rather than fabricating specifics.
