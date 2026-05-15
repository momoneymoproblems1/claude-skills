# claude-skills

Personal Claude Code skills marketplace — 22 skills across finance, design, engineering, and productivity.

## Skills included

### Finance & Professional
| Skill | Description |
|-------|-------------|
| `boris` | 87 Claude Code workflow tips from Boris Cherny |
| `compliance-officer` | SEC/FINRA Compliance Officer (CCO responsibilities) |
| `finance-skills` | Ratio analysis, DCF valuation, budget variance, rolling forecasts |
| `financial-planner` | CFP comprehensive financial planning |
| `insurance-specialist` | Life, disability, LTC, and annuity planning |
| `investment-adviser` | RIA/IAR fiduciary investment advice |
| `retirement-specialist` | 401(k), IRA, Roth, Social Security optimization |

### Design & Frontend
| Skill | Description |
|-------|-------------|
| `accessibility` | WCAG 2.2 Level AA audits and ARIA implementation |
| `critique` | UX design critique with quantitative scoring |
| `design-system` | Generate and audit design systems |
| `frontend-patterns` | React, Next.js, state management patterns |
| `svg-logo-designer` | Professional SVG logo generation |
| `ui-ux-pro-max` | UI/UX intelligence: 50+ styles, 161 palettes, 57 font pairings |

### Engineering
| Skill | Description |
|-------|-------------|
| `api-design` | REST API design patterns and conventions |
| `backend-patterns` | Node.js/Express/Next.js API architecture |
| `blueprint` | Multi-session, multi-agent project planning |
| `coding-standards` | Consistent code quality standards |
| `e2e-testing` | Playwright E2E testing patterns and CI/CD |

### Productivity
| Skill | Description |
|-------|-------------|
| `caveman` | Ultra-compressed ~75% token reduction mode |
| `find-skills` | Discover and install Claude Code skills |
| `using-superpowers` | Master Claude Code advanced capabilities |
| `vercel-react-best-practices` | Vercel Engineering React/Next.js performance patterns |

## Add this marketplace to Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "plugins": [
    {
      "type": "github",
      "repo": "drewg27/claude-skills",
      "branch": "main"
    }
  ]
}
```

To install a single skill:

```json
{
  "plugins": [
    {
      "type": "github",
      "repo": "drewg27/claude-skills",
      "path": "plugins/caveman"
    }
  ]
}
```
