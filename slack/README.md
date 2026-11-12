# Slack app

Display settings for the Holtkeeper Slack app. Paste them into **Basic Information → Display
Information** of the app at [api.slack.com/apps](https://api.slack.com/apps), or merge
[`manifest.yml`](manifest.yml) into the app manifest.

<img src="../profile/assets/slack-bot.png" width="160" alt="Holtkeeper Slack bot avatar">

## Permissions and events

[`manifest.yml`](manifest.yml) lists the bot scopes and events. The ones the current features need:

| Scope              | For                                                                  |
| ------------------ | -------------------------------------------------------------------- |
| `channels:history` | read messages in public channels the bot is in, to find merge request links |
| `groups:history`   | the same in private channels                                         |
| `reactions:write`  | set the review status emoji on those messages                        |
| `chat:write`       | post release announcements and the per-merge-request status list    |

Events: `message.channels` and `message.groups`, sent to `https://<your Holtkeeper host>/api/slack/events`.
Replace the example host in the manifest with yours. Slack checks the URL when you save it, so turn
Event Subscriptions on after Holtkeeper has the app's bot token and signing secret. After changing
scopes, reinstall the app to the workspace.

## Icon

[`profile/assets/slack-bot.png`](../profile/assets/slack-bot.png): the organization avatar at
1024 × 1024, rendered by `scripts/render.py`. Slack rounds the corners itself; the drawing keeps
clear of them.

## Review status emoji

Custom emoji for the review status reactions, in [`emoji/`](emoji). Upload them under
**Customize workspace → Emoji** with the names below, then set those names in the review status
settings instead of the defaults. Each one is the mascot's head drawn in the status color with the status sign on its forehead: the color and sign carry the meaning at reaction size (16 px), the ears and muzzle keep it recognizable as Holtkeeper. The dot of the exclamation mark is the nose.

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
| Background color   | `#0B0B0C`                                                                   |

Long description:

> Holtkeeper watches a fleet of GitLab and GitHub repositories and brings what needs a person to
> Slack.
>
> • Reviews: a status emoji on messages that link a merge request, updated as the AI review runs
> and finishes.
> • Updates and audits: failed dependency updates, new vulnerabilities and allowlist entries about to
> expire.
> • Releases: announcements of new versions with grouped changes, tasks, breaking changes and the
> repositories an upgrade would break.
> • Ask: mention @holtkeeper in a thread or send it a direct message to ask about a repository, a
> package or a job.
>
> Buttons in its messages run the same commands as the web panel, under your own permissions.

## Colors

The Graphite palette of the web UI, which the mascot and banners use too (same constants as
`scripts/render.py`):

| Name   | Hex       | Use                                                   |
| ------ | --------- | ----------------------------------------------------- |
| Bg     | `#0B0B0C` | tile background; Slack "Background color"             |
| Panel  | `#111113` | raised surfaces, the top of tile gradients            |
| Fg     | `#EDEDEF` | text on dark                                          |
| Muted  | `#93939B` | secondary text                                        |
| Accent | `#F0A63A` | the one accent: the mascot, links, attachment color bar |

Message tone colors for attachment bars, as in the web UI: success `#3ECF8E`, warning `#F0B03A`,
danger `#F2665F`, info `#6AA2FF`, neutral `#F0A63A`.
