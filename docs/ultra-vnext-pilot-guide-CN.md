# Codex Ultra Orchestration vNext 试跑说明

## 目标

这份说明用于试跑 `ultra-orchestration` 仓库中的 vNext 技能树。

vNext 技能树位置：

`<REPO_ROOT>\skills-vnext`

## 主入口

vNext 只需要一个主入口：

```text
$ultra-vnext-core <任务描述>
```

`ultra-vnext-core` 会根据任务类型自动路由到需要的子技能。用户不需要手动列出 `ultra-brainstorming`、`ultra-planning`、`ultra-review` 等全部技能。

如果客户端提供 slash alias，也可以使用：

```text
/ultra-vnext-core <任务描述>
```

## 技能组成

- `ultra-vnext-core`
  主入口、路由器、共享 contracts、状态机、ledger 初始化和 contract 校验脚本
- `ultra-brainstorming`
  设计先行的澄清流程与显式审批门
- `ultra-planning`
  TaskManifest、WorkPackage、DAG 和写锁边界
- `ultra-execution-control`
  dispatch、freeze/careful/guard、host-driven ledger
- `ultra-review`
  spec fidelity、evidence、downside risk 审查
- `ultra-qa`
  static + dynamic QA 双模式
- `ultra-risk-vetting`
  风险分级、审批门槛和护栏选择
- `ultra-delivery`
  final deliverable、orchestration log、vetter report 和 retro 交付
- `openspec-ultra-bridge-v2`
  将 OpenSpec change 资产桥接成 Ultra 执行工件

## 推荐试跑方式

### 通用任务

```text
$ultra-vnext-core 构建一个工作区模型默认值设置页。
```

主入口会按需要路由到设计澄清、规划、风险门、执行、审查、QA 和交付阶段。

### OpenSpec 项目

```text
$ultra-vnext-core OpenSpec change <change-id 或路径>: 实现第一个 slice。
```

示例 change 路径：

`<PROJECT_ROOT>\openspec\changes\<change-id>`

主入口会先路由到 `openspec-ultra-bridge-v2`，再继续进入 Ultra 的规划、执行、审查、QA 和交付流程。

### Bug 修复

```text
$ultra-vnext-core bugfix: 审批通过后命令执行卡住。
```

主入口会建立最小调查计划，识别回归面，执行风险判断，并要求交付前提供 QA 证据。

## 辅助脚本

初始化 run：

```powershell
python <REPO_ROOT>\skills-vnext\ultra-vnext-core\scripts\new_run.py `
  <PROJECT_ROOT>\runs-vnext `
  --run-id run-001
```

桥接 OpenSpec change：

```powershell
python <REPO_ROOT>\skills-vnext\openspec-ultra-bridge-v2\scripts\bridge_change.py `
  <PROJECT_ROOT>\openspec\changes\<change-id> `
  <PROJECT_ROOT>\runs-vnext\bridge-output
```

校验核心 contract：

```powershell
python <REPO_ROOT>\skills-vnext\ultra-vnext-core\scripts\validate_contracts.py `
  <PROJECT_ROOT>\runs-vnext\run-001\ledger.json `
  --kind executionledger
```

## 不安装时如何调用

如果暂时不想安装 vNext，可以让 agent 直接读取主入口技能文件：

```text
请读取并使用 <REPO_ROOT>\skills-vnext\ultra-vnext-core\SKILL.md。
任务：OpenSpec change <PROJECT_ROOT>\openspec\changes\<change-id>，实现第一个 slice。
```

## 成功标准

一次试跑可以认为成功，当它满足：

- 用户只需要调用 `ultra-vnext-core` 主入口
- 主入口能正确识别通用任务、OpenSpec change 或 bugfix
- 实现前存在明确 design 或 OpenSpec change
- `TaskManifest` 和 `WorkPackage` 不依赖聊天历史也能被理解
- 风险门有明确分级和 guardrail
- review 有 accept / reject / reroute 结论
- QA 明确区分 static evidence 与 dynamic evidence
- delivery 产出 `final_deliverable`、`orchestration_log`、`vetter_report`
- 残余风险和 follow-up 被单独列出
