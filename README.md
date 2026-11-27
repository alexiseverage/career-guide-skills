# Career Guide Skills

Turn a career goal into a print-ready workbook, a researched local opportunity directory, or both. Each is an independently installable [Agent Skill](https://agentskills.io/specification).

| Skill | Use it for |
| --- | --- |
| [`career-guide-book`](skills/career-guide-book/SKILL.md) | A practical career guide with lessons, actions, readiness checkpoints, and reusable worksheets. Defaults to 50 total PDF pages. |
| [`local-opportunity-directory`](skills/local-opportunity-directory/SKILL.md) | A dated list of nearby employers, studios, training programs, or other public career leads. Can accompany a guide or stand alone. |

## Install

Use the [skills CLI](https://skills.sh/docs/cli) and select the skills and agent you want. Access to the repository is required while it is private.

```sh
npx skills add alexiseverage/career-guide-skills
```

To install from an existing checkout, run `npx skills add .` from the repository root. For agents with manual installation, copy the entire desired folder from `skills/` to your agent's skill directory. In environments without skill discovery, give the agent the relevant `SKILL.md` and its supporting files as task context.

## Ask for a guide

> Create a career guide for a beginner transitioning into bicycle repair. Include practice exercises, a tool budget, and milestones for applying to shops.

> Make a 24-page workbook for starting a bookkeeping career. Use A4, keep it low-ink, and skip optional styling.

> Find bicycle repair shops within 20 km of Edinburgh city centre where I could ask about work experience. Include public contacts and label any confirmed openings.

Both skills default to a print-ready PDF and self-contained editable HTML. Paper size follows the intended print locale where known, with US Letter as the fallback. The default styling works in grayscale. If you opt in, [Aesthetic Frontend Skills](https://github.com/alexiseverage/aesthetic-frontend-skills) can provide style direction adapted for print.

Current facts and local leads require web research or supplied evidence. PDF delivery requires an agent that can create files and render or export documents. With fewer capabilities, the skills can provide the editable source or an honest research worksheet and explain what is still unverified.

## Develop

See the [glossary](GLOSSARY.md), the [packaging decision](docs/adr/0001-standalone-skills.md), and the [smoke tests](tests/README.md). Keep examples fictional and exclude completed personal guides, private research, and machine-specific configuration.
