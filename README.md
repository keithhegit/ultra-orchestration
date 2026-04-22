# Ultra Orchestration Skills

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![Repo Status](https://img.shields.io/badge/status-active-success)](#)
[![Method](https://img.shields.io/badge/method-OpenSpec%20%2B%20Ultra-informational)](#methodology-core)

[English](#english) | [中文](#中文)

## English

Ultra Orchestration is an open-source skill repository for disciplined
AI-assisted software delivery.

It keeps the original repository theme intact:

- **OpenSpec specification plane** for long-lived program, milestone, and change assets
- **Ultra-Orchestrator execution plane** for intake, planning, dispatch, execution,
  review, QA, delivery, and retro

This repository is the source of truth for the skill system, references, helper
scripts, and orchestration methodology.

Backstory and whitepaper page:

- [GitHub Pages / docs.html](https://keithhegit.github.io/ultra-orchestration/docs.html)

## What Is Included

### Stable core skill suite

Under [`skills/`](./skills/):

- `ultra-orchestrator`
- `openspec-ultra-bridge`
- `clarify-and-intake`
- `decision-complete-planner`
- `dispatch-and-track`
- `spec-review`
- `code-review`
- `qa-verify`
- `risk-vetter`
- `safety-guard`
- `deliver-and-retro`
- `autoplan`

These remain the canonical stable delivery contract.

### vNext experimental skill suite

Under [`skills-vnext/`](./skills-vnext/):

- `ultra-vnext-core`
- `ultra-brainstorming`
- `ultra-planning`
- `ultra-execution-control`
- `ultra-review`
- `ultra-qa`
- `openspec-ultra-bridge-v2`

This track is designed to absorb the strongest ideas from:

- `obra/superpowers`
  design-first workflow, one-question-at-a-time clarification, and hard gates
- `OpenSpec`
  durable proposal/design/tasks/archive assets
- `gstack`
  role discipline and structured delivery flow
- `forrestchang/andrej-karpathy-skills`
  simple high-signal engineering principles
- `oh-my-codex`
  runtime awareness, orchestration traces, and heavier workflow posture

The vNext goal is not to replace Ultra's theme or control plane. It upgrades the
same Ultra direction with:

- finite-state-machine loopbacks instead of a fragile linear waterfall
- context-firewall handoff through artifacts, not full chat inheritance
- DAG plus write-lock dispatch rules for safe parallelism
- host-driven ledger ownership
- richer design and planning prompts before implementation

## Methodology Core

### 1. Two-plane collaboration

- **OpenSpec** owns long-lived specification assets and status accounting
- **Ultra-Orchestrator** owns execution control, quality gates, and delivery evidence

Neither replaces the other. They stay synchronized.

### 2. Delivery structure

For non-trivial work, use:

1. `Program`
2. `Milestone`
3. `Change`
4. `Slice`

Then run execution in this phase order:

1. Intake
2. Plan
3. Dispatch
4. Execute
5. Review
6. QA
7. Deliver
8. Retro

### 3. Progress accounting

- `Change` is the specification and planning unit
- `Slice` is the implementation and verification unit

Do not run milestone-wide engineering without change and slice decomposition.

### 4. Slice status discipline

Canonical slice states:

- `slice_0_not_opened`
- `slice_0_spec_ready`
- `slice_1_completed`
- `slice_2_in_progress`
- `slice_3_qa_pending`
- `slice_4_done`

Advance slice status only with verification evidence.

### 5. Bridge discipline

Each active change should include:

- `proposal.md`
- `tasks.md`
- `ultra-bridge.md`

Recommended for richer changes:

- `design.md`

After each completed slice:

1. update `tasks.md`
2. update `ultra-bridge.md`
3. update any program-facing status rollups if counts changed
4. record verification evidence

## Repository Layout

```text
.github/
  ISSUE_TEMPLATE/
  workflows/
skills/
  autoplan/
  clarify-and-intake/
  code-review/
  decision-complete-planner/
  deliver-and-retro/
  dispatch-and-track/
  openspec-ultra-bridge/
  qa-verify/
  risk-vetter/
  safety-guard/
  spec-review/
  ultra-orchestrator/
skills-vnext/
  ultra-vnext-core/
  ultra-brainstorming/
  ultra-planning/
  ultra-execution-control/
  ultra-review/
  ultra-qa/
  openspec-ultra-bridge-v2/
docs/
  ultra-vnext-pilot-guide-CN.md
docs.html
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
```

## How To Use

### Install the stable suite

Copy folders from [`skills/`](./skills/) into your global skill directory.

Example on Windows:

```powershell
Copy-Item -Recurse -Force .\skills\ultra-orchestrator C:\Users\<you>\.cursor\skills\ultra-orchestrator
```

### Evaluate the vNext suite

Use [`skills-vnext/`](./skills-vnext/) as an experimental track for pilot work.

The current recommended pilot is:

- use OpenSpec as the long-lived spec layer
- keep Ultra as the control plane
- validate one bounded change at a time

Chinese pilot guide:

- [docs/ultra-vnext-pilot-guide-CN.md](./docs/ultra-vnext-pilot-guide-CN.md)

## Source And Release Workflow

1. update or add skills in this repository
2. validate the workflow in a real project
3. commit and tag a release if needed
4. sync released skills into your global skill directory

## License

This project is licensed under the **Apache License 2.0**.
See [LICENSE](./LICENSE).

---

## 中文

Ultra Orchestration 是一个面向 AI 辅助软件交付的开源技能仓库。

本仓库保持原有主题不变，核心仍然是“双平面协作”：

- **OpenSpec 规格平面**：负责长期规格资产、里程碑、变更与归档
- **Ultra-Orchestrator 编排平面**：负责 Intake、Plan、Dispatch、Execute、
  Review、QA、Deliver、Retro 的执行控制

仓库继续作为技能、参考资料、辅助脚本和方法论的源码基线。

白皮书与背景页：

- [GitHub Pages / docs.html](https://keithhegit.github.io/ultra-orchestration/docs.html)

## 当前包含两条技能线

### 1. 稳定主线

位于 [`skills/`](./skills/)：

- `ultra-orchestrator`
- `openspec-ultra-bridge`
- `clarify-and-intake`
- `decision-complete-planner`
- `dispatch-and-track`
- `spec-review`
- `code-review`
- `qa-verify`
- `risk-vetter`
- `safety-guard`
- `deliver-and-retro`
- `autoplan`

这条线仍然是当前仓库的稳定交付主线。

### 2. vNext 实验线

位于 [`skills-vnext/`](./skills-vnext/)：

- `ultra-vnext-core`
- `ultra-brainstorming`
- `ultra-planning`
- `ultra-execution-control`
- `ultra-review`
- `ultra-qa`
- `openspec-ultra-bridge-v2`

这条线吸收了多种优秀方法，但不改变仓库主题，也不替代 Ultra 的控制平面定位。

重点吸收来源：

- `obra/superpowers`
  强化 design-first、逐问澄清、hard gate
- `OpenSpec`
  强化 proposal / design / tasks / archive 的长期规格资产
- `gstack`
  强化角色纪律与阶段化交付
- `forrestchang/andrej-karpathy-skills`
  强化高密度、低噪声的工程原则
- `oh-my-codex`
  强化运行时意识、轨迹记录与工程化工作流姿态

vNext 的主要升级点：

- 用有限状态机闭环替代脆弱的线性瀑布流
- 用 artifact handoff 替代全文聊天历史继承
- 用 DAG + 写锁约束来定义安全并发
- 用 host-driven ledger 取代大 JSON 由模型直接重写
- 在编码前强化 design 与 planning 提示质量

## 方法论核心

### 1. 双平面协作

- **OpenSpec** 负责长期规格资产与状态核算
- **Ultra-Orchestrator** 负责执行控制、质量门禁与交付证据

两者同步协作，互不替代。

### 2. 项目结构与执行流

对非平凡任务，先按以下结构组织：

1. `Program`
2. `Milestone`
3. `Change`
4. `Slice`

然后按以下阶段执行：

1. Intake
2. Plan
3. Dispatch
4. Execute
5. Review
6. QA
7. Deliver
8. Retro

### 3. 进度核算单位

- `Change` 是规格与计划单位
- `Slice` 是实现与验证单位

不要直接以整段 Milestone 作为粗粒度开发单位。

### 4. Slice 状态纪律

使用以下标准状态：

- `slice_0_not_opened`
- `slice_0_spec_ready`
- `slice_1_completed`
- `slice_2_in_progress`
- `slice_3_qa_pending`
- `slice_4_done`

只有在存在验证证据时，才推进 slice 状态。

### 5. Bridge 同步纪律

每个活跃 change 建议至少包含：

- `proposal.md`
- `tasks.md`
- `ultra-bridge.md`

更复杂的变更建议补上：

- `design.md`

每完成一个 slice，至少同步四件事：

1. 更新 `tasks.md`
2. 更新 `ultra-bridge.md`
3. 如果项目级统计变化，更新汇总状态文档
4. 记录验证证据

## 如何使用

### 安装稳定主线

把 [`skills/`](./skills/) 里的技能目录复制到你的全局技能目录。

Windows 示例：

```powershell
Copy-Item -Recurse -Force .\skills\ultra-orchestrator C:\Users\<你>\.cursor\skills\ultra-orchestrator
```

### 试跑 vNext

把 [`skills-vnext/`](./skills-vnext/) 当作实验线使用，先在真实项目里做 pilot。

推荐 pilot 方法：

- 用 OpenSpec 做长期规格层
- 用 Ultra 做控制平面
- 一次只验证一个边界清晰的 change

中文试跑说明：

- [docs/ultra-vnext-pilot-guide-CN.md](./docs/ultra-vnext-pilot-guide-CN.md)

## 源码与发布流程

1. 在本仓库中更新技能
2. 在真实项目中验证
3. 提交并按需要打 tag
4. 将已发布版本同步到全局技能目录

## License

本项目使用 **Apache License 2.0**。
详见 [LICENSE](./LICENSE)。
