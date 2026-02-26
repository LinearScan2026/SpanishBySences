# 家庭场景语言启蒙小抄（西语 + 英语）

给 3 岁孩子的沉浸式语言启蒙材料，按家庭各区域整理高频句子，支持**西班牙语**和**英语**双语切换，配合 12 个月渐进计划使用。

## 孩子当前水平

- 词汇量 500+，以名词为主
- 能听懂简单句（¿Dónde está tu zapato? / Quiero más leche）
- 能说单词和少量短句，完整句子不多

## 家庭成员

| 中文 | 西班牙语 | 英语 |
|------|----------|------|
| 妈妈 | Mamá     | Mommy |
| 爸爸 | Papá     | Daddy |
| 宝宝 | Bebé / 孩子名字 | Baby / 孩子名字 |
| 爷爷 | Abuelo   | Grandpa |
| 奶奶 | Abuela   | Grandma |

## 12 个月计划概览

| 阶段 | 时间 | 目标 | 核心句型 |
|------|------|------|----------|
| 阶段 1 | 第 1-2 月 | 听懂并执行 | 祈使句、是/否问句、Vamos a... |
| 阶段 2 | 第 3-4 月 | 短句输出 | Yo quiero...、Es + 形容词、Me gusta... |
| 阶段 3 | 第 5-6 月 | 简单对话 | ¿Qué estás haciendo?、Porque...、¿Puedo...? |
| 阶段 4 | 第 7-8 月 | 描述与叙述 | 过去时（Comí / Fui）、方位词、¿Cuántos? |
| 阶段 5 | 第 9-10 月 | 感受与想法 | Estoy + 情绪、Voy a...、más...que、¿Me ayudas? |
| 阶段 6 | 第 11-12 月 | 自主表达 | y/pero/también、Si + 条件、Yo creo que... |

## 包含区域

| 编号 | 区域 | 西语文件 | 英语文件 |
|------|------|----------|----------|
| 01 | 卫生间 | [cheatsheets/01-bano.md](cheatsheets/01-bano.md) | [cheatsheets-en/01-bano.md](cheatsheets-en/01-bano.md) |
| 02 | 客厅 | [cheatsheets/02-sala.md](cheatsheets/02-sala.md) | [cheatsheets-en/02-sala.md](cheatsheets-en/02-sala.md) |
| 03 | 餐桌 | [cheatsheets/03-mesa-comedor.md](cheatsheets/03-mesa-comedor.md) | [cheatsheets-en/03-mesa-comedor.md](cheatsheets-en/03-mesa-comedor.md) |
| 04 | 大门玄关 | [cheatsheets/04-puerta-entrada.md](cheatsheets/04-puerta-entrada.md) | [cheatsheets-en/04-puerta-entrada.md](cheatsheets-en/04-puerta-entrada.md) |
| 05 | 卧室 | [cheatsheets/05-dormitorio.md](cheatsheets/05-dormitorio.md) | [cheatsheets-en/05-dormitorio.md](cheatsheets-en/05-dormitorio.md) |
| 06 | 厨房 | [cheatsheets/06-cocina.md](cheatsheets/06-cocina.md) | [cheatsheets-en/06-cocina.md](cheatsheets-en/06-cocina.md) |
| 07 | 电梯 | [cheatsheets/07-ascensor.md](cheatsheets/07-ascensor.md) | [cheatsheets-en/07-ascensor.md](cheatsheets-en/07-ascensor.md) |
| 08 | 地下车库 | [cheatsheets/08-garaje.md](cheatsheets/08-garaje.md) | [cheatsheets-en/08-garaje.md](cheatsheets-en/08-garaje.md) |
| 09 | 汽车内 | [cheatsheets/09-coche.md](cheatsheets/09-coche.md) | [cheatsheets-en/09-coche.md](cheatsheets-en/09-coche.md) |
| 10 | 幼儿园门口 | [cheatsheets/10-guarderia.md](cheatsheets/10-guarderia.md) | [cheatsheets-en/10-guarderia.md](cheatsheets-en/10-guarderia.md) |

## 如何使用

### 传到 iPhone 上查看

`index.html` 是**单文件自包含**的（CSS 已内嵌），只需传这一个文件即可。

**方法一：微信传输（最简单）**
1. 电脑微信登录，打开"文件传输助手"
2. 把 `index.html` 拖进去发送
3. 手机微信点开文件 → 点右上角"..." → "用其他应用打开" → 选择"Safari"或"文件"
4. 在 Safari 中打开后，可以"添加到主屏幕"方便下次使用

**方法二：iCloud 同步**
1. 电脑安装 [iCloud for Windows](https://support.apple.com/zh-cn/icloud-windows)
2. 把 `index.html` 放入 iCloud Drive 文件夹
3. iPhone 上打开"文件"App → iCloud Drive → 找到文件 → 点击用 Safari 打开

**方法三：邮件发送**
1. 把 `index.html` 作为附件发邮件给自己
2. iPhone 上打开邮件 → 点附件 → 用 Safari 打开

### A4 打印
用浏览器打开 `index.html`，按 Ctrl+P（Mac: Cmd+P）打印，每个区域自动分页为独立 A4 页。建议打印后贴在对应区域，随时参考。

### 渐进使用
1. 先看 [plan-12-meses.md](plan-12-meses.md) 了解整体计划
2. 每个阶段只关注对应标签的句子（阶段1 / 阶段2 / 阶段3）
3. 顶部有"阶段筛选按钮"，可以只显示当前阶段的句子
4. 每个场景先选 3-5 句反复使用，熟练后再加新句子

### 修改内容后重新生成 HTML
编辑 `cheatsheets/` 或 `cheatsheets-en/` 下的 Markdown 文件或 `style.css` 后，运行：
```
python build.py
```
会重新生成 `index.html`，把更新的文件传到手机即可。

## 在线访问

本项目已部署到 GitHub Pages，可直接在浏览器中打开：

**https://LinearScan2026.github.io/SpanishBySences/**

## 使用原则

- **只说目标语言**：中文翻译只帮家长理解含义，对孩子只说目标语言（西语或英语）
- **动作配合**：说的同时做出动作，帮助孩子理解
- **不纠正，多重复**：孩子说错时，用正确的说法重复一遍即可
- **高频重复**：同一句话在同一场景反复出现，才能内化
- **耐心等待**：说完后给孩子 5-10 秒反应时间
