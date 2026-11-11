# 维护与发布指南

这份文档给维护者看：怎么把仓库发布到 GitHub、怎么打版本、改了课件之后怎么重新生成 PDF。普通学习者只需要看 [README.md](README.md)。

## 1. 仓库元数据

### 仓库名

```text
python-beginner
```

### About 描述（可直接粘贴）

```text
马哥 Python 入门私教课｜7 讲 + 13 个视频，零基础从安装到面向对象。含可运行 Jupyter 课件与 PDF，B 站同步讲解，MIT 开源。
```

英文字段可以追加一句，方便国际搜索：

```text
Beginner-friendly Python course in Chinese: 7 lectures, 13 videos, Jupyter notebooks + PDF handouts.
```

### Website

```text
https://www.bilibili.com/video/BV1aK4y1F7g9
```

### Topics（最多 20 个，只能用小写字母、数字和连字符）

```text
python
python3
python-tutorial
tutorial
beginner
beginners
learning-python
chinese
zh-cn
jupyter
jupyter-notebook
video-course
bilibili
programming
oop
functions
loops
data-types
education
learn-to-code
```

> GitHub 的 topics 不支持中文。中文关键词放在 About 描述和 README 标题里即可。

### Social preview

在 **Settings → General → Social preview** 上传一张 1280×640 的图片。可以用 B 站课程封面，或做一张写着课程名、讲次数、“零基础”的简洁封面。注意缩略图尺寸下文字仍然可读。

## 2. 首次发布

```bash
cd "【课件】马哥Python入门私教课"

git init -b main
git add .
git status                 # 确认没有 .DS_Store、.ipynb_checkpoints、视频文件
git commit -m "docs: 开源 Python 入门私教课课件（7 讲）"

git remote add origin git@github.com:<你的用户名>/python-beginner.git
git push -u origin main
```

推送后在 GitHub 上依次设置：

1. **About**：填描述、Website、上面的 20 个 topics；
2. **Settings → General → Social preview**：上传封面；
3. **Settings → Features**：开启 Issues，Discussions 可选；
4. **Branches**：默认分支设为 `main`，可给 `main` 加保护规则；
5. 发布 `v1.0.0` Release（见下一节）。

## 3. 版本与标签

版本号遵循语义化版本：

| 变更类型 | 版本位 | 例子 |
| --- | --- | --- |
| 课程结构大改、目录不兼容 | MAJOR | `v2.0.0` |
| 新增一讲、新增章节 | MINOR | `v1.1.0` |
| 错别字、链接、排版、代码修正 | PATCH | `v1.0.1` |

打标签并发布 Release：

```bash
git tag -a v1.0.0 -m "首个开源版本：7 讲课件 + PDF"
git push origin v1.0.0

gh release create v1.0.0 \
  --title "v1.0.0 课程开源首发" \
  --notes "## 课程首发

- 7 讲 Jupyter 课件与 7 份 PDF 讲义
- 13 个 B 站视频，总时长约 78 分钟
- 修正课件中的协议说明、编号、错别字
- 新增英文 README 与 PDF 构建脚本"
```

Release 说明建议包含：本次改了什么、对应 B 站视频是否更新、是否有不兼容的目录调整。

## 4. 修改课件后重新生成 PDF

PDF 是提交进仓库的，所以**改了 ipynb 就要同步重新生成 PDF**，否则两份内容会不一致。

依赖：

```bash
pip install nbconvert
# 另需本机安装 Google Chrome 或 Chromium
```

生成全部 PDF：

```bash
python scripts/build_pdf.py
```

只生成某一讲：

```bash
python scripts/build_pdf.py 第3讲-Python数据类型
```

Chrome 不在默认路径时：

```bash
CHROME=/path/to/chrome python scripts/build_pdf.py
```

脚本会先用 nbconvert 把每个 notebook 转成自包含 HTML，再用无头 Chrome 打印成 A4 PDF，最后覆盖 `pdf/` 下的同名文件。生成后建议打开 PDF 抽查：中文是否正常、图片是否完整、代码有没有被截断。

## 5. 发布前检查清单

- [ ] README 里的文件名、讲次、时长与 B 站一致
- [ ] B 站链接的 `p` 参数正确：第 1、2、3、9、10、12、13 P
- [ ] 每个 notebook 能从顶部运行到尾（刻意保留的报错示例除外）
- [ ] `notebooks/img/` 完整，GitHub 上图片能正常渲染
- [ ] PDF 与 ipynb 内容一致，页首声明是 MIT
- [ ] 没有 `.DS_Store`、`.ipynb_checkpoints/`、`__pycache__/`
- [ ] `LICENSE` 的年份与署名正确
- [ ] 中文 README 与 `README_EN.md` 的互相链接可用
- [ ] About、Topics、Website、Social preview 已设置
- [ ] 已打 tag 并发布 Release
- [ ] 仓库体积合理（当前约 9 MB，无需 Git LFS）

## 6. 目录与命名约定

```text
notebooks/第N讲-主题.ipynb     # 课件，中文文件名，与视频标题对应
notebooks/img/                 # 插图，必须与 ipynb 同级，保持相对路径引用
pdf/第N讲-主题.pdf             # 与 ipynb 同名，方便对照
scripts/build_pdf.py           # 构建脚本
```

约定：

- 不提交视频文件、录屏素材、大体积压缩包；
- 图片文件名保持稳定，替换截图时不要改文件名，避免批量修改 ipynb；
- 新增讲次时，README 表格、`CHANGELOG.md`、B 站分集链接要一起更新；
- 中文文件名没问题，但**不要包含空格、括号、`#`、`?`**，否则链接需要转义。

## 7. 常见维护任务

### 新增一讲

1. 放入 `notebooks/第8讲-主题.ipynb` 和对应图片；
2. 在 README 表格中加一行，补上视频 `p` 参数与时长；
3. 运行 `python scripts/build_pdf.py 第8讲-主题`；
4. 更新 `CHANGELOG.md`，提交后打 `v1.1.0`。

### 替换截图

1. 用同名文件覆盖 `notebooks/img/` 下的旧图；
2. 压缩到合理体积（建议单张 < 300 KB）；
3. 遮盖截图里的用户名、本地路径、浏览器头像等个人信息；
4. 重新生成对应 PDF。

### 修改课程文案

1. 改 ipynb 中对应的 markdown / code cell；
2. 重新运行并保存输出；
3. 重新生成 PDF；
4. 在 `CHANGELOG.md` 记录改了什么。

## 8. 可选增强

- **GitHub Actions**：加一个 nbformat 校验工作流，防止提交损坏的 ipynb；
- **GitHub Pages / nbviewer**：给课件做一个网页入口，方便手机阅读；
- **英文 README 完善**：如果面向国际读者，可补充英文目录和截图说明；
- **视频合集**：在 B 站把 13 个视频加入同一个合集，方便按讲次跳转。
