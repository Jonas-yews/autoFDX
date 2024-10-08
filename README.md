# 自动化脚本 - Fallen Doll

## 项目介绍

这是一个适用于Fallen Doll（堕落玩偶）游戏的自动化脚本，主要功能是利用PyAutoGUI库实现找图点击鼠标功能。

---

## 功能实现

代码实现了以下主要功能：

- **自动点击双重高潮**：通过图像识别自动点击双重高潮按钮。
- **自动重复**：重复五次点击操作后播放提示音并等待五秒，如果等待期间按下键盘空格键则会中止程序，方便用户更换实验，再次点击键盘回车键后继续程序；如果等待期间没有按下空格键，则自动重复循环。
- **自动点赞**：每次双高、点击再来一发按钮后会为玩家列表第一位和第二位（防止第一位玩家处于失去理智无法点赞状态）分别点赞两次（请确保打开玩家列表）。

---

## 如何使用

### 系统环境参数

1. 下载压缩包后解压
2. Python版本3.12.2
3. 安装必要环境：在CMD中分别输入以下代码然后回车：
   ```sh
   pip install numpy opencv-contrib-python PyAutoGUI
   pip install threading
   pip install winsound
   pip install sys
   pip install keyboard

### 操作说明

1. 启动脚本后需要手动将灵敏度拉到最高。
2. 重点：需要手动将速度调整到能够达到双重高潮。本脚本只能实现自动点击，无法自动调整速度。
3. 请在打开游戏，并且将实验放置好之后再双击打开脚本（程序开头会直接寻找开始按钮并点击）。
4. 适用于1k分辨率、全屏模式

## 版本更新内容摘要

**v1.0 (2024-07-01):**
- 初始版本，实现自动点击双重高潮和自动重复功能。

**v1.01 (2024-07-04):**
- 删除了cum1.png和cum3.png

**v1.02 (2024-08-19):**
- 游戏版本更新导致脚本点赞give函数bug，更新了新版本的点赞xy坐标，修复了点赞功能
- 添加了【拘束器自动化】文件夹：简单的重复点击内射和点赞，拘束器刷通行证用
