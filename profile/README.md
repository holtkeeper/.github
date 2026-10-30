<p align="center">
  <a href="https://github.com/holtkeeper/holtkeeper"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/banner.png" alt="Holtkeeper — the keeper of your repository holt"></a>
</p>

<p align="center">
  <a href="https://github.com/holtkeeper/holtkeeper"><b>Repository</b></a> ·
  <a href="https://github.com/holtkeeper/holtkeeper/blob/main/docs/PLAN.md">Plan</a> ·
  <a href="https://github.com/holtkeeper/holtkeeper/blob/main/docs/README.md">Modules</a> ·
  <a href="https://github.com/holtkeeper/holtkeeper/blob/main/docs/development.md">Development</a>
</p>

Holtkeeper is an automation engine for a fleet of Git repositories on GitLab and GitHub. Every
automation is a plugin on one contract, configured as code in `holtkeeper.config.ts` and run
from the CLI, a scheduled pipeline, webhooks, the web UI or a chat bot. Every change goes through
a merge request, never a direct push. TypeScript on Bun, MIT.

## What it keeps

<table>
  <tr>
    <td width="88" align="center"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/icon-review.png" width="64" alt=""></td>
    <td><b>Review</b><br>AI review of merge requests: line threads with suggestions, a summary, replies in threads and incremental re-review on every push.</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/icon-updates.png" width="64" alt=""></td>
    <td><b>Updates</b><br>Package updates propagated across the fleet through Renovate; when a pipeline breaks, the agent reads the changelog and fixes the code in the same branch.</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/icon-audit.png" width="64" alt=""></td>
    <td><b>Audit</b><br>Vulnerabilities from lockfiles of any ecosystem via OSV-Scanner, fixed per package manager, with an allowlist whose entries expire.</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/icon-browserslist.png" width="64" alt=""></td>
    <td><b>Browserslist</b><br>Scheduled <code>update-browserslist-db</code> per repository group, with a before/after diff of the resolved browsers in the merge request.</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/icon-release.png" width="64" alt=""></td>
    <td><b>Release</b><br>A changelog, readiness checks, tags, release notes and manual deploy jobs, with a human confirming every dangerous step.</td>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/icon-quality.png" width="64" alt=""></td>
    <td><b>Quality</b><br>Lint, dead code, duplication, leaked secrets, licenses, bundle size and config drift, reported across every repository.</td>
  </tr>
</table>

## Repositories

<table>
  <tr>
    <td width="88" align="center"><img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/icon-holtkeeper.png" width="64" alt=""></td>
    <td>
      <a href="https://github.com/holtkeeper/holtkeeper"><b>holtkeeper</b></a> — the engine<br>
      The core and plugin contract, forge adapters, analyzers, the <code>holtkeeper</code> CLI, the server and the web UI.<br>
      <sub><a href="https://github.com/holtkeeper/holtkeeper/blob/main/docs/README.md">Docs</a> · TypeScript, Bun, React</sub>
    </td>
  </tr>
</table>

<sub>Status: pre-alpha. Everything here changes freely until the first tagged release.</sub>

---

<p align="center">
  <img src="https://github.com/holtkeeper/.github/raw/main/profile/assets/ai-disclaimer.png" alt="Disclaimer: fully AI-generated. Not a single line of code was written or reviewed by a human. Use at your own risk.">
</p>

> [!CAUTION]
> **Fully AI-generated.** Not a single line of this project was written or reviewed by a human: all of it was
> written by Claude through Claude Code. It's a Pandora's box, so use it at your own risk.
