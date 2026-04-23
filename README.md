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

The repository ships two skill tracks:

- [`skills/`](./skills/) is the stable skill suite
- [`skills-vnext/`](./skills-vnext/) is the vNext preview suite

Backstory and whitepaper page:

- [GitHub Pages / docs.html](https://keithhegit.github.io/ultra-orchestration/docs.html)

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

The vNext suite adds:

- design-first clarification and explicit approval gates
- OpenSpec-backed durable specification artifacts
- finite-state-machine loopbacks instead of fragile linear waterfall execution
- artifact-driven handoff instead of full chat-history inheritance
- DAG plus write-lock rules for safe parallelism
- host-driven ledger ownership

## Skills Library

### Stable Core Suite

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

Use this track when you want the current stable contract.

### vNext Preview Suite

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

Use this track when you want to pilot the stricter next-generation protocol.

## Version Evolution Log

### Stable To vNext Mapping

| vNext skill | Stable skill relationship | Replacement type | Main upgrade |
|---|---|---|---|
| `ultra-vnext-core` | `ultra-orchestrator` | Partial replacement plus shared kernel | Extracts contracts, FSM loopbacks, context firewall, safe parallelism, and host-driven ledger rules into the shared core. |
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

### 3. Install vNext Preview Skills

For a pilot, copy the full vNext suite into a project-level skill directory:

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills-vnext\* $TARGET
```

If you only want to test a few skills, copy selected folders:

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills-vnext\ultra-vnext-core "$TARGET\ultra-vnext-core"
Copy-Item -Recurse -Force .\skills-vnext\ultra-planning "$TARGET\ultra-planning"
Copy-Item -Recurse -Force .\skills-vnext\ultra-delivery "$TARGET\ultra-delivery"
```

If you do not want to install yet, ask the agent to read repository-relative
skill files. Replace `<REPO_ROOT>` with the folder where you cloned this
repository.

Example:

```text
Please read and use:
<REPO_ROOT>\skills-vnext\ultra-vnext-core\SKILL.md
<REPO_ROOT>\skills-vnext\ultra-brainstorming\SKILL.md
<REPO_ROOT>\skills-vnext\ultra-planning\SKILL.md
```

## Starting The vNext Workflow

### For A New Feature

Use this starting prompt:

```text
Use $ultra-vnext-core, $ultra-brainstorming, $ultra-planning, $ultra-risk-vetting,
$ultra-execution-control, $ultra-review, $ultra-qa, and $ultra-delivery.
Start with design-first clarification, produce a TaskManifest and WorkPackages,
then execute only after reviewable acceptance checks exist.
```

### For An OpenSpec-Based Project

Use this starting prompt:

```text
Use $openspec-ultra-bridge-v2 with $ultra-vnext-core.
Treat OpenSpec as the specification layer and Ultra as the execution control plane.
Bridge one change into TaskManifest and WorkPackages, then continue through review,
QA, delivery, and retro.
```

### For A Bug Fix

Use this starting prompt:

```text
Use $ultra-vnext-core, $ultra-planning, $ultra-risk-vetting, $ultra-review,
$ultra-qa, and $ultra-delivery. Build a minimal investigation plan, identify
the regression surface, fix only the approved owned paths, and require QA
evidence before delivery.
```

## Helper Scripts

Initialize a vNext run directory:

```powershell
python .\skills-vnext\ultra-vnext-core\scripts\new_run.py .\runs-vnext --run-id run-001
```

Validate core JSON artifacts:

```powershell
python .\skills-vnext\ultra-vnext-core\scripts\validate_contracts.py .\runs-vnext\run-001\ledger.json --kind executionledger
```

Bridge an OpenSpec change:

```powershell
python .\skills-vnext\openspec-ultra-bridge-v2\scripts\bridge_change.py .\openspec\changes\<change-id> .\runs-vnext\bridge-output
```

Chinese pilot guide:

- [docs/ultra-vnext-pilot-guide-CN.md](./docs/ultra-vnext-pilot-guide-CN.md)

## How To Evaluate Success

A vNext run is considered healthy when:

- the agent does not jump directly from vague request to coding
- the design or OpenSpec change is explicit before implementation
- `TaskManifest` and `WorkPackage` artifacts can be inspected without chat history
- parallel execution only happens for disjoint owned paths
- risk decisions appear in `vetter_report`
- review produces accept/reject/reroute decisions with evidence
- QA states static or dynamic evidence honestly
- delivery includes `final_deliverable`, `orchestration_log`, and `vetter_report`
- residual risks and follow-ups are separated from completed work

## Repository Layout

```text
.github/
  ISSUE_TEMPLATE/
  workflows/
skills/
  stable core skills
skills-vnext/
  vNext preview skills
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

仓库提供两组技能套件：

- [`skills/`](./skills/) 是稳定技能套件
- [`skills-vnext/`](./skills-vnext/) 是 vNext 预览技能套件

文档与白皮书：

- [GitHub Pages / docs.html](https://keithhegit.github.io/ultra-orchestration/docs.html)

## 它如何工作

Ultra Orchestration 通过工程化生命周期管理提升 AI 辅助交付的可控性和可审计性：

1. 澄清目标、边界和成功标准
2. 把请求变成可审查的设计或规格
3. 生成 decision-complete 任务图
4. 派发边界明确的工作包
5. 做规格一致性和工程质量审查
6. 通过 QA 验证行为
7. 交付结果、证据、风险和复盘

vNext 预览套件提供以下增强能力：

- 设计先行的澄清流程与显式审批门
- 基于 OpenSpec 的持久规格资产
- 用有限状态机闭环替代单向执行流程
- 用 artifact handoff 替代全文上下文传递
- 用 DAG + 写锁定义安全并发
- 用 host-driven ledger 管理执行状态

## 技能库

### 稳定主线

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

适合需要当前稳定交付协议的场景。

### vNext 预览套件

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

适合在真实项目中试用更严格的下一代编排协议。

## 版本迭代日志

### 稳定版到 vNext 对应关系

| vNext 技能 | 稳定版对应技能 | 迁移关系 | 主要变化 |
|---|---|---|---|
| `ultra-vnext-core` | `ultra-orchestrator` | 共享内核 | 将 contracts、状态机闭环、context firewall、安全并发和 host-driven ledger 抽象为公共运行规则。 |
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

### 3. 安装 vNext 预览技能

如果要做 pilot，可以把整套 vNext 复制到项目级技能目录：

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills-vnext\* $TARGET
```

如果只想试用其中几个技能，也可以只复制选定目录：

```powershell
$TARGET = "<PROJECT_ROOT>\.agents\skills"
New-Item -ItemType Directory -Force $TARGET
Copy-Item -Recurse -Force .\skills-vnext\ultra-vnext-core "$TARGET\ultra-vnext-core"
Copy-Item -Recurse -Force .\skills-vnext\ultra-planning "$TARGET\ultra-planning"
Copy-Item -Recurse -Force .\skills-vnext\ultra-delivery "$TARGET\ultra-delivery"
```

如果暂时不想安装，可以让 agent 直接读取仓库内的技能文件。请把 `<REPO_ROOT>` 替换为你本地克隆本仓库的位置。

示例：

```text
请读取并使用：
<REPO_ROOT>\skills-vnext\ultra-vnext-core\SKILL.md
<REPO_ROOT>\skills-vnext\ultra-brainstorming\SKILL.md
<REPO_ROOT>\skills-vnext\ultra-planning\SKILL.md
```

## 启动 vNext 工作流

### 新功能开发

推荐启动语：

```text
请使用 $ultra-vnext-core、$ultra-brainstorming、$ultra-planning、
$ultra-risk-vetting、$ultra-execution-control、$ultra-review、$ultra-qa、
$ultra-delivery。先做 design-first 澄清，产出 TaskManifest 和 WorkPackage，
只有在 acceptance checks 可审查后才进入实现。
```

### OpenSpec 项目

推荐启动语：

```text
请使用 $openspec-ultra-bridge-v2 和 $ultra-vnext-core。
把 OpenSpec 当作规格层，把 Ultra 当作执行控制平面。
先桥接一个 change 到 TaskManifest 和 WorkPackage，然后继续 review、QA、delivery 和 retro。
```

### Bug 修复

推荐启动语：

```text
请使用 $ultra-vnext-core、$ultra-planning、$ultra-risk-vetting、
$ultra-review、$ultra-qa 和 $ultra-delivery。先建立最小调查计划，
识别回归面，只修改批准的 owned paths，并在交付前提供 QA 证据。
```

## 辅助脚本

初始化 vNext run 目录：

```powershell
python .\skills-vnext\ultra-vnext-core\scripts\new_run.py .\runs-vnext --run-id run-001
```

校验核心 JSON 工件：

```powershell
python .\skills-vnext\ultra-vnext-core\scripts\validate_contracts.py .\runs-vnext\run-001\ledger.json --kind executionledger
```

桥接 OpenSpec change：

```powershell
python .\skills-vnext\openspec-ultra-bridge-v2\scripts\bridge_change.py .\openspec\changes\<change-id> .\runs-vnext\bridge-output
```

中文 pilot 指南：

- [docs/ultra-vnext-pilot-guide-CN.md](./docs/ultra-vnext-pilot-guide-CN.md)

## 如何评估技能运行成功

一次 vNext 运行可以认为健康，当它满足：

- agent 没有从模糊请求直接跳到编码
- 实现前存在明确 design 或 OpenSpec change
- `TaskManifest` 和 `WorkPackage` 不依赖聊天历史也能被理解
- 只有 owned paths 不重叠时才并行
- `vetter_report` 里有风险决策
- review 明确输出 accept / reject / reroute 和证据
- QA 如实区分 static evidence 与 dynamic evidence
- delivery 包含 `final_deliverable`、`orchestration_log` 和 `vetter_report`
- 残余风险与 follow-up 没有混进“已完成”结论

## 仓库结构

```text
.github/
  ISSUE_TEMPLATE/
  workflows/
skills/
  stable core skills
skills-vnext/
  vNext preview skills
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
