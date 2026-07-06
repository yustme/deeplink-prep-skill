# deeplink-prep-skill

A [Claude Code](https://claude.com/claude-code) plugin marketplace shipping one plugin:
**`deeplink-podcast-prep`** — prepare a guest to answer well on the
[Deeplink Show](https://www.youtube.com/@DeeplinkShow) podcast.

From the host's prepared question doc (usually a Notion link) it builds one interactive HTML
prep brief — for each question: talking points, verified facts, callbacks to earlier Deeplink
episodes that covered the topic, and a soundbite in the guest's register.

## Install

```
/plugin marketplace add yustme/deeplink-prep-skill
/plugin install deeplink-podcast-prep@deeplink-prep
```

Then start with e.g. "připrav mě na Deeplink" or paste the question doc link. The skill is also
invocable directly as `/deeplink-podcast-prep:deeplink-podcast-prep`.

## Update

```
/plugin marketplace update deeplink-prep
```

## What it does

1. Reads the guest and questions out of the host's doc (pasted or fetched).
2. Matches each question against a bundled map of all past Deeplink episodes, so the guest can
   reference the show's back-catalog on air ("to jste probírali v díle 9…").
3. Researches the guest live and verifies every number the questions cite; optionally draws on a
   personal/company knowledge base — only with explicit approval.
4. Delivers one self-contained HTML brief, as a hosted Artifact or from a local web server.

It never invents facts, quotes, or episode callbacks — unverified items are marked "ověřit" /
"doplnit". Briefs are in Czech (the show's language).

## Maintaining

See [MAINTAINING.md](MAINTAINING.md) — repo layout, release process, and the common task of
adding new episodes to the episode map.

## License

[MIT](LICENSE)
