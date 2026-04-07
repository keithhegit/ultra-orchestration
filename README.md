# Ultra Orchestration Skills

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![Repo Status](https://img.shields.io/badge/status-active-success)](#)
[![Method](https://img.shields.io/badge/method-OpenSpec%20%2B%20Ultra-informational)](#skill-methodology-core)

中文说明见下方 **[中文](#中文)**。

A curated open-source skill suite for disciplined AI-assisted software delivery using a dual-plane model:

- **OpenSpec specification plane**: `Program -> Milestone -> Change -> Slice`
- **Ultra-Orchestrator execution plane**: `Intake -> Plan -> Dispatch -> Execute -> Review -> QA -> Deliver -> Retro`

This repository is the source-of-truth for the skill system, references, and orchestration methodology.

## Quick Links

- Methodology: [Skill Methodology (Core)](#skill-methodology-core)
- Install in Cursor: [How to Use in Cursor](#how-to-use-in-cursor)
- Contributing: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Security: [SECURITY.md](./SECURITY.md)
- Code of Conduct: [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

## License

This project is licensed under the **Apache License 2.0**. See [`LICENSE`](./LICENSE).

## Repository Layout

```text
.github/
  ISSUE_TEMPLATE/
  workflows/
skills/
  autoplan/
  clarify-and-intake/
  code-review/
  codex_ultra_orchestration/
  decision-complete-planner/
  deliver-and-retro/
  dispatch-and-track/
  openspec-ultra-bridge/
  qa-verify/
  risk-vetter/
  safety-guard/
  spec-review/
  ultra-orchestrator/
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
```

## Skill Methodology (Core)

### 1) Two-plane collaboration

- **OpenSpec** owns long-lived specification assets and status accounting.
- **Ultra-Orchestrator** owns execution control, quality gates, and delivery evidence.

Both planes must stay synchronized. Neither replaces the other.

### 2) Program model and delivery flow

For product development, use this structure first:

1. `Program`
2. `Milestone`
3. `Change`
4. `Slice`

Then execute each non-trivial task in this mandatory phase order:

1. Intake
2. Plan
3. Dispatch
4. Execute
5. Review
6. QA
7. Deliver
8. Retro

### 3) What is the unit of progress?

- `Change` = spec/progress accounting unit
- `Slice` = implementation and verification unit

Do **not** run milestone-wide coding without change/slice decomposition.

### 4) Slice status contract

Use canonical statuses only:

- `slice_0_not_opened`
- `slice_0_spec_ready`
- `slice_1_completed`
- `slice_2_in_progress`
- `slice_3_qa_pending`
- `slice_4_done`

Advance slice status only with verification evidence.

### 5) Bridge discipline (OpenSpec ↔ Ultra)

Each opened change should include:

- `proposal.md`
- `tasks.md`
- `ultra-bridge.md`

`ultra-bridge.md` should contain at least:

- `change_id`
- `milestone`
- `status`
- `task_manifest_focus`
- `work_package_scope`
- `next_slice`

After each slice completion:

1. update `tasks.md`
2. update `ultra-bridge.md`
3. update program-facing status docs if counts/states changed
4. record verification evidence

## Included Skills

- `ultra-orchestrator` — Core control-plane orchestration
- `openspec-ultra-bridge` — OpenSpec ↔ Ultra artifact bridge
- `clarify-and-intake` — Requirement normalization
- `decision-complete-planner` — Decomposition and planning
- `dispatch-and-track` — Work package dispatch and tracking
- `code-review` — Engineering quality review
- `spec-review` — Specification consistency review
- `qa-verify` — QA verification gate
- `risk-vetter` — Risk classification before high-impact actions
- `safety-guard` — Safety guardrails and operation constraints
- `deliver-and-retro` — Delivery assembly and retrospectives
- `autoplan` — Fast planning pipeline
- `codex_ultra_orchestration` — Whitepapers, examples, run artifacts

## How to Use in Cursor

### Global installation (recommended)

Copy skill folders into Cursor global skills directory.

- Windows: `C:\Users\<you>\.cursor\skills\`

Example:

```powershell
Copy-Item -Recurse -Force .\skills\ultra-orchestrator C:\Users\<you>\.cursor\skills\ultra-orchestrator
```

Then restart Cursor or refresh agent context.

### Source and release workflow

1. edit/update skills in this repository
2. validate in a real project
3. commit + tag release
4. sync released skill folders to global directory

---

## 中文

这是一个面向开源协作的技能仓库，用于“规范平面 + 编排平面”双轨交付。

- **OpenSpec 规格平面**：`Program -> Milestone -> Change -> Slice`
- **Ultra-Orchestrator 编排平面**：`Intake -> Plan -> Dispatch -> Execute -> Review -> QA -> Deliver -> Retro`

本仓库是整套技能、参考资料和方法论的源码基线。

## 快速链接

- 方法论：[`Skill Methodology (Core)`](#skill-methodology-core)
- 安装方式：[`How to Use in Cursor`](#how-to-use-in-cursor)
- 贡献指南：[`CONTRIBUTING.md`](./CONTRIBUTING.md)
- 安全策略：[`SECURITY.md`](./SECURITY.md)
- 行为准则：[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)

## 许可证

本项目采用 **Apache License 2.0**。见 [`LICENSE`](./LICENSE)。

## 仓库结构

```text
.github/
  ISSUE_TEMPLATE/
  workflows/
skills/
  autoplan/
  clarify-and-intake/
  code-review/
  codex_ultra_orchestration/
  decision-complete-planner/
  deliver-and-retro/
  dispatch-and-track/
  openspec-ultra-bridge/
  qa-verify/
  risk-vetter/
  safety-guard/
  spec-review/
  ultra-orchestrator/
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
```

## Skill 方法论（核心）

### 1）双平面协作

- **OpenSpec** 负责长期规格资产与状态核算。
- **Ultra-Orchestrator** 负责执行控制、质量门禁、交付证据。

两者必须同步，不能互相替代。

### 2）项目作用流程（关键）

开发结构先按这条主线：

1. `Program`
2. `Milestone`
3. `Change`
4. `Slice`

然后每个中大型任务按固定编排阶段执行：

1. Intake
2. Plan
3. Dispatch
4. Execute
5. Review
6. QA
7. Deliver
8. Retro

### 3）进度核算单位

- `Change`：规格/进度核算单位
- `Slice`：实现与验证核算单位

不要直接按整个 Milestone 粗放式开发。

### 4）Slice 状态约定

仅使用以下状态：

- `slice_0_not_opened`
- `slice_0_spec_ready`
- `slice_1_completed`
- `slice_2_in_progress`
- `slice_3_qa_pending`
- `slice_4_done`

slice 状态推进必须有验证证据。

### 5）Bridge 同步纪律（OpenSpec ↔ Ultra）

每个已打开的 change 至少包含：

- `proposal.md`
- `tasks.md`
- `ultra-bridge.md`

`ultra-bridge.md` 至少包含：

- `change_id`
- `milestone`
- `status`
- `task_manifest_focus`
- `work_package_scope`
- `next_slice`

每完成一个 slice 后，至少做这 4 件事：

1. 更新 `tasks.md`
2. 更新 `ultra-bridge.md`
3. 若项目计数变化，更新总状态文档
4. 记录验证证据

## 包含技能

- `ultra-orchestrator`：主编排控制平面
- `openspec-ultra-bridge`：OpenSpec 与 Ultra 桥接
- `clarify-and-intake`：需求澄清与归一化
- `decision-complete-planner`：规划与拆解
- `dispatch-and-track`：工作包派发与追踪
- `code-review`：工程质量审查
- `spec-review`：规格一致性审查
- `qa-verify`：QA 验证门禁
- `risk-vetter`：高风险动作前风险评估
- `safety-guard`：安全护栏与约束
- `deliver-and-retro`：交付汇总与复盘
- `autoplan`：快速规划流水线
- `codex_ultra_orchestration`：白皮书、示例、运行产物

## 在 Cursor 中使用

### 全局安装（推荐）

将技能目录复制到：

- `C:\Users\<你>\.cursor\skills\`

示例：

```powershell
Copy-Item -Recurse -Force .\skills\ultra-orchestrator C:\Users\<你>\.cursor\skills\ultra-orchestrator
```

复制后重启 Cursor 或刷新 Agent 上下文。

### 源码与发布流程

1. 在本仓库更新技能源码
2. 在真实项目中验证
3. 提交并打 tag
4. 同步发布版本到全局技能目录
