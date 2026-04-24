# Codex Ultra Orchestration 主线试跑说明

## 目标

这份说明用于试跑 `ultra-orchestration` 仓库中的主线 strict 控制面。

默认入口已经从 vNext 预览入口收敛为：

```text
$ultra-orchestrator <任务描述>
```

`ultra-vnext-core` 仍然保留为兼容别名，但新用户和新项目默认使用
`ultra-orchestrator`。

## 主入口

推荐调用方式：

```text
$ultra-orchestrator <任务描述>
```

OpenSpec 显式调用：

```text
$ultra-orchestrator OpenSpec change <change-id 或路径>: <任务描述>
```

如果客户端提供 slash alias，也可以使用：

```text
/ultra-orchestrator <任务描述>
```

## 运行模式

主入口启动后必须先判断运行模式：

- `LIGHT`
  适合 review-only、QA-only、解释类或用户明确要求轻量执行的任务。
- `STANDARD`
  适合用户明确要求快速编排、且风险低的任务。
- `STRICT`
  适合无法使用 OpenSpec，但仍需要 ledger 和 JSON contracts 的开发任务。
- `STRICT_OPENSPEC`
  开发任务默认优先模式，适合 feature、bugfix、多文件实现、pilot、完整控制面验证和 slice DAG 执行。

开发任务应优先进入 `STRICT_OPENSPEC`。如果无法使用该模式，agent 必须说明降级原因。

## 推荐试跑

### 普通开发任务

```text
$ultra-orchestrator 构建一个工作区模型默认值设置页。
```

期望行为：

- 默认优先 `STRICT_OPENSPEC`
- 若没有现成 OpenSpec change，先创建或要求创建 change scaffold
- 初始化 run ledger
- 产出 JSON `TaskManifest` 和 JSON `WorkPackage`
- 运行 contract validation
- 按 slice DAG 推进
- delivery 输出 `control_surface_used`

### OpenSpec 项目

```text
$ultra-orchestrator OpenSpec change <change-id 或路径>: 实现第一个 slice。
```

示例 change 路径：

```text
<PROJECT_ROOT>\openspec\changes\<change-id>
```

期望行为：

- 通过 `openspec-ultra-bridge` 桥接 proposal、design、tasks 和 ultra-bridge
- 将 OpenSpec change 转成 Ultra execution artifacts
- 再进入 planning、risk、dispatch、review、QA 和 delivery

### Review-only

```text
$ultra-orchestrator review this implementation
```

期望行为：

- 允许 `LIGHT`
- delivery 明确说明为什么未使用 OpenSpec、ledger 或 contract validation

## 严格控制面最低要求

`STRICT` 和 `STRICT_OPENSPEC` 运行必须具备：

- `ledger.json`
- JSON `TaskManifest`
- JSON `WorkPackage`
- JSON 或结构化 `AgentResult`
- `validate_contracts.py` 校验结果
- review 结论
- QA 结论
- `control_surface_used`

如果只能产出 Markdown 文档，本次试跑不能算 strict 成功。

## 辅助脚本

初始化 run：

```powershell
python <REPO_ROOT>\skills\ultra-orchestrator\scripts\new_run.py `
  <PROJECT_ROOT>\runs `
  --run-id run-001 `
  --run-mode STRICT_OPENSPEC
```

校验核心 contract：

```powershell
python <REPO_ROOT>\skills\ultra-orchestrator\scripts\validate_contracts.py `
  <PROJECT_ROOT>\runs\run-001\ledger.json `
  --kind executionledger
```

校验完整 run：

```powershell
python <REPO_ROOT>\skills\ultra-orchestrator\scripts\validate_run.py `
  <PROJECT_ROOT>\runs\run-001
```

桥接 OpenSpec change：

```powershell
python <REPO_ROOT>\skills-vnext\openspec-ultra-bridge-v2\scripts\bridge_change.py `
  <PROJECT_ROOT>\openspec\changes\<change-id> `
  <PROJECT_ROOT>\runs\bridge-output
```

## 成功判断

一次主线试跑可以认为成功，当它满足：

- 用户只需要调用 `ultra-orchestrator`
- 开发任务默认优先 `STRICT_OPENSPEC`
- 无 OpenSpec change 时不会直接降级为 Markdown-only 编排
- strict run 使用 ledger、JSON artifacts 和 contract validation
- `TaskManifest` 和 `WorkPackage` 不依赖聊天历史也能被理解
- slice status、owned paths、review gate 和 QA gate 明确
- delivery 输出 `final_deliverable`、`orchestration_log`、`vetter_report` 和 `control_surface_used`
- 残余风险和 skipped control surfaces 被单独列出
