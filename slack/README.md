# Slack app

Display settings for the Holtkeeper Slack app. Paste them into **Basic Information → Display
Information** of the app at [api.slack.com/apps](https://api.slack.com/apps), or merge
[`manifest.yml`](manifest.yml) into the app manifest.

<img src="../profile/assets/slack-bot.png" width="160" alt="Holtkeeper Slack bot avatar">

## Icon

[`profile/assets/slack-bot.png`](../profile/assets/slack-bot.png), 1024 × 1024, rendered from
[`slack-bot.svg`](../profile/assets/slack-bot.svg) by `scripts/render.py`. The mascot from the
organization avatar with a speech bubble, so the bot is told apart from the org in the sidebar.
Slack rounds the corners itself; the drawing keeps clear of them.

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
