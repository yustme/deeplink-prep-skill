# Maintaining & distributing the `deeplink-podcast-prep` plugin

This repo is a **Claude Code plugin marketplace** that ships one plugin (`deeplink-podcast-prep`),
which provides the skill. Below: how users install it, how to release updates, and — most often —
how to **add new Deeplink episodes to the episode map**.

## Repo layout

```
.
├── .claude-plugin/
│   └── marketplace.json                       # marketplace catalog (repo root)
├── plugins/
│   └── deeplink-podcast-prep/                  # the plugin
│       ├── .claude-plugin/
│       │   └── plugin.json                     # plugin manifest
│       └── skills/
│           └── deeplink-podcast-prep/          # the skill
│               ├── SKILL.md                    # purpose, workflow, guardrails
│               └── references/
│                   ├── prep-method.md          # runtime playbook (how to build a brief)
│                   ├── deeplink-show.md        # show format + fictional example question doc
│                   └── episode-map.md          # ← the back-catalog you keep growing
├── scripts/                                    # maintainer tools (NOT shipped in the plugin)
│   ├── youtube_transcript.py                   # pull a YouTube transcript
│   └── test_youtube_transcript.py
├── requirements.txt                            # deps for scripts/
├── transcripts/                                # raw transcripts — LOCAL ONLY, gitignored
└── MAINTAINING.md
```

## Installing (for users)

```bash
/plugin marketplace add yustme/deeplink-prep-skill
/plugin install deeplink-podcast-prep@deeplink-prep
```

The skill is then available as `/deeplink-podcast-prep:deeplink-podcast-prep`. `/plugin list` shows
what's installed.

## Releasing an update

The marketplace serves the plugin straight from this repo — there's nothing to package. To publish
a change:

1. Edit the skill / manifests, commit, and push to `main`.
2. **Bump `version`** in `plugins/deeplink-podcast-prep/.claude-plugin/plugin.json` (semver). Clients
   key updates off this — if you don't bump it, installs won't see the change. (Omit `version`
   entirely only if you want every commit SHA treated as a new version.)
3. Users update with `/plugin marketplace update deeplink-prep` (or reinstall).

## Non-negotiable constraints (don't break these)

- **Standalone.** The skill must run in any environment where it's installed, using only its own
  bundled files + live/public web. No local paths, no `transcripts/`, no single-machine sources at
  runtime. That's why episode knowledge is *distilled into `episode-map.md`*, not read from
  transcripts live.
- **No personal info baked in.** The skill is generic; `deeplink-show.md`'s example is fictional. The
  episode map may name public podcast guests (S-series) — that's the show's public catalog, fine.
- **Grounded, not invented.** Every episode entry reflects what the episode actually covered. Never
  add a topic or a "díl N" callback that isn't real.

## Adding new episodes to the episode map (the common task)

`skills/deeplink-podcast-prep/references/episode-map.md` has two parts: a **topic index**
(téma → díly) at the top, and a **per-episode detail** list below. When new episodes air, update both.

### 1. Get the transcript

Drop the transcript into `transcripts/` locally (it stays gitignored). Naming mirrors existing files,
e.g. `ep20_nazev-tematu.txt` or `S04_jmeno-hosta.txt`.

**From a YouTube video** — use `scripts/youtube_transcript.py`, which pulls the video's captions
(incl. auto-generated) and writes them to a text file:

```bash
pip install -r requirements.txt          # one-time: youtube-transcript-api
python scripts/youtube_transcript.py "https://www.youtube.com/watch?v=VIDEOID" \
    -o transcripts/ep20_nazev-tematu.txt
python scripts/youtube_transcript.py VIDEOID --languages cs en -o transcripts/ep20.txt
```

Accepts a full URL or a bare 11-char ID. If the video has no captions the script exits with a clear
error — then transcribe the audio another way (e.g. Whisper) and save the text.

(Older transcripts are one long line with `>>` turn delimiters and HTML entities; the YouTube helper
writes plain text, which is fine — the map is built from meaning, not formatting. To read a
`>>`-delimited file: `sed 's/>>/\n>>/g' FILE | less`.)

### 2. Distill one detail block per episode

Append a block to the **## Díly (detail)** section, in episode order, using this exact template:

```markdown
### Díl {N} — {krátký český název}
- **Host(s)/guest:** {Filip a Jindra; nebo "Filip (host) × {jméno hosta}" u S-dílů}
- **O čem díl je (1 věta):** {jedna věta}
- **Probíraná témata:** {8–12 KONKRÉTNÍCH podtémat — takových, na které se dá napasovat budoucí otázka}
- **Zapamatovatelné momenty / citace:** {2–3 krátké momenty/citace, citace pod ~20 slov}
- **Keywords:** {comma-separated lowercase tagy pro index}
```

Topics specific enough to match a question ("halucinace u lékařské diagnostiky", not "AI obecně");
quotes short and near-verbatim. Claude can distill a batch from the transcripts — review before
pasting and keep it grounded; don't let it invent.

### 3. Update the topic index

Add each new episode's `{N}` to every matching line in the **## Topic index**, and add a new line for
any theme not yet listed. The index powers topic lookup, so keep it in sync with the detail blocks.

### 4. Update the coverage note

Bump the "⚠️ Coverage note" line near the top of `episode-map.md` to the new highest episode, so the
skill knows how far the catalog reaches (and won't invent díly beyond it).

## Updating other parts of the skill

- **Behavior / workflow / guardrails** → `skills/deeplink-podcast-prep/SKILL.md`.
- **How a brief is built** (research, KB-consent step, output shape) → `references/prep-method.md`.
- **Show format / example input** → `references/deeplink-show.md`.
- If you renumber `prep-method.md` sections, fix the `§N` cross-references in `SKILL.md`.
- Keep the SKILL.md `description` free of a bare `": "` (colon+space) — it breaks the YAML frontmatter.
  Keep frontmatter `name:` equal to the skill folder name (`deeplink-podcast-prep`).

Quick self-check before shipping (swap in the guest's name/company you researched):

```bash
grep -rniE "{guest-name}|{company}" plugins/deeplink-podcast-prep && echo "FOUND — remove it" || echo "clean"
```

## Maintainer scripts

`scripts/` holds build-time tooling only — it is **not** part of the shipped plugin. Run its tests:

```bash
pip install -r requirements.txt
cd scripts && python -m pytest -q
```
