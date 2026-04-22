# Codex Ultra Orchestration vNext 试跑说明

## 目标

这份说明用于在不改动主工作空间 `D:\Codex_workspace\.agents\skills` 的前提下，
试跑本轮新增的 vNext 技能树。

vNext 技能树位置：

`D:\Codex_workspace\codex_ultra_orchestration\skills-vnext`

## 本轮新增了什么

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
- `openspec-ultra-bridge-v2`
  将 OpenSpec change 资产桥接成 Ultra 执行工件

## 推荐试跑顺序

建议先在 `/teammate` 项目验证一条完整但收敛的链路：

1. 选择一个已有 OpenSpec change
2. 用 `openspec-ultra-bridge-v2` 生成桥接工件
3. 用 `ultra-vnext-core` 初始化 run 目录
4. 用 `ultra-brainstorming` 和 `ultra-planning` 重新审视是否收敛
5. 再进入执行、review、QA

推荐 change：

`D:\Codex_workspace\teammate\app-repo\openspec\changes\desktop-runtime-foundation`

## 已验证的本地命令

初始化 run：

```powershell
python D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\ultra-vnext-core\scripts\new_run.py `
  D:\Codex_workspace\codex_ultra_orchestration\runs-vnext `
  --run-id run-20260422-vnext-smoke
```

桥接 OpenSpec change：

```powershell
python D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\openspec-ultra-bridge-v2\scripts\bridge_change.py `
  D:\Codex_workspace\teammate\app-repo\openspec\changes\desktop-runtime-foundation `
  D:\Codex_workspace\codex_ultra_orchestration\pilot-output\desktop-runtime-foundation
```

校验核心 contract：

```powershell
python D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\ultra-vnext-core\scripts\validate_contracts.py `
  D:\Codex_workspace\codex_ultra_orchestration\runs-vnext\run-20260422-vnext-smoke\ledger.json `
  --kind executionledger

python D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\ultra-vnext-core\scripts\validate_contracts.py `
  D:\Codex_workspace\codex_ultra_orchestration\runs-vnext\run-20260422-vnext-smoke\run-output.json `
  --kind runoutput
```

## 当前已产出的试跑物

- run 目录：
  `D:\Codex_workspace\codex_ultra_orchestration\runs-vnext\run-20260422-vnext-smoke`
- bridge 目录：
  `D:\Codex_workspace\codex_ultra_orchestration\pilot-output\desktop-runtime-foundation`

桥接目录里已经包含：

- `bridge-summary.json`
- `task-manifest.json`
- `task-manifest.yaml`
- `work-packages.json`
- `work-packages.yaml`

## 线程中如何调用

因为这套 vNext 目前还没有装进全局技能目录，所以在新的项目线程里不应该假设
可以直接使用 `/ultra-vnext-core` 之类的全局命令。

推荐做法是：

1. 在新线程中明确说明要使用
   `D:\Codex_workspace\codex_ultra_orchestration\skills-vnext` 里的技能
2. 让 Codex 先读取相应 `SKILL.md`
3. 再按技能规范推进

可直接这样说：

```text
请读取 D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\openspec-ultra-bridge-v2\SKILL.md
和 D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\ultra-vnext-core\SKILL.md，
然后对 D:\Codex_workspace\teammate\app-repo\openspec\changes\desktop-runtime-foundation
执行 bridge + run 初始化 + planning 准备。
```

如果要做完整设计先行链路，可用：

```text
请依次读取并使用
1. D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\ultra-brainstorming\SKILL.md
2. D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\ultra-planning\SKILL.md
3. D:\Codex_workspace\codex_ultra_orchestration\skills-vnext\openspec-ultra-bridge-v2\SKILL.md

目标仓库是 D:\Codex_workspace\teammate\app-repo
目标 change 是 openspec/changes/desktop-runtime-foundation
请按 vNext 方法完成 spec tighten、bridge mapping 和 execution-ready plan。
```

## 当前阻塞

本地 vNext 已完成独立落地和 smoke test。

唯一还没完成的是：

- 远程 `ultra-orchestration` 仓库地址尚未在当前工作区中定位到
- 因此还不能执行“克隆远程仓库并推送新版本”这一步

一旦补充远程仓库 URL，就可以把这套 `skills-vnext` 迁入真正的仓库底座并推送。
