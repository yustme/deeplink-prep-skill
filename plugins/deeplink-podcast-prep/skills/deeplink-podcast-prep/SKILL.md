---
name: deeplink-podcast-prep
description: Prepare a guest to answer well on the Deeplink Show podcast. The host sends the guest a prepared question doc (usually a Notion link); give that link (or paste it) and the skill helps the guest answer each question — substance to answer well, plus callbacks to which earlier Deeplink episodes already covered that topic ("this you discussed in episode 9, when you talked about…"), drawn from a bundled map of all past episodes. It presents the prep as an interactive HTML page the guest can review comfortably — offered either as a hosted Artifact or served from a local web server. Use when the user says "připrav mě na Deeplink / na podcast", "podklady na rozhovor", "mám link na otázky na podcast", "podcast prep", or pastes/links a Deeplink question doc.
---

# Deeplink Podcast Prep

## Overview

The host has already prepared the questions (in the Notion doc) — **the skill does NOT invent
question blocks.** Its job is to help the **guest answer well**: for each question, give the
substance to answer it, and point to **which earlier Deeplink episodes already covered that topic**
so the guest can reference the show's back-catalog on air ("to jste, Filipe, probírali v díle 9,
když jste se bavili o…"). The brief is an interactive HTML page, delivered either as a hosted
**Artifact** or from a **local web server** — whichever lets the guest review it best.

Two knowledge sources feed each answer:
1. **The bundled episode map** (`references/episode-map.md`) — a distilled map of every past Deeplink
   episode: topics, guests, memorable moments. This is what powers the episode callbacks and is why
   the skill is **standalone** (the map is baked in; no local transcripts needed at runtime).
2. **Live research on the guest** — because the guest differs each episode, gather their background
   and verify the facts the questions reference (see `prep-method.md`).

## References

Read these as needed:
- `references/prep-method.md` — **the runtime playbook**: read the guest + questions out of the doc,
  match each topic to the episode map, research the guest live, write the answer prep, guardrails.
  Start here.
- `references/episode-map.md` — **the show's back-catalog**: per-episode topics/guests + a topic→
  episode index. Use it to find where a topic was previously discussed.
- `references/deeplink-show.md` — the show's format, block arc, timing, and a short illustrative
  (fictional) question doc so the prep matches how an episode actually runs.

## Workflow

1. **Get the questions.** From a pasted list, or fetch the URL (Notion, Doc). Try WebFetch first;
   if the page is private and returns an empty shell, use browser tools (`mcp__claude-in-chrome__*`)
   to read the logged-in page if available; otherwise ask the user to paste the questions.
2. **Read the guest + questions out of the doc** — the guest's name, role, field; and every question
   with the factual hooks it embeds (funding, scale, stats, personal stories). See `prep-method.md` §1.
3. **Match each question to the episode map** — find topics in `references/episode-map.md` that the
   question touches, so the prep can cite where the show covered it before. See `prep-method.md` §2.
4. **Offer to use a knowledge base** — the guest may have a personal or company KB with richer,
   first-hand material. See `prep-method.md` §3:
   - **If a KB is already known** (a connected KB/MCP tool — Notion, Confluence, Drive, company wiki —
     or one the user named earlier): don't ask open-endedly. Tell the user which KB you'll use and
     **ask for approval before reading it**.
   - **If none is known:** ask the user whether they have a personal/company knowledge base to draw
     more from, and how to reach it. Never access a KB without the user's go-ahead.
5. **Research the guest live** — background and voice, and verify every number the questions reference
   against an authoritative source. WebSearch/WebFetch, any approved KB, + connected MCP tools;
   degrade gracefully.
6. **Write the prep per question** — talking points to answer well (3–5), verified facts (mark
   unconfirmed as "ověřit"), **episode callbacks** ("→ díl 9: …" when the topic was covered before),
   one soundbite in the guest's register, optional "pozor na". Personal items you can't research:
   scaffold an angle and mark "doplnit vlastními detaily". See `prep-method.md` §5.
7. **Build & deliver the brief** — build the self-contained HTML page (load the `artifact-design`
   skill if available to calibrate design), then deliver it in whichever way lets the guest review it
   best. Offer both and let the user choose (see "Output & delivery" below):
   - **Hosted Artifact** — publish via the Artifact tool; a shareable link, opens on any device.
   - **Local web server** — write the HTML to a file and serve it locally, bound to localhost
     only (e.g. `python3 -m http.server --bind 127.0.0.1` in that dir — the brief may contain
     private material and must not be visible to the LAN), then give the user the
     `http://localhost:PORT/…` URL.
   If one path isn't available in the current environment (no Artifact tool, or no shell), use the
   other rather than failing.

## Output & delivery

The deliverable is one **self-contained HTML page** (same content regardless of delivery mode):

- **Format:** inline CSS, no external assets (an Artifact's CSP blocks external hosts; keeping it
  self-contained also makes the local-server copy work offline). Responsive / readable on a phone
  during recording.
- **Structure:** header (podcast name, guest, length, format) → one section per block → one card per
  question containing: the question, talking points, highlighted facts/numbers, **episode callbacks**
  (a distinct "už zaznělo v pořadu" element linking to the relevant díl(s) and what was said there),
  a visually separated **soundbite**, and optional "pozor na".
- **Style:** clean, fast to scan; a light, high-contrast reading surface works best during recording.
  `favicon: 🎙️`. Keep the `<title>` stable (episode / guest name).
- **Language:** the podcast's language (Czech for Deeplink).
- **Delivery modes:**
  - *Artifact* — publish the file with the Artifact tool; report the link.
  - *Local server* — write the file (a temp/working dir is fine), start a simple static server in
    that directory **bound to 127.0.0.1** (never all interfaces), and report the local URL. Mention
    how to stop it. This is handy for reviewing privately or when Artifact hosting isn't available.

## Guardrails

- **Never invent facts, numbers, quotes, or personal details.** Verify against a real source or mark
  "ověřit" / "doplnit". A wrong number said on air is worse than a gap in the prep.
- **External stats must be exact** — right source, year, and wording; note where precision is uncertain.
- **Confidentiality:** the podcast is public — don't surface unpublished/sensitive info about the
  guest or their customers, including anything read from a knowledge base, without the guest's ok.
- **Knowledge-base consent:** never read a personal/company KB without the user's explicit approval;
  if a KB is already connected, announce which one and ask before using it (see `prep-method.md` §3).
- **Standalone:** don't depend on machine-specific *sources* (local repos, one person's files) — only
  bundled references + live/public web. Writing the brief to a local file and serving it is a fine
  *output*; the constraint is about inputs, not deliverables.
