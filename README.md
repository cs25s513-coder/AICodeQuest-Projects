# AICodeQuest — Week-Long Training Study

## Welcome

Four starter projects. Pick one with your team, and go make it better —
with an AI coding assistant riding shotgun.

- 🌌 **MoonTrip** — a cheerful, wildly-subsidised space-tourism agency
  selling trips to the Moon, Mars, and everywhere in between.
- 🕳️ **BlackHole Explorer** — an interactive observatory for black holes,
  bent starlight, slowed clocks, and spaghettification.
- 🚀 **RocketMart** — everything you need to leave the planet, one cart at
  a time.
- 🗣️ **Bhasha Bharat** — learn India's languages, one lesson and one
  flashcard at a time.

## The week

`[STUDY_DATES]`

- **Day 0** — onboarding: fork the repo, get your project running, install
  the extension.
- **Days 1–5** — build: pick tasks from your project's README, ship them
  as pull requests.
- **Day 6** — demo day.
- **Day 7** — wrap-up.

## Get started

1. Fork [`[REPO_URL]`]([REPO_URL]), then clone your fork.
2. Pick your team's project and follow its README to run it.
3. Install the extension: `[EXTENSION_INSTALL]`.

## The rules

- **Use an AI coding assistant** (Copilot, ChatGPT, Claude, anything) to
  write your task code. That is the point of the study. Note which
  assistant you used in your pull request.
- **One task = one pull request.** Don't combine tasks, and don't split
  one task across several PRs.
- **Tag honestly.** When the extension asks which parts an AI wrote,
  answer truthfully. There is no penalty either way.
- **Keep the game to yourself.** Don't share bugs, answers or screenshots
  of the game with teammates.
- Follow the coding rules in your project README.

## How the game works

> **When does the game start?**
> When you open a pull request for a **feature-sized** change that
> touches your project's logic, API and web code together, the extension
> pauses the *Create pull request* button and starts the game. Every
> numbered task (M1, B1, R1, L1, …) is designed to start it. Warm-up
> tasks, data-only edits (`data/*.json`), documentation and small tweaks
> do not.
>
> **What happens?**
> 1. **Tag your code.** Mark which parts of your change an AI assistant
>    wrote.
> 2. **Defend (4 rounds).** We plant a bug in one of *your* functions.
>    Find it and fix it.
> 3. **Understand (5 questions).** Predict what one of your functions
>    returns for a given input.
> 4. **Attack (4 rounds).** Plant a bug of your own and see whether our
>    AI can repair it.
>
> It takes about 10–15 minutes. To pass, `[PASS_MARK]`. If you don't
> reach the pass mark, you can play another round with fresh bugs. When
> you pass, the *Create pull request* button unlocks.
>
> **Rewards.** Every bug you catch counts. Badges, streaks and
> celebrations are waiting — check the Badges page in the extension.

## Help

Need a hand? `[SUPPORT_CONTACT]`.

| Problem | Try this |
|---|---|
| App doesn't start | Check you ran both the API and web commands from your project's README, in the right folder. Check the prerequisite runtime versions (Python/Node/Java) match what the README asks for. |
| Port already in use | Something else on your machine is using that project's port. Stop it, or check your project README for the exact port numbers. |
| The game didn't start | Warm-up tasks (W1, W2) and data-only edits don't start it — that's expected. Make sure your PR touches `logic/`, `api/` and `web/` together for a numbered task. |
| The extension says I'm signed out | Re-run the sign-in step from `[EXTENSION_INSTALL]`. |
