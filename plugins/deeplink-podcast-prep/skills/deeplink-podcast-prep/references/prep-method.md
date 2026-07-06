# Prep method — help the guest answer, and cite the back-catalog

The runtime core. The host has already written the questions; **do not invent question blocks.**
Goal: from the host's prepared doc, produce a brief where each question has (a) the substance to
answer it well, (b) callbacks to earlier Deeplink episodes that covered the topic, and (c) a
soundbite — matched to who the guest actually is.

## 1. Read the guest + questions out of the doc

The doc gives you most of what you need before any research:
- **Guest identity** — the intro names the guest, their role, and their company/field.
- **Umbrella themes** — the episode's framing lines.
- **The questions** — take them as given. Note the **concrete hooks** each embeds (a funding round,
  a customer, a stat, a personal story) — each hook is a fact to verify.
- **Block arc & time budgets** — see `deeplink-show.md`.

Write down: guest name, role, company/domain; the list of questions; and every factual claim the
questions assume (the things to verify).

## 2. Match each question to the episode map (the show's memory)

For every question, scan `references/episode-map.md` for episodes that touched the same topic — use
the per-episode **Keywords** and **Probíraná témata**, and the **topic index** at the top of the map.
This is the skill's signature move: it lets the guest say on air "to jste v pořadu už řešili v díle
9, když jste se bavili o…", tying their answer into the show's back-catalog.

For each match, capture: the **díl number**, the **one-line angle** it was discussed from, and
(optionally) a memorable moment from that episode. Prefer 1–2 strong, genuinely-related callbacks
over a long weak list. If nothing in the catalog fits a question, that's fine — no callback.

## 3. Offer to use a knowledge base (with consent)

The guest often has richer, first-hand material in a **personal or company knowledge base** — Notion,
Obsidian, Confluence, Google Drive, an internal wiki, a docs/notes folder, or a connected KB/MCP
tool. This is the fastest path to accurate, specific answers, but it is private data and needs the
user's go-ahead before you touch it.

Two cases:
- **A KB is already known** — you can see a connected KB/MCP tool (Notion, Confluence, Drive, company
  wiki, docs search…), or the user named one earlier in the conversation. **Do not ask open-endedly.**
  Tell the user exactly which KB you detected and that you plan to use it, and **ask for approval
  before reading from it.** E.g. "Vidím připojený Notion — můžu z něj čerpat pro přípravu? (a/n)".
- **No KB is known** — ask once whether they have a personal or company knowledge base you could draw
  more from, and how to reach it (which tool / which space / a link or path).

Rules:
- **Never read a KB without explicit approval.** If the user declines or doesn't answer, proceed with
  public sources only — don't block.
- **Confidentiality still applies** (see Guardrails): a KB may hold unpublished or sensitive material.
  Use it to make the guest's answers accurate, but don't put confidential KB details into public
  soundbites without the guest's ok.
- Note in the brief which claims came from the KB, so the guest knows what's internal.

## 4. Research the guest live

Because the guest differs each episode, this can't be pre-baked. Gather:
1. **The guest & their company** — company site, the guest's own site/LinkedIn, prior talks or
   interviews (also to catch how they phrase things → their voice), recent news.
2. **Each embedded hook** — verify the specific numbers/events the questions cite; note the exact
   figure and date from an authoritative source.
3. **Domain background** for substantive answers, plus any named external stat traced to its primary
   source and correct wording.

Tools: WebSearch / WebFetch first; the approved KB (§3) and connected MCP knowledge tools for depth.
If a source needs a login that isn't set up, skip it and note the gap — never block on it.

## 5. Write the prep per question

For each question, in the podcast's language (Czech for Deeplink):
- **Talking points** — 3–5 bullets: the substance of a good answer, specific to this guest.
- **Facts & numbers** — only VERIFIED figures, each with its source. Mark anything unconfirmed as
  "ověřit" rather than stating it as fact.
- **Už zaznělo v pořadu** — the episode callback(s) from step 2: "→ díl {N} ({téma}) — {jedna věta}".
  Omit if there's no genuine match.
- **Soundbite** — one punchy sentence the guest could actually say, in their register (grounded,
  plain language, no hype). Match their voice if you have samples; otherwise write a strong natural
  line and flag it as a suggestion to make their own.
- **Pozor na** (optional) — a phrasing to avoid, a sensitive area, or a claim to hedge.

Personal / block-0 questions (a trip, a hobby): you usually can't research these — scaffold an angle
and mark "doplnit vlastními detaily" instead of inventing specifics.

## 6. Output — one HTML brief (see SKILL.md "Output & delivery")

One self-contained HTML page: header with episode + guest; one section per block; one card per
question (question → talking points → facts → **už zaznělo v pořadu** → soundbite → optional
"pozor na"). Deliver it as a **hosted Artifact** or from a **local web server** — offer both and let
the user choose whichever lets them review it best; fall back to the other if one isn't available.

## Guardrails

- **Never invent facts, numbers, quotes, or personal details** — nor an episode callback. A callback
  must point to a real episode in `episode-map.md` that genuinely covered the topic; if unsure, leave
  it out. Verify or mark "ověřit" / "doplnit". A wrong number said on air is worse than a gap.
- **Get external stats exactly right** — correct source, year, and wording; note where uncertain.
- **Confidentiality** — the podcast is public. Don't surface unpublished/sensitive info about the
  guest or their customers.
- **Standalone** — rely only on live/public sources and bundled references, never on files that exist
  on one person's machine. The skill must run the same in any environment where it is installed.
