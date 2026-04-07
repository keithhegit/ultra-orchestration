# OpenSpec × Ultra-Orchestrator 融合设计文档

## 1. 文档目的

这份文档用来说明 OpenSpec 和 Ultra-Orchestrator 在同一工程体系中如何融合。

目标不是让两套体系互相替代，而是形成“规格层 + 控制层”的分层架构。

- OpenSpec 负责 spec artifacts
- Ultra-Orchestrator 负责 state machine, review, QA, risk gate, ledger
- Git Worktree 负责 parallel isolation
- Automation 负责 scripts and execution hooks

## 2. 基于你截图的核心判断

从 workflow tour 的截图可以提炼出一条完整链路：

1. Git Worktree
2. OpenSpec
3. Automation

同时配套的 opsx 命令族包括：

- `/opsx:explore`
- `/opsx:new`
- `/opsx:ff`
- `/opsx:apply`
- `/opsx:verify`
- `/opsx:archive`

这说明该体系的核心不是单个 skill，而是“并行开发 + 规格驱动 + 自动化执行”的完整工程路径。

## 3. 两套系统的最佳定位

### 3.1 OpenSpec 的最佳定位

OpenSpec 最适合担任 repo 内的 spec layer：

- proposal
- design
- tasks
- spec delta
- archive

它负责的是“要做什么”与“规格如何被持续维护”。

### 3.2 Ultra-Orchestrator 的最佳定位

Ultra-Orchestrator 最适合担任 control plane：

- Intake
- Plan
- Dispatch
- Execute
- Review
- QA
- Deliver
- Retro

它负责的是“怎么安全地执行、打回、重试、审核和交付”。

### 3.3 最重要的结论

不建议让 OpenSpec 取代 Ultra，也不建议让 Ultra 取代 OpenSpec。

最佳方案是：

- OpenSpec = source-of-truth for spec
- Ultra = source-of-truth for orchestration state

## 4. opsx 命令与 Ultra 阶段的映射

### `/opsx:explore`

建议映射到 Ultra 的 `Intake`。

作用：

- 理解需求
- 收集上下文
- 提炼 constraints
- 识别 risk signals

### `/opsx:new`

建议映射到 OpenSpec change creation + Ultra `Plan` 起点。

作用：

- 新建 change-id
- 初始化 proposal / design / tasks
- 为 ledger 创建运行索引

### `/opsx:ff`

建议定义为 fast-forward spec framing。

作用：

- 从 explore 结果生成可执行 spec skeleton
- 补齐 acceptance checks
- 让 proposal / design / tasks 进入可 apply 状态

### `/opsx:apply`

建议映射到 Ultra 的 `Dispatch + Execute`。

作用：

- 从 OpenSpec tasks 生成 WorkPackage
- 在 worktree 中实施变更
- 受 DAG, write lock, retry budget 约束

### `/opsx:verify`

建议映射到 Ultra 的 `Review + QA`。

作用：

- spec consistency review
- engineering review
- scenario verification
- regression verification

如果失败，触发状态机回滚。

### `/opsx:archive`

建议映射到 `Deliver -> Archive -> Retro`。

作用：

- 归档已通过变更
- 合入 long-term spec
- 将 ledger 标记为 terminal state

## 5. 融合后的状态机闭环

推荐的高层状态流为：

- `explore -> new -> ff -> apply -> verify -> archive`

但它不是线性瀑布流，而是可回滚状态机：

- `verify -> apply`
  - 当 implementation 偏离 spec 或 review 不通过
- `verify -> ff`
  - 当 spec 不完整但 change boundary 仍成立
- `verify -> new`
  - 当 change boundary 判断错误或需要重建

这与 Ultra 现有的 feedback loop 完全一致：

- `Review -> Execute`
- `QA -> Execute`
- `QA -> Plan`

## 6. 数据桥接模型

### OpenSpec Change -> TaskManifest

建议映射如下：

- `change-id` -> `TaskManifest.id`
- proposal summary -> `goal`
- design constraints -> `constraints`
- task dependencies -> `dependencies`
- spec delta / acceptance criteria -> `success_criteria`
- affected scope -> `owned_paths`

### OpenSpec Task -> WorkPackage

- task item -> `scope`
- role hint -> `role`
- affected files -> `owned_paths`
- task checks -> `acceptance_checks`

### AgentResult -> OpenSpec Feedback

Ultra 的 `AgentResult` 不直接替代 OpenSpec artifacts，而是作为 feedback layer：

- `evidence` 用于证明完成
- `risks` 用于补充 design 或 tasks
- `failure_context` 用于回写修正建议

## 7. 与 Git Worktree 的关系

这个融合体系非常适合 Worktree：

- 一个 change 对应一个 worktree
- 一个 worktree 对应一个 run
- ledger 需要记录 `change-id`, `worktree path`, `active_write_locks`, `current_stage`

主要价值：

- 并行变更得到物理隔离
- write conflict 更易被管理
- verify / archive 可以按 change 粒度执行

## 8. 对现有 Ultra skill 的影响

现有 Ultra skill 体系不需要推翻。建议保持以下 skill 不变：

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

建议新增一个 bridge skill：

- `openspec-ultra-bridge`

它的职责是：

- 读取 OpenSpec change artifacts
- 生成 `TaskManifest` 和 `WorkPackage`
- 建立 `change-id <-> task-id` 映射
- 把 review / QA / failure context 回写为 OpenSpec 更新建议

## 9. 分阶段融合计划

### Phase 1

先做文档级和协议级融合：

- 明确 change-id / task-id 映射
- 明确 opsx 命令和 Ultra 阶段的对应关系
- 明确 archive gate 的放行条件

### Phase 2

实现 `openspec-ultra-bridge`：

- OpenSpec task -> WorkPackage
- AgentResult -> feedback suggestion
- RunOutput -> archive gate input

### Phase 3

接入 worktree 和 ledger 扩展：

- `change-id`
- `worktree path`
- `active_write_locks`
- `terminal state`

### Phase 4

接入 archive gate 和 automation hooks。

## 10. 现阶段最值得的结论

我的建议是：

- 先做 bridge，不做重写
- 先做 protocol mapping，不做 platform replacement
- 先做 pilot，不做过度自动化

也就是说，当前最好的路线是：

**OpenSpec 做 spec layer，Ultra-Orchestrator 做 control plane，Git Worktree 做 parallel isolation，Automation 做 execution glue。**

## 11. 结语

这条融合路线的价值在于，它能把 spec-first 从“写文档习惯”升级为“可执行、可审计、可回滚的工程编排体系”。

如果你认可这个方向，下一步就适合进入 `openspec-ultra-bridge` 的 skill 规格设计和目录实装。
