# Ultra Orchestration Skills

中文说明见下方 **[中文](#中文)**。

A curated skill suite for running software delivery with a dual-plane model:

- **OpenSpec** as the specification plane (`Program -> Milestone -> Change -> Slice`)
- **Ultra-Orchestrator** as the execution plane (`Intake -> Plan -> Dispatch -> Execute -> Review -> QA -> Deliver -> Retro`)

This repository stores reusable skill source code for the orchestration stack.

## Repository Structure

```text
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
```

## Included Skills

- `ultra-orchestrator` — Core control-plane orchestration skill
- `openspec-ultra-bridge` — OpenSpec ↔ Ultra artifact bridge
- `clarify-and-intake` — Requirement intake normalization
- `decision-complete-planner` — Planning and decomposition
- `dispatch-and-track` — Work package assignment and tracking
- `code-review` — Engineering quality review
- `spec-review` — Specification consistency review
- `qa-verify` — Verification and QA gate execution
- `risk-vetter` — Risk assessment before high-impact actions
- `safety-guard` — Safety policies and guardrails
- `deliver-and-retro` — Delivery summaries and retrospectives
- `autoplan` — Fast planning pipeline mode
- `codex_ultra_orchestration` — Program docs, examples, run artifacts

## Workflow Model

Use this fixed phase order for non-trivial work:

1. Intake
2. Plan
3. Dispatch
4. Execute
5. Review
6. QA
7. Deliver
8. Retro

Feedback loops are allowed when needed:

- `Review -> Execute`
- `QA -> Execute`
- `QA -> Plan`

## How to Use in Cursor

### Global installation (recommended)

Copy each skill folder under your Cursor global skills directory:

- Windows: `C:\Users\<you>\.cursor\skills\`

Example:

```powershell
Copy-Item -Recurse -Force .\skills\ultra-orchestrator C:\Users\<you>\.cursor\skills\ultra-orchestrator
```

After copying, restart Cursor or refresh the agent context so the skill list updates.

### Project-local source of truth

Keep this repository as the source code and documentation for your skills, and synchronize to global skills when releasing updates.

## Design Principles

- Keep OpenSpec and execution ledgers synchronized.
- Use `change` for spec/progress accounting and `slice` for implementation progress.
- Advance slice status only with verification evidence.
- Prefer bounded owned-path slices over broad milestone-wide coding.

## Versioning Guidance

Recommended release process:

1. Update skill source in this repository.
2. Validate workflows on a real project.
3. Tag a release (for example, `v1.0.0`).
4. Sync released skills to global Cursor skills directory.

---

## 中文

这是一个用于工程交付编排的技能仓库，采用“双平面协作”模型：

- **OpenSpec** 负责规格平面（`Program -> Milestone -> Change -> Slice`）
- **Ultra-Orchestrator** 负责执行平面（`Intake -> Plan -> Dispatch -> Execute -> Review -> QA -> Deliver -> Retro`）

本仓库用于保存这套技能体系的可复用源码。

## 目录结构

```text
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
```

## 已包含技能

- `ultra-orchestrator`：主编排控制平面
- `openspec-ultra-bridge`：OpenSpec 与 Ultra 的桥接
- `clarify-and-intake`：需求澄清与 intake 归一化
- `decision-complete-planner`：任务规划与分解
- `dispatch-and-track`：工作包派发与跟踪
- `code-review`：工程质量审查
- `spec-review`：规格一致性审查
- `qa-verify`：QA 验证与门禁执行
- `risk-vetter`：高风险动作前风险评估
- `safety-guard`：安全策略与防护栏
- `deliver-and-retro`：交付汇总与复盘
- `autoplan`：快速规划流水线模式
- `codex_ultra_orchestration`：程序文档、示例与运行产物

## 执行流程

中大型任务固定使用以下阶段顺序：

1. Intake
2. Plan
3. Dispatch
4. Execute
5. Review
6. QA
7. Deliver
8. Retro

允许按证据触发回环：

- `Review -> Execute`
- `QA -> Execute`
- `QA -> Plan`

## 在 Cursor 中使用

### 全局安装（推荐）

将每个技能目录复制到 Cursor 全局技能目录：

- Windows：`C:\Users\<你>\.cursor\skills\`

示例：

```powershell
Copy-Item -Recurse -Force .\skills\ultra-orchestrator C:\Users\<你>\.cursor\skills\ultra-orchestrator
```

复制后，建议重启 Cursor 或刷新 Agent 上下文，让技能列表重新索引。

### 项目内源码管理

建议把本仓库作为技能源码与文档的唯一来源；发布时再同步到全局目录。

## 设计原则

- OpenSpec 账本与执行账本必须同步。
- `change` 用于规格/进度核算，`slice` 用于实现进度核算。
- slice 状态推进必须有验证证据支撑。
- 优先采用“边界清晰的小切片”而非“大里程碑整包开发”。

## 版本发布建议

1. 在本仓库更新技能源码。
2. 在真实项目中验证流程。
3. 打版本标签（例如 `v1.0.0`）。
4. 将发布版本同步到 Cursor 全局技能目录。
