from datetime import datetime


def calMinuteDuration(start, end):  # 计算一个活动的持续时间，单位为分钟
    start_time = datetime.strptime(start, "%Y/%m/%d:%H:%M")
    end_time = datetime.strptime(end, "%Y/%m/%d:%H:%M")
    minDuration = ((end_time - start_time).total_seconds()) / 60
    return minDuration  # 带一位小数

print(calMinuteDuration('2022/7/7:22:00','2022/7/7:23:00'))