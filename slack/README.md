# Slack app

Display settings for the Holtkeeper Slack app. Paste them into **Basic Information → Display
Information** of the app at [api.slack.com/apps](https://api.slack.com/apps), or merge
[`manifest.yml`](manifest.yml) into the app manifest.

<img src="../profile/assets/slack-bot.png" width="160" alt="Holtkeeper Slack bot avatar">

## Icon

[`profile/assets/slack-bot.png`](../profile/assets/slack-bot.png): the organization avatar at
1024 × 1024, rendered by `scripts/render.py`. Slack rounds the corners itself; the drawing keeps
clear of them.

## Review status emoji

Custom emoji for the review status reactions, in [`emoji/`](emoji). Upload them under
**Customize workspace → Emoji** with the names below, then set those names in the review status
settings instead of the defaults. Each one is the mascot's head with a status badge in the corner:
the badge carries the meaning at 22 px, the face backs it up when the emoji is shown larger.

| Status                         | Name              | File                                                              | Default |
| ------------------------------ | ----------------- | ----------------------------------------------------------------- | ------- |
| Review in progress             | `:hk-reviewing:`  | [`hk-reviewing.gif`](emoji/hk-reviewing.gif) (animated, looks around) | 👀      |
| Clean                          | `:hk-clean:`      | [`hk-clean.png`](emoji/hk-clean.png)                              | 🟢      |
| Minor comments only            | `:hk-minor:`      | [`hk-minor.png`](emoji/hk-minor.png)                              | 🟠      |
| Needs changes                  | `:hk-changes:`    | [`hk-changes.png`](emoji/hk-changes.png)                          | 🔴      |
| Not reviewed (too large)       | `:hk-skipped:`    | [`hk-skipped.png`](emoji/hk-skipped.png)                          | ⚪      |

<img src="emoji/hk-reviewing.gif" width="64"> <img src="emoji/hk-clean.png" width="64"> <img src="emoji/hk-minor.png" width="64"> <img src="emoji/hk-changes.png" width="64"> <img src="emoji/hk-skipped.png" width="64">

All are 128 × 128 with a transparent background and well under Slack's 128 KB limit. The animated
one has a static twin, `hk-reviewing.png`, for workspaces that turn animation off. Only the
in-progress status moves: finished statuses stay still so a channel full of them does not flicker.

## Texts

| Field              | Value                                                                       |
| ------------------ | --------------------------------------------------------------------------- |
| App name           | Holtkeeper                                                                  |
| Bot display name   | holtkeeper                                                                  |
| Short description  | Keeps your Git repositories in order: reviews, updates, audits and releases. |
| Background color   | `#1E140D`                                                                   |

Long description:

> Holtkeeper watches a fleet of GitLab and GitHub repositories and brings what needs a person to
> Slack.
>
> • Reviews: a summary when an AI review lands on a merge request, and a ping when a thread waits
> for an answer.
> • Updates and audits: failed dependency updates, new vulnerabilities and allowlist entries about to
> expire.
> • Releases: readiness checks, changelogs and a button to start the deploy job.
> • Ask: mention @holtkeeper in a thread or send it a direct message to ask about a repository, a
> package or a job.
>
> Buttons in its messages run the same commands as the web panel, under your own permissions.

## Colors

The palette of the mascot (same constants as `scripts/render.py`):

| Name   | Hex       | Use                                              |
| ------ | --------- | ------------------------------------------------ |
| Ink    | `#1A120C` | text on light, eyes; app background in Slack     |
| Night  | `#1E140D` | tile background (Slack "Background color")       |
| Orange | `#FF7A1A` | primary accent: the head, attachment color bar   |
| Ember  | `#D95A0B` | pressed and hover states, outer ears             |
| Amber  | `#FFB547` | highlights: key, speech bubble, warnings         |
| Cream  | `#FFE6CC` | muzzle, soft backgrounds                         |

Message tone colors for attachment bars, if a message uses them: success `#1F9D55`, warning
`#FFB547`, danger `#E5484D`, info `#0EA5E9`, neutral `#FF7A1A`.
