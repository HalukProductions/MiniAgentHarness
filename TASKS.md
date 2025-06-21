# MiniAgentHarness Roadmap

Starter kit for building test-first, easily deployable AI agents.

---

## Completed Tasks

- [x] Scaffolded Poetry project with CLI and stub agent
- [x] Added Pytest plugin, fixtures, and green sample test
- [x] Configured GitHub Actions `ci.yml` to run test suite
- [x] Reserved package names by publishing `mini-agent-harness==0.0.0` to **PyPI** and **NPM**
- [x] Flesh out `README.md` with badges, quick-start guide, and differentiators
- [x] Add GitHub Actions release workflow to publish to PyPI & NPM on version tags
- [x] Bump working version to `0.1.0.dev0` (Python) and `0.1.0-dev` (NPM)

## In Progress Tasks

- [ ] Implement core ReAct-style agent loop (`mini_agent_harness.core.loop`) **(initial echo LLM completed; full tool loop pending)**

## Future Tasks

- [ ] YAML tool registry with auto-import & CLI stub generation
- [ ] `mini-agent serve` FastAPI server with streaming SSE endpoint
- [ ] React webapp (`webapp/`) with shadcn/ui chat + playground
- [ ] Testing harness Phase 1: DeepEval metrics and Guardrails schema checks
- [ ] Testing harness Phase 2: LangSmith golden conversation replay
- [ ] One-click Vercel deploy (`deploy/vercel.json`) and README badge
- [ ] Cloudflare Workers edge target via `wrangler deploy`
- [ ] Docs site and launch assets (logo, screenshots, blog post)

## Implementation Plan

Phased approach (adapted from 6-week outline):

1. Core agent loop & expanded CLI
2. Testing harness Phase 1 (unit metrics)
3. Web UI skeleton
4. One-click deploy targets (Vercel → CF Workers)
5. Documentation polish & examples

## Relevant Files

- `mini_agent_harness/cli.py` – entry-point for `mini-agent` CLI ✅
- `mini_agent_harness/core/__init__.py` – stub `Agent` + `AgentResult` ✅
- `mini_agent_harness/testing/` – pytest plugin & fixtures ✅
- `.github/workflows/ci.yml` – CI running test suite ✅
- `README.md` – _currently being updated_
