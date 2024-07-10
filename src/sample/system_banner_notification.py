# 发送系统横幅通知

import subprocess

# 这行代码导入了 Python 的 subprocess 模块，该模块允许你生成新的进程，连接到它们的输入/输出/错误管道，并获取它们的返回码。

def show_notification(title, text):
    cmd = 'display notification "{}" with title "{}"'.format(text, title)
    subprocess.call(["osascript", "-e", cmd])


# 这里创建了一个名为 cmd 的变量，它包含了一个格式化的字符串，这个字符串是一个 AppleScript 命令，用于显示通知。
# 使用 format 方法将 text 和 title 插入到 AppleScript 命令中。format(text, title) 将第一个 {} 替换为 text 的值，将第二个 {} 替换为 title 的值。

# subprocess.call 函数用于运行命令。参数是一个列表，其中包含要执行的命令及其参数。
# "osascript" 是执行 AppleScript 脚本的命令。
# "-e" 参数指定后面的字符串是一段要执行的脚本。
# cmd 是前面构建的包含通知命令的 AppleScript 脚本。

# 执行示例
# show_notification("会议提醒", "你的下一次会议将在 10 分钟后开始。")

# 跟 DialogDemo1.py 几乎一样，只是调用方式不同


# 注意：
# 这个函数仅适用于 macOS，因为它依赖于 macOS 的 osascript 命令。
# 确保在使用这个函数之前已经导入了 subprocess 模块。
