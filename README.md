# Ultra Orchestration Skills

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![Repo Status](https://img.shields.io/badge/status-active-success)](#)
[![Method](https://img.shields.io/badge/method-OpenSpec%20%2B%20Ultra-informational)](#methodology-core)

[English](#english) | [中文](#中文)

## English

Ultra Orchestration is an open-source skill repository for disciplined
AI-assisted software delivery. It provides a two-plane method for turning
ambiguous engineering requests into structured specifications, bounded
execution packages, review evidence, QA results, and auditable delivery
records.

- **OpenSpec specification plane** for long-lived program, milestone, change,
  and archive assets
- **Ultra-Orchestrator execution plane** for intake, planning, dispatch,
  execution, review, QA, delivery, risk control, and retro

The repository ships a mainline skill suite and a compatibility preview suite:

- [`skills/`](./skills/) is the mainline suite. Start here.
- [`skills-vnext/`](./skills-vnext/) keeps vNext compatibility aliases and
  preview internals.

Mainline entry points:

- `ultra-orchestrator` is the default public entry point.
- `ultra-vnext-core` remains a compatibility alias.
- `ultra-orchestrator-legacy` preserves the older lightweight workflow.

Backstory and whitepaper page:

- [GitHub Pages / docs.html](https://keithhegit.github.io/ultra-orchestration/docs.html)

## Installation

### 1. Get The Repository

Recommended:

```bash
git clone https://github.com/keithhegit/ultra-orchestration.git
cd ultra-orchestration
```

You can also download a GitHub release archive, but the examples below assume a
normal cloned repository.

### 2. Install Stable Skills

Copy folders from [`skills/`](./skills/) into your agent's global or
project-level skill directory.

Common targets:

| Agent | Project-level target | User-level target | Notes |
|---|---|---|---|
| Codex | `<PROJECT_ROOT>\.agents\skills` | `%USERPROFILE%\.codex\skills` | Use project-level install when sharing skills with a repo. |
| Cursor | `<PROJECT_ROOT>\.agents\skills` or Cursor's configured skill path | `%USERPROFILE%\.cursor\skills` | Cursor setups vary by version and plugin support. |
| Claude Code | `<PROJECT_ROOT>\.claude\skills` | `%USERPROFILE%\.claude\skills` | Claude Code discovers project and user skills. |
| OpenCode | `<PROJECT_ROOT>\.opencode\skills` | platform-specific home config | OpenCode also discovers compatible `.claude\skills` and `.agents\skills` folders. |
| OpenClaw, Hermes, other IDE agents | the agent's documented skills directory | the agent's documented user skills directory | If the agent supports `SKILL.md` folders, copy each skill folder as-is. |

Platform references:

- [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode skills](https://opencode.ai/docs/skills)

Generic project-level example:

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator "$TARGET\ultra-orchestrator"
Copy-Item -Recurse -Force .\skills\openspec-ultra-bridge "$TARGET\openspec-ultra-bridge"
```

Claude Code project-level example:

```powershell
$TARGET = "<PROJECT_ROOT>\.claude\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator "$TARGET\ultra-orchestrator"
Copy-Item -Recurse -Force .\skills\openspec-ultra-bridge "$TARGET\openspec-ultra-bridge"
```

OpenCode project-level example:

```powershell
$TARGET = "<PROJECT_ROOT>\.opencode\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator "$TARGET\ultra-orchestrator"
Copy-Item -Recurse -Force .\skills\openspec-ultra-bridge "$TARGET\openspec-ultra-bridge"
```

Restart or refresh your agent after copying skills.

### 3. Optional: Legacy And vNext Compatibility

New users should install and invoke `ultra-orchestrator`. The compatibility
folders are only for older prompts or migration testing.

Legacy lightweight workflow:

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator-legacy "$TARGET\ultra-orchestrator-legacy"
```

Older vNext prompt compatibility:

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills-vnext\ultra-vnext-core "$TARGET\ultra-vnext-core"
```

Do not start new projects from the compatibility aliases unless you are testing
backward compatibility. Start new work with `$ultra-orchestrator`.

## Starting The Mainline Workflow

`ultra-orchestrator` is the default public entry point. Users should not need
to name every subskill. The orchestrator chooses run mode, prefers
`STRICT_OPENSPEC` for development work, and routes to the right sequence:
OpenSpec bootstrap or bridge, planning, risk vetting, execution control,
review, QA, and delivery.

### General Startup

```text
$ultra-orchestrator <task description>
```

Example:

```text
$ultra-orchestrator Build a workspace settings page for model defaults.
```

### OpenSpec Startup

```text
$ultra-orchestrator OpenSpec change <change-id or path>: <task description>
```

Example:

```text
$ultra-orchestrator OpenSpec change workspace-model-defaults: implement the first slice.
```

### Bug Fix Startup

```text
$ultra-orchestrator bugfix: <symptom or failing behavior>
```

Example:

```text
$ultra-orchestrator bugfix: command execution hangs after approval is granted.
```

If your agent client exposes slash aliases, use `/ultra-orchestrator` with the
same forms. `$ultra-vnext-core` remains available as a compatibility alias.

## How It Works

Ultra Orchestration organizes AI-assisted work through a structured engineering
lifecycle:

1. clarify what is being built
2. turn the request into a reviewable design or spec
3. create a decision-complete task graph
4. dispatch bounded work packages
5. review against spec and engineering quality
6. verify behavior through QA
7. package the deliverable, evidence, risks, and retro

The mainline `ultra-orchestrator` now includes the vNext strict control plane:

- design-first clarification and explicit approval gates
- OpenSpec-backed durable specification artifacts
- finite-state-machine loopbacks instead of fragile linear waterfall execution
- artifact-driven handoff instead of full chat-history inheritance
- DAG plus write-lock rules for safe parallelism
- host-driven ledger ownership
- run mode selection: `LIGHT`, `STANDARD`, `STRICT`, `STRICT_OPENSPEC`
- OpenSpec-first defaults for development work
- machine-checkable JSON artifacts and contract validation

The default experience is:

1. start with `ultra-orchestrator`
2. let the entry point choose run mode and route subskills
3. prefer `STRICT_OPENSPEC` for development work
4. require ledger-backed planning before controlled dispatch
5. proceed through execution, review, QA, risk evidence, and delivery

## Skills Library

### Stable Core Suite

Under [`skills/`](./skills/):

- `ultra-orchestrator`
- `ultra-orchestrator-legacy`
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

Use `ultra-orchestrator` for new work. Use `ultra-orchestrator-legacy` only
when you need the original lightweight staged flow.

### vNext Compatibility And Internal Protocols

Under [`skills-vnext/`](./skills-vnext/):

- `ultra-vnext-core`
- `ultra-brainstorming`
- `ultra-planning`
- `ultra-execution-control`
- `ultra-review`
- `ultra-qa`
- `ultra-risk-vetting`
- `ultra-delivery`
- `openspec-ultra-bridge-v2`

Use this track only when you need vNext compatibility names or internal
protocol references. New projects should start from `ultra-orchestrator`.

## Version Evolution Log

### Mainline Merge 2026-04-24

- Promoted the vNext strict protocol into `skills/ultra-orchestrator`.
- Preserved the old stable orchestrator as `skills/ultra-orchestrator-legacy`.
- Kept `skills-vnext/ultra-vnext-core` as a compatibility alias.
- Made development tasks prefer `STRICT_OPENSPEC` by default.
- Added mandatory `control_surface_used` reporting for strict runs.

### Legacy To Mainline Mapping

| Mainline / vNext skill | Legacy relationship | Migration type | Main upgrade |
|---|---|---|---|
| `ultra-orchestrator` | `ultra-orchestrator-legacy` | Mainline replacement | Adds run mode selection, strict OpenSpec preference, ledger-backed execution, JSON artifacts, contract validation, slice DAGs, and control-surface reporting. |
| `ultra-vnext-core` | `ultra-orchestrator` | Compatibility alias | Keeps existing vNext invocations working while following the mainline protocol. |
| `ultra-brainstorming` | `clarify-and-intake` + early `autoplan` | Enhanced replacement | Adds design-first discovery, hard gates, one-question-at-a-time clarification, approach comparison, and approval before planning or coding. |
| `ultra-planning` | `decision-complete-planner` | Direct vNext replacement | Keeps task graph planning but strengthens DAG dependencies, owned paths, acceptance checks, retry assumptions, and serial/parallel boundaries. |
| `ultra-execution-control` | `dispatch-and-track` + part of `safety-guard` | Enhanced integration | Combines dispatch, write locks, bounded retries, blockers, freeze/careful/guard behavior, and host-driven ledger updates. |
| `ultra-review` | `spec-review` + `code-review` | Merged replacement | Keeps spec fidelity and engineering quality as two internal gates, then returns accept, reject-to-execute, or reroute-to-plan. |
| `ultra-qa` | `qa-verify` | Direct vNext replacement | Makes static QA and dynamic QA explicit, with scenario coverage, evidence, pass/fail, and loopback routing. |
| `ultra-risk-vetting` | `risk-vetter` + approval-facing part of `safety-guard` | Direct vNext replacement | Defines LOW/MEDIUM/HIGH/EXTREME thresholds, approval requirements, guardrail mapping, and vetter report output. |
| `ultra-delivery` | `deliver-and-retro` | Direct vNext replacement | Packages `final_deliverable`, `orchestration_log`, `vetter_report`, QA evidence, residual risks, follow-ups, and retro. |
| `openspec-ultra-bridge-v2` | `openspec-ultra-bridge` | Enhanced replacement | Keeps OpenSpec as the spec layer and Ultra as the control plane, with bridge scripts that materialize TaskManifest and WorkPackage artifacts. |

### vNext 2026-04-23

- Added `ultra-risk-vetting`
- Added `ultra-delivery`
- Updated README with stable-to-vNext mapping
- Added clearer installation, startup, and success-evaluation guidance

## Methodology Core

### 1. Two-plane Collaboration

- **OpenSpec** owns long-lived specification assets and status accounting
- **Ultra-Orchestrator** owns execution control, quality gates, delivery
  evidence, and risk decisions

Neither replaces the other. They stay synchronized.

### 2. Delivery Structure

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

### 3. Progress Accounting

- `Change` is the specification and planning unit
- `Slice` is the implementation and verification unit

Do not run milestone-wide engineering without change and slice decomposition.

### 4. Slice Status Discipline

Canonical slice states:

- `slice_0_not_opened`
- `slice_0_spec_ready`
- `slice_1_completed`
- `slice_2_in_progress`
- `slice_3_qa_pending`
- `slice_4_done`

Advance slice status only with verification evidence.

### 5. Bridge Discipline

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

## How Routing And Planning Work

`ultra-orchestrator` is the primary router. It should classify run mode first,
then load only the required subskills.

Typical routes:

- development, feature, bugfix, pilot, or multi-file implementation
  - `ultra-orchestrator -> STRICT_OPENSPEC -> openspec-ultra-bridge -> decision-complete-planner -> dispatch-and-track -> review -> qa-verify -> deliver-and-retro`
- existing OpenSpec change
  - `ultra-orchestrator -> openspec-ultra-bridge -> decision-complete-planner -> dispatch-and-track -> review -> qa-verify -> deliver-and-retro`
- review-only or QA-only
  - `ultra-orchestrator -> LIGHT -> review/QA -> deliver-and-retro`

For `STRICT` and `STRICT_OPENSPEC`, markdown-only artifacts are not enough. A
run is not execution-ready until it has a ledger, JSON `TaskManifest`, JSON
`WorkPackage` artifacts, owned paths, acceptance checks, dependency order,
retry assumptions, and a contract-validation plan.

## Helper Scripts

Initialize a mainline run directory:

```powershell
python .\skills\ultra-orchestrator\scripts\new_run.py .\runs --run-id run-001 --run-mode STRICT_OPENSPEC
```

Validate core JSON artifacts:

```powershell
python .\skills\ultra-orchestrator\scripts\validate_contracts.py .\runs\run-001\ledger.json --kind executionledger
```

Optional bridge helper for an OpenSpec change:

```powershell
python .\skills-vnext\openspec-ultra-bridge-v2\scripts\bridge_change.py .\openspec\changes\<change-id> .\runs\run-001\bridge-output
```

Chinese pilot guide:

- [docs/ultra-vnext-pilot-guide-CN.md](./docs/ultra-vnext-pilot-guide-CN.md)

## How To Evaluate Success

A mainline Ultra run is considered healthy when:

- the user only needs to invoke `ultra-orchestrator`
- development work defaults to `STRICT_OPENSPEC`
- the run does not silently downgrade to markdown-only orchestration
- OpenSpec change or bootstrap status is explicit before implementation
- `ledger.json`, JSON `TaskManifest`, and JSON `WorkPackage` artifacts exist for strict runs
- contract validation is run or an explicit blocker explains why it could not run
- slice status, owned paths, review gate, and QA gate are clear
- risk decisions appear in `vetter_report`
- delivery includes `final_deliverable`, `orchestration_log`, `vetter_report`, and `control_surface_used`
- skipped control surfaces, residual risks, and follow-ups are separated from completed work

## Repository Layout

```text
.github/
  ISSUE_TEMPLATE/
  workflows/
skills/
  mainline skills and legacy compatibility
skills-vnext/
  vNext compatibility aliases and preview internals
docs/
  ultra-vnext-pilot-guide-CN.md
docs.html
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
```

## Source And Release Workflow

1. update or add skills in this repository
2. validate the workflow in a real project
3. commit and tag a release if needed
4. sync released skills into the target global or workspace skill directory

## Philosophy

- protocol over improvisation
- evidence over claims
- design before implementation
- safe parallelism over accidental concurrency
- durable artifacts over chat memory
- Ultra remains the control plane

## License

This project is licensed under the **Apache License 2.0**.
See [LICENSE](./LICENSE).

---

## 中文

Ultra Orchestration 是一个面向 AI 辅助软件交付的开源技能仓库。它通过标准化规格、任务拆解、执行控制、审查、QA、风险记录和交付证据，帮助 AI 编程代理更稳定地处理复杂工程任务。

项目采用双平面协作模型：

- **OpenSpec 规格平面**：负责长期规格资产、里程碑、变更与归档
- **Ultra-Orchestrator 编排平面**：负责 Intake、Plan、Dispatch、Execute、Review、QA、Deliver、风险控制与 Retro

仓库提供两组技能目录：

- [`skills/`](./skills/) 是主线技能与 legacy 兼容入口
- [`skills-vnext/`](./skills-vnext/) 是 vNext 兼容别名与内部协议参考

主线入口：

- `ultra-orchestrator` 是默认公开入口
- `ultra-vnext-core` 保留为兼容别名
- `ultra-orchestrator-legacy` 保留旧轻量流程

文档与白皮书：

- [GitHub Pages / docs.html](https://keithhegit.github.io/ultra-orchestration/docs.html)

## 安装

### 1. 获取仓库

推荐使用 `git clone`：

```bash
git clone https://github.com/keithhegit/ultra-orchestration.git
cd ultra-orchestration
```

也可以下载 GitHub release 或源码压缩包，但下面的命令默认你已经进入克隆后的仓库目录。

### 2. 安装稳定技能

把 [`skills/`](./skills/) 里的技能目录复制到目标 agent 的全局或项目级技能目录。

常见目标目录：

| Agent | 项目级目录 | 用户级目录 | 说明 |
|---|---|---|---|
| Codex | `<PROJECT_ROOT>\.agents\skills` | `%USERPROFILE%\.codex\skills` | 如果希望技能随项目共享，优先使用项目级目录。 |
| Cursor | `<PROJECT_ROOT>\.agents\skills` 或 Cursor 当前配置的 skills 目录 | `%USERPROFILE%\.cursor\skills` | Cursor 的插件和技能支持会随版本与配置变化。 |
| Claude Code | `<PROJECT_ROOT>\.claude\skills` | `%USERPROFILE%\.claude\skills` | Claude Code 支持项目级和用户级 skills。 |
| OpenCode | `<PROJECT_ROOT>\.opencode\skills` | 按 OpenCode 当前平台配置 | OpenCode 也会发现兼容的 `.claude\skills` 和 `.agents\skills`。 |
| OpenClaw、Hermes、其他 IDE Agent | 对应工具文档中的 skills 目录 | 对应工具文档中的用户级 skills 目录 | 如果工具支持 `SKILL.md` 文件夹结构，保持目录原样复制即可。 |

平台参考：

- [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode skills](https://opencode.ai/docs/skills)

通用项目级示例：

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator "$TARGET\ultra-orchestrator"
Copy-Item -Recurse -Force .\skills\openspec-ultra-bridge "$TARGET\openspec-ultra-bridge"
```

Claude Code 项目级示例：

```powershell
$TARGET = "<PROJECT_ROOT>\.claude\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator "$TARGET\ultra-orchestrator"
Copy-Item -Recurse -Force .\skills\openspec-ultra-bridge "$TARGET\openspec-ultra-bridge"
```

OpenCode 项目级示例：

```powershell
$TARGET = "<PROJECT_ROOT>\.opencode\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator "$TARGET\ultra-orchestrator"
Copy-Item -Recurse -Force .\skills\openspec-ultra-bridge "$TARGET\openspec-ultra-bridge"
```

复制完成后，请重启或刷新对应 agent 的上下文。

### 3. 可选：Legacy 与 vNext 兼容入口

新用户只需要安装并调用 `ultra-orchestrator`。下面两个入口只用于老提示词兼容或迁移测试。

旧轻量流程：

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills\ultra-orchestrator-legacy "$TARGET\ultra-orchestrator-legacy"
```

旧 vNext 提示词兼容：

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills-vnext\ultra-vnext-core "$TARGET\ultra-vnext-core"
```

除非你正在测试兼容性，否则新项目不要从兼容别名启动。新工作默认使用 `$ultra-orchestrator`。

## 启动主线工作流

`ultra-orchestrator` 是默认公开入口。用户不需要手动列出所有子技能；主入口会先判断运行模式，开发任务默认优先 `STRICT_OPENSPEC`，再自动路由到 OpenSpec bootstrap 或 bridge、planning、risk vetting、execution control、review、QA 和 delivery。

### 通用启动

```text
$ultra-orchestrator <任务描述>
```

示例：

```text
$ultra-orchestrator 构建一个工作区模型默认值设置页。
```

### OpenSpec 启动

```text
$ultra-orchestrator OpenSpec change <change-id 或路径>: <任务描述>
```

示例：

```text
$ultra-orchestrator OpenSpec change workspace-model-defaults: 实现第一个 slice。
```

### Bug 修复启动

```text
$ultra-orchestrator bugfix: <异常现象或失败行为>
```

示例：

```text
$ultra-orchestrator bugfix: 审批通过后命令执行卡住。
```

如果你的 agent 客户端提供 slash alias，也可以用 `/ultra-orchestrator` 加同样的参数启动。`ultra-vnext-core` 仍保留为兼容别名。

## 它如何工作

Ultra Orchestration 通过工程化生命周期管理提升 AI 辅助交付的可控性和可审计性：

1. 澄清目标、边界和成功标准
2. 把请求变成可审查的设计或规格
3. 生成 decision-complete 任务图
4. 派发边界明确的工作包
5. 做规格一致性和工程质量审查
6. 通过 QA 验证行为
7. 交付结果、证据、风险和复盘

主线 `ultra-orchestrator` 已合入 vNext strict 控制面：

- 设计先行的澄清流程与显式审批门
- 基于 OpenSpec 的持久规格资产
- 用有限状态机闭环替代单向执行流程
- 用 artifact handoff 替代全文上下文传递
- 用 DAG + 写锁定义安全并发
- 用 host-driven ledger 管理执行状态
- 支持 `LIGHT`、`STANDARD`、`STRICT`、`STRICT_OPENSPEC` 运行模式
- 开发任务默认优先 `STRICT_OPENSPEC`
- 使用机器可校验 JSON 工件和 contract validation

默认使用方式是：

1. 从 `ultra-orchestrator` 启动
2. 由主入口判断运行模式并自动路由
3. 开发任务优先进入 `STRICT_OPENSPEC`
4. 在进入受控 dispatch 前建立 ledger 和 JSON planning artifacts
5. 再进入执行、审查、QA、风险记录和交付

## 技能库

### 稳定主线

位于 [`skills/`](./skills/)：

- `ultra-orchestrator`
- `ultra-orchestrator-legacy`
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

新工作默认使用 `ultra-orchestrator`。只有需要旧轻量流程时才使用
`ultra-orchestrator-legacy`。

### vNext 兼容与内部协议

位于 [`skills-vnext/`](./skills-vnext/)：

- `ultra-vnext-core`
- `ultra-brainstorming`
- `ultra-planning`
- `ultra-execution-control`
- `ultra-review`
- `ultra-qa`
- `ultra-risk-vetting`
- `ultra-delivery`
- `openspec-ultra-bridge-v2`

这组技能保留为兼容入口和内部协议参考。新项目默认从 `ultra-orchestrator` 启动，不需要手动枚举这些子技能。

## 版本迭代日志

### 主线合并后的对应关系

| 当前入口或技能 | 旧版或兼容来源 | 迁移关系 | 主要变化 |
|---|---|---|---|
| `ultra-orchestrator` | `ultra-vnext-core` + 原 `ultra-orchestrator` | 新默认主线 | 将 vNext strict protocol 提升为默认入口，自动判断 `LIGHT / STANDARD / STRICT / STRICT_OPENSPEC`，开发任务优先 strict OpenSpec。 |
| `ultra-orchestrator-legacy` | 原 `ultra-orchestrator` | 兼容保留 | 保留旧轻量阶段化编排，供老项目或非 strict 场景使用。 |
| `ultra-vnext-core` | vNext 预览入口 | 兼容别名 | 继续支持已有 vNext 调用，但推荐新项目改用 `ultra-orchestrator`。 |
| `ultra-brainstorming` | `clarify-and-intake` + `autoplan` 前半段 | 增强版 | 增加 design-first、显式审批门、逐问澄清、方案对比和规划前确认。 |
| `ultra-planning` | `decision-complete-planner` | 直接对应 | 强化 DAG、owned paths、acceptance checks、retry 假设和串并行边界。 |
| `ultra-execution-control` | `dispatch-and-track` + 部分 `safety-guard` | 整合版 | 合并 dispatch、写锁、受限重试、blocker、freeze/careful/guard 和 ledger 更新纪律。 |
| `ultra-review` | `spec-review` + `code-review` | 合并版 | 保留规格一致性和工程质量两层审查，并输出 accept / reject / reroute。 |
| `ultra-qa` | `qa-verify` | 直接对应 | 明确 static QA / dynamic QA 双模式，补充场景覆盖、证据和失败回流。 |
| `ultra-risk-vetting` | `risk-vetter` + `safety-guard` 的审批部分 | 直接对应 | 定义 LOW/MEDIUM/HIGH/EXTREME、审批门槛、护栏映射和 vetter report。 |
| `ultra-delivery` | `deliver-and-retro` | 直接对应 | 统一 final_deliverable、orchestration_log、vetter_report、QA 证据、残余风险和复盘。 |
| `openspec-ultra-bridge-v2` | `openspec-ultra-bridge` | 增强版 | 保持 OpenSpec 为规格层、Ultra 为控制平面，并用脚本生成 TaskManifest 与 WorkPackage 工件。 |

### vNext 2026-04-23

- 新增 `ultra-risk-vetting`
- 新增 `ultra-delivery`
- README 增加稳定版到 vNext 对应表
- README 增加安装、启动和成功评估指南

## 方法论核心

### 1. 双平面协作

- **OpenSpec** 负责长期规格资产与状态核算
- **Ultra-Orchestrator** 负责执行控制、质量门禁、交付证据与风险决策

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

只有存在验证证据时，才推进 slice 状态。

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

## 路由与 Planning 如何协同

`ultra-orchestrator` 是主路由器。它应先判断运行模式，再按需加载最少必要的子技能。

常见路由：

- 开发任务、feature、bugfix、pilot 或多文件实现
  - `ultra-orchestrator -> STRICT_OPENSPEC -> openspec-ultra-bridge -> decision-complete-planner -> dispatch-and-track -> review -> qa-verify -> deliver-and-retro`
- 已有 OpenSpec change
  - `ultra-orchestrator -> openspec-ultra-bridge -> decision-complete-planner -> dispatch-and-track -> review -> qa-verify -> deliver-and-retro`
- review-only 或 QA-only
  - `ultra-orchestrator -> LIGHT -> review/QA -> deliver-and-retro`

对于 `STRICT` 和 `STRICT_OPENSPEC`，Markdown-only 工件不够。只有当运行具备 ledger、JSON `TaskManifest`、JSON `WorkPackage`、owned paths、acceptance checks、依赖顺序、retry 假设和 contract validation 计划后，才算 execution-ready。

## 辅助脚本

初始化主线 run 目录：

```powershell
python .\skills\ultra-orchestrator\scripts\new_run.py .\runs --run-id run-001 --run-mode STRICT_OPENSPEC
```

校验核心 JSON 工件：

```powershell
python .\skills\ultra-orchestrator\scripts\validate_contracts.py .\runs\run-001\ledger.json --kind executionledger
```

可选：桥接 OpenSpec change：

```powershell
python .\skills-vnext\openspec-ultra-bridge-v2\scripts\bridge_change.py .\openspec\changes\<change-id> .\runs\run-001\bridge-output
```

中文 pilot 指南：

- [docs/ultra-vnext-pilot-guide-CN.md](./docs/ultra-vnext-pilot-guide-CN.md)

## 如何评估技能运行成功

一次主线 Ultra 运行可以认为健康，当它满足：

- 用户只需要调用 `ultra-orchestrator`
- 开发任务默认进入 `STRICT_OPENSPEC`
- 运行不会静默降级成 Markdown-only 编排
- 实现前存在明确 OpenSpec change 或 bootstrap 状态
- strict run 具备 `ledger.json`、JSON `TaskManifest` 和 JSON `WorkPackage`
- contract validation 已运行，或有明确 blocker 说明为什么无法运行
- slice status、owned paths、review gate 和 QA gate 明确
- `vetter_report` 里有风险决策
- delivery 包含 `final_deliverable`、`orchestration_log`、`vetter_report` 和 `control_surface_used`
- skipped control surfaces、残余风险和 follow-up 没有混进“已完成”结论

## 仓库结构

```text
.github/
  ISSUE_TEMPLATE/
  workflows/
skills/
  mainline skills and legacy compatibility
skills-vnext/
  vNext compatibility aliases and preview internals
docs/
  ultra-vnext-pilot-guide-CN.md
docs.html
README.md
LICENSE
CONTRIBUTING.md
SECURITY.md
CODE_OF_CONDUCT.md
```

## 源码与发布流程

1. 在本仓库中更新技能
2. 在真实项目中验证
3. 按需要提交并打 tag
4. 将发布版本同步到目标全局或工作空间技能目录

## 哲学

- 协议优先于即兴发挥
- 证据优先于口头结论
- 设计先于实现
- 安全并发优先于偶然并发
- 持久工件优先于聊天记忆
- Ultra 始终是控制平面

## License

本项目使用 **Apache License 2.0**。
详见 [LICENSE](./LICENSE)。
