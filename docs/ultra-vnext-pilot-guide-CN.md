# Codex Ultra Orchestration vNext 试跑说明

## 目标

这份说明用于试跑 `ultra-orchestration` 仓库中的 vNext 技能树。

vNext 技能树位置：

`<REPO_ROOT>\skills-vnext`

## 本轮包含的 vNext 技能

- `ultra-vnext-core`
  共享 contracts、状态机、ledger 初始化和 contract 校验脚本
- `ultra-brainstorming`
  吸收 `superpowers` 的 design-first / hard-gate 方式
- `ultra-planning`
  强化 TaskManifest、WorkPackage、DAG 和写锁边界
- `ultra-execution-control`
  强化 dispatch、freeze/careful/guard、host-driven ledger
- `ultra-review`
  强化 spec fidelity / evidence / downside risk 审查
- `ultra-qa`
  强化 static + dynamic QA 双模式
- `ultra-risk-vetting`
  强化风险分级、审批门槛和护栏选择
- `ultra-delivery`
  强化 final deliverable、orchestration log、vetter report 和 retro 交付
- `openspec-ultra-bridge-v2`
  将 OpenSpec change 资产桥接成 Ultra 执行工件

## 推荐试跑顺序

建议先在 `/teammate` 项目验证一条完整但收敛的链路：

1. 选择一个已有 OpenSpec change
2. 用 `openspec-ultra-bridge-v2` 生成桥接工件
3. 用 `ultra-vnext-core` 初始化 run 目录
4. 用 `ultra-brainstorming` 和 `ultra-planning` 重新审视是否收敛
5. 用 `ultra-risk-vetting` 做风险门判断
6. 进入 execution、review、QA
7. 用 `ultra-delivery` 汇总交付、证据、风险和复盘

推荐 change：

`<PROJECT_ROOT>\openspec\changes\<change-id>`

## 已验证的本地命令

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

如果还不想把 vNext 安装进全局技能目录，可以在新线程里让 Codex 直接读取本仓库里的 `SKILL.md`。

最小桥接链路：

```text
请读取并使用：
1. <REPO_ROOT>\skills-vnext\openspec-ultra-bridge-v2\SKILL.md
2. <REPO_ROOT>\skills-vnext\ultra-vnext-core\SKILL.md

然后对 <PROJECT_ROOT>\openspec\changes\<change-id>
执行 bridge + run 初始化 + planning 准备。
```

完整设计先行链路：

```text
请依次读取并使用：
1. <REPO_ROOT>\skills-vnext\ultra-brainstorming\SKILL.md
2. <REPO_ROOT>\skills-vnext\ultra-planning\SKILL.md
3. <REPO_ROOT>\skills-vnext\openspec-ultra-bridge-v2\SKILL.md
4. <REPO_ROOT>\skills-vnext\ultra-risk-vetting\SKILL.md
5. <REPO_ROOT>\skills-vnext\ultra-execution-control\SKILL.md
6. <REPO_ROOT>\skills-vnext\ultra-review\SKILL.md
7. <REPO_ROOT>\skills-vnext\ultra-qa\SKILL.md
8. <REPO_ROOT>\skills-vnext\ultra-delivery\SKILL.md

目标仓库是 <PROJECT_ROOT>。
目标 change 是 openspec/changes/<change-id>。
请按 vNext 方法完成 spec tighten、bridge mapping、execution-ready plan、review、QA 和 delivery。
```

## 成功标准

一次试跑可以认为成功，当它满足：

- 实现前存在明确 design 或 OpenSpec change
- `TaskManifest` 和 `WorkPackage` 不依赖聊天历史也能被理解
- 风险门有明确分级和 guardrail
- review 有 accept / reject / reroute 结论
- QA 明确区分 static evidence 与 dynamic evidence
- delivery 产出 `final_deliverable`、`orchestration_log`、`vetter_report`
- 残余风险和 follow-up 被单独列出
