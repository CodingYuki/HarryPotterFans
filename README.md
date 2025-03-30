# 哈利波特粉丝网站

这是一个基于 Flask 的哈利波特粉丝网站，包含以下功能：

- 哈利波特知识问答
- 分院帽测试
- 魔法小游戏
- 霍格沃茨校歌

## 安装说明

1. 确保已安装 Python 3.7 或更高版本
2. 克隆项目到本地
3. 进入项目目录
4. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行说明

1. 在项目根目录下运行：
   ```bash
   python app.py
   ```
2. 打开浏览器访问：http://localhost:5000

## 功能说明

### 哈利波特问答
- 测试你对哈利波特系列的知识掌握程度
- 包含多个随机问题
- 实时显示得分

### 分院帽测试
- 通过回答一系列问题来确定你属于哪个学院
- 包含进度显示
- 最终显示分院结果

### 魔法小游戏
- 使用方向键控制角色移动
- 空格键施放魔法
- 躲避障碍物
- 计分系统

### 霍格沃茨校歌
- 显示英文歌词和中文翻译
- 提供音频播放功能
- 支持在线播放

## 项目结构

```
harry_potter_fan_site/
├── app.py              # Flask 应用主文件
├── requirements.txt    # 项目依赖
├── static/            # 静态文件
│   ├── css/          # 样式文件
│   ├── js/           # JavaScript 文件
│   ├── images/       # 图片资源
│   └── audio/        # 音频文件
└── templates/         # HTML 模板
    ├── index.html     # 主页
    ├── quiz.html      # 问答页面
    ├── sorting_hat.html # 分院帽测试页面
    ├── game.html      # 游戏页面
    └── school_song.html # 校歌页面
```

## 注意事项

- 请确保在运行游戏时使用现代浏览器
- 音频播放需要浏览器支持 HTML5 音频
- 建议使用 Chrome 或 Firefox 浏览器以获得最佳体验 