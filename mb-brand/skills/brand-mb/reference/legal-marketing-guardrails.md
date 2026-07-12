# Legal Marketing Guardrails

Source of truth for the compliance rules and channel list used by `post-writer-mb`, `post-grader-mb`, `viral-hooks-mb`, and `repurpose-mb`. MB is a plaintiff law firm — social content that would be fine for a generic small business can be misleading, insensitive, or non-compliant here. These skills embed this checklist directly (self-contained, no runtime cross-skill file read); this file is the single place to update it when the rules change.

## Compliance guardrails (hard gate — a failure here blocks shipping, regardless of any quality score)

- **No outcome guarantees.** Never "you will win," "guaranteed compensation," "we always get results." Claims must not promise a specific legal outcome.
- **No misleading comparative claims.** Don't imply a typical or average result from a single case or a cherry-picked number.
- **Trigger/content warning required** for sexual abuse, suicide, or similarly distressing subject matter — this is an existing MB house rule (see `tone-of-voice.md`), not new. Lead with something steady, not a distressing opening line.
- **Real person's name only where consent is on file.** If consent status is unknown, flag it and default to "a client" or an anonymised description rather than assuming a name is clear to use.
- **No absolute claims about the law** ("always," "never") without a hedge — laws and case outcomes vary by jurisdiction and circumstance.

## Confirmed MB social channels

LinkedIn, Instagram, TikTok, Meta (Facebook). These are the only 4 channels these skills should default to — don't ask which platform each time; ask which of these 4 (or all 4) the post is for.

## Change log

- 2026-07-12: Created alongside the `post-writer-mb` / `post-grader-mb` / `viral-hooks-mb` / `repurpose-mb` skill set, adapted from Blotato's public `blotato-skills` content-creation skills.
