# OpenSpec × Ultra-Orchestrator 融合架构白皮书

## 1. 执行摘要

这份文档定义了 OpenSpec 与 Ultra-Orchestrator 的融合架构。融合的目标不是构建一个“更大的单体系统”，而是将两套体系按职责分层：

- OpenSpec 负责规格层（spec layer）
- Ultra-Orchestrator 负责控制层（control plane）
- Git Worktree 负责并行变更的物理隔离
- Automation 负责脚本执行与自动化钩子

这种架构适合中大型工程任务，尤其适合具有以下特征的场景：

- 需要 spec-first 工作流
- 需要多角色协作
- 需要 review / QA / archive 闭环
- 需要并行变更但又必须控制写入风险

融合之后的核心理念可以概括为一句话：

> 让 OpenSpec 管“规格资产”，让 Ultra-Orchestrator 管“执行编排”，让 Worktree 管“并行隔离”，让 Automation 管“机器化动作”。

## 2. 背景与问题

### 2.1 仅有 OpenSpec 的局限

仅使用 OpenSpec 时，系统能够很好地管理：

- proposal
- design
- tasks
- archive

但它本身并不自然解决以下问题：

- 多阶段 state machine 如何流转
- Review 和 QA 失败时如何打回
- 并行变更如何做 write lock 管理
- 外部工具如何 risk vetting
- 运行过程如何留下完整证据链

### 2.2 仅有 Ultra-Orchestrator 的局限

仅使用 Ultra-Orchestrator 时，系统能够很好地管理：

- 角色与阶段
- state machine feedback loops
- risk gates
- review / QA
- orchestration log / vetter report

但它本身不提供 repo 内的长期 spec source-of-truth，也不提供 change archive 的原生资产归档体系。

### 2.3 因此需要融合

融合的意义在于：

- 用 OpenSpec 保证 spec 和 change lifecycle 的长期稳定
- 用 Ultra-Orchestrator 保证执行阶段的结构化、可回滚、可审计
- 用 Git Worktree 保证并行变更的物理隔离
- 用 Automation 将上述约定变成机器可执行动作

## 3. 架构定位

### 3.1 四层架构

推荐的融合结构为四层：

1. Git Worktree Layer
2. OpenSpec Layer
3. Ultra-Orchestrator Layer
4. Automation Layer

### 3.2 Git Worktree Layer

负责：

- 为每个 change 提供独立工作副本
- 为并行变更提供物理隔离
- 降低分支切换成本与写冲突风险

### 3.3 OpenSpec Layer

负责：

- proposal
- design
- tasks
- spec delta
- archive

它是 spec source-of-truth。

### 3.4 Ultra-Orchestrator Layer

负责：

- Intake
- Plan
- Dispatch
- Execute
- Review
- QA
- Deliver
- Retro

它是 orchestration source-of-truth。

### 3.5 Automation Layer

负责：

- bridge scripts
- run initialization
- validation scripts
- archive gates
- later event-loop hooks

## 4. opsx 命令族与 Ultra 阶段的映射

### 4.1 `/opsx:explore`

映射到 Ultra 的 `Intake`。

作用：

- 理解背景
- 搜索 repo 现状
- 提取 constraints / assumptions / risks
- 判断是否需要开启新 change

### 4.2 `/opsx:new`

映射到 OpenSpec change creation + Ultra `Plan` 的起点。

作用：

- 创建 change-id
- 初始化 proposal / design / tasks
- 为 orchestration ledger 创建 run shell

### 4.3 `/opsx:ff`

建议定位为 fast-forward spec framing。

作用：

- 从 explore 结果快速生成 proposal / design / tasks skeleton
- 补齐 acceptance checks
- 把 spec 从“可讨论”推进到“可 apply”状态

### 4.4 `/opsx:apply`

映射到 Ultra 的 `Dispatch + Execute`。

作用：

- 从 OpenSpec tasks 生成 `WorkPackage`
- 按 role 派发任务
- 在 worktree 中执行变更
- 受 DAG, write lock, max retries 约束

### 4.5 `/opsx:verify`

映射到 Ultra 的 `Review + QA`。

作用：

- spec consistency review
- engineering review
- scenario verification
- regression verification
- 根据 failure context 决定打回到 apply / ff / new

