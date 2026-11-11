# 更新日志

本文件记录课程内容与仓库结构的变更。版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## 未发布

### 新增

- GitHub Issue 表单：内容错误 / 代码问题、内容建议 / 改进
- `assets/social-preview.png`（1280×640）及可编辑的 HTML 源文件

## v1.0.0 — 2026-11-11

首个开源版本。

### 新增

- 7 讲 Jupyter 课件（`notebooks/`）
- 7 份 PDF 讲义（`pdf/`）
- 课程插图（`notebooks/img/`）
- 中文 / 英文 README、MIT LICENSE、贡献指南、维护指南
- `scripts/build_pdf.py`：从 ipynb 重新生成 PDF

### 修复

- 第 1 讲：Python 开源协议由 GPL 更正为 PSF License（与 GPL 兼容）
- 第 1 讲：统一 Python 2 / 3 版本号的写法
- 第 2 讲：标题与文件名统一为 PyCharm，修正“入门关工具”错字
- 第 3 讲：`6.1` 标题行首多余空格导致不渲染；补充 Jupyter 与 PyCharm 输出差异的说明
- 第 4 讲：缩进建议改为 PEP 8 的 4 个空格，避免与主流规范冲突
- 第 5 讲：while 小节重复编号 `2.3` → `2.4`；“元祖” → “元组”
- 第 6 讲：圆面积注释误写为“半径”
- 全部：删除末尾空白代码格，清理交互式 `input()` 的残留输出

### 变更

- 课件页首声明由“禁止转载”改为 MIT 开源声明，并加上对应 B 站分集链接
- 目录结构由 `jupyter版/`、`pdf版/` 调整为 `notebooks/`、`pdf/`
- PDF 由更新后的课件重新生成（A4、文字可检索）

### 说明

- 视频仍以 B 站为准，仓库不包含视频文件
