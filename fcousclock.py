# 导入plyer库和time库
from plyer import notification
import time

# 定义工作时间和休息时间（单位为秒）
work_time = 25 * 60
break_time = 5 * 60

# 定义通知的标题和内容
work_title = "开始工作"
work_message = "专注于你的任务，不要分心。"
break_title = "开始休息"
break_message = "放松一下，休息一会儿。"

# 创建一个无限循环，每次循环执行一个工作周期和一个休息周期
while True:
    # 发送开始工作的通知
    notification.notify(title=work_title, message=work_message)
    # 等待工作时间结束
    time.sleep(work_time)
    # 发送开始休息的通知
    notification.notify(title=break_title, message=break_message)
    # 等待休息时间结束
    time.sleep(break_time)
