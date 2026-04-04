# 版本管理指南

## 当前版本

- **版本号**: v1.0.1
- **发布日期**: 2026-04-04
- **版本状态**: 稳定版

## 版本号规则

本项目使用 [语义化版本](https://semver.org/lang/zh-CN/)（Semantic Versioning）：

版本号格式：`主版本号.次版本号.修订号`

- **主版本号**：重大更新，不兼容旧版本（如 v1.0.0 → v2.0.0）
- **次版本号**：新增功能，向下兼容（如 v1.0.0 → v1.1.0）
- **修订号**：修复问题，向下兼容（如 v1.0.0 → v1.0.1）

## 如何更新版本

### 1. 修改版本号

编辑 `main.py` 文件中的版本信息：

```python
__version__ = "1.1.0"  # 修改这里
__date__ = "2026-04-04"  # 修改日期
```

### 2. 更新 CHANGELOG.md

在 `CHANGELOG.md` 文件顶部添加新版本记录：

```markdown
## [1.1.0] - 2026-04-04

### 新增
- 新功能描述

### 修复
- 修复问题描述
```

### 3. 提交到 Git

```bash
git add main.py CHANGELOG.md
git commit -m "发布 v1.1.0"
git tag v1.1.0
git push origin main --tags
```

## 版本历史

查看 [CHANGELOG.md](./CHANGELOG.md) 了解完整版本历史。

## 查看当前版本

### 方法1：查看代码
打开 `main.py`，查看顶部的 `__version__` 变量。

### 方法2：查看生成的网页
打开生成的 `AI日报.html` 网页，在底部页脚可以看到版本号。

### 方法3：命令行查看
```bash
python -c "import main; print(main.__version__)"
```
