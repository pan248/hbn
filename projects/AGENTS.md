# AGENTS.md

## 项目概览
HBN品牌「慢一点远一点」主题移动端H5落地页，面向大广赛参赛作品展示。
- 技术栈：原生 HTML/CSS/JS（native-static 模板）
- 部署：Python http.server（端口 5000）
- 目标环境：移动端浏览器 + 微信 WebView

## 目录结构
```
├── index.html          # H5 主页面（单页全内容）
├── styles/main.css     # 全局样式（含动画、响应式）
├── games/
│   ├── liankan.html    # 连连看游戏「慢慢寻·成分寻缘」
│   ├── jie-dongxi.html # 接东西游戏「慢慢接·晨露凝收」
│   └── xiaoxiaole.html # 消消乐游戏「慢慢消·时光沉淀」
├── public/qrcode.png   # 品牌配色二维码图片
├── DESIGN.md           # 设计规范
├── .coze               # 项目配置（构建与运行）
└── AGENTS.md           # 本文件
```

## 构建与运行
- 开发：`coze dev` 或 `python -m http.server 5000 --bind 0.0.0.0`
- 部署：同上（静态项目无需构建步骤）
- 端口：5000

## 代码风格
- CSS 变量统一管理设计 Token（颜色、缓动曲线等）
- 字体：Noto Serif SC（.cn 域）用于标题衬线排版
- 动画：缓慢柔和，缓动曲线 cubic-bezier(0.25, 0.1, 0.25, 1.0)
- JS：IIFE 包裹，ES5 兼容写法，确保微信旧版 WebView 兼容
- 滚动动画：IntersectionObserver + .reveal 类

## 关键功能
- 全屏沉浸式分屏滚动
- 浮动金色粒子效果（CSS animation）
- 滚动触发的渐显动画
- 互动体验入口区域（3个主题小游戏）
- 连连看「慢慢寻」：4x4成分配对，点击匹配相同成分消除
- 接东西「慢慢接」：Canvas水滴下落，触控移动瓶身接住精华
- 消消乐「慢慢消」：6x6三消，交换相邻成分消除，支持连消
- 静态二维码（/public/qrcode.png）+ 动态 fallback
- 分享功能（微信 JSBridge + 剪贴板复制）
- 微信分享 meta 标签配置

## 注意事项
- 二维码图片使用品牌色（#2C1810 前景 / #F5EDE3 背景）
- 所有外部资源使用 .cn 域（Google Fonts）
- 禁止 emoji、荧光色、快速动画