### 4.6 `/opsx:archive`

映射到 `Deliver -> Archive -> Retro`。

作用：

- 只在 review / QA 通过后允许归档
- 把 approved change 并入长期 spec source-of-truth
- 标记 run 为 terminal

## 5. 状态机闭环

高层线路是：

- `explore -> new -> ff -> apply -> verify -> archive`

但这是有回滚的 state machine，不是线性瀑布流。

### 5.1 verify -> apply

当 implementation 偏离 spec、review 不通过、或 QA 发现局部行为错误时，返回 apply。

### 5.2 verify -> ff

当 change boundary 仍成立，但 spec 或 tasks 不足以支撑执行时，返回 ff。

### 5.3 verify -> new

当发现 change boundary 判断错误、拆分粒度错误或需要重建 change 时，返回 new。

这与 Ultra 已有的反馈流是一致的：

- `Review -> Execute`
- `QA -> Execute`
- `QA -> Plan`

## 6. 桥接对象模型

### 6.1 OpenSpec Change -> TaskManifest

推荐映射如下：

- `change-id` -> `TaskManifest.id`
- proposal summary -> `goal`
- design constraints -> `constraints`
- task dependencies -> `dependencies`
- acceptance criteria -> `success_criteria`
- affected areas -> `owned_paths`
- implementation intent -> `expected_outputs`

### 6.2 OpenSpec Task -> WorkPackage

推荐映射如下：

- task item -> `scope`
- role hint -> `role`
- task target -> `owned_paths`
- verification checklist -> `acceptance_checks`

### 6.3 AgentResult -> OpenSpec Feedback

Ultra 的 `AgentResult` 不应覆盖 OpenSpec artifacts，而应成为 OpenSpec 的反馈层：

- `evidence` 证明任务完成
- `risks` 提醒 design / tasks 补充
- `failure_context` 用于生成 spec 修正建议

### 6.4 RunOutput -> Archive Gate

只有在以下条件满足时才允许 archive：

- review approved
- QA passed 或已显式接受残余风险
- risk vetter 未阻断
- final deliverable 可交付

## 7. 对现有 Ultra skill 体系的影响

现有 skill 不需推翻，依然应保留：

- `clarify-and-intake`
- `decision-complete-planner`
- `dispatch-and-track`
- `spec-review`
- `code-review`
- `qa-verify`
- `deliver-and-retro`
- `risk-vetter`
- `safety-guard`
- `autoplan`

需新增的是 bridge 层，而不是換掉原有系统。

## 8. 建议新增的 skill

### 8.1 `openspec-ultra-bridge`

这个 skill 应负责：

- 读取 OpenSpec change artifacts
- 生成 `TaskManifest`
- 生成 `WorkPackage`
- 建立 `change-id <-> task-id` 映射
- 把 review / QA / failure context 转为 OpenSpec 更新建议

### 8.2 `openspec-archive-gate`

可以在 bridge skill 之后再增加这个轻量 gate，负责：

- 读取 `RunOutput`
- 判断是否允许 archive
- 拒绝未经验证的变更归档

## 9. 实施路线

### Phase 1

先做文档与协议层融合：

- 明确 opsx 命令与 Ultra 阶段映射
- 明确 change-id / task-id 映射
- 明确 archive gate 通行条件

### Phase 2

实装 `openspec-ultra-bridge` skill。

### Phase 3

把 worktree metadata、active write locks、run mapping 接入 ledger。

### Phase 4

再接 archive gate 和自动化 hooks。

## 10. 当前阶段的最佳策略

当前最推荐的路径是：

- 先做 bridge，不做系统重写
- 先做 protocol mapping，不做 platform replacement
- 先做 pilot，不做过度自动化

也就是说，现阶段最好的组合是：

**OpenSpec 做 spec layer，Ultra-Orchestrator 做 control plane，Git Worktree 做 parallel isolation，Automation 做 execution glue。**

## 11. 结语

这种融合架构的最大价值是，它能把 spec-first 从“写 spec 文档”提升为“可执行、可审计、可回滚的工程编排体系”。

如果这一融合线路跑通，它会让“规格驱动开发”不再只是一种文档习惯，而是一套真正可落地的 engineering control system。
