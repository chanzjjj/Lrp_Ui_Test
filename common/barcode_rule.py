import json
import os
from datetime import datetime

class DailyCounter:
    def __init__(self, storage_file='counter.json'):
        self.storage_file = storage_file
        self._init_storage()

    def _init_storage(self):
        """初始化存储文件"""
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({'date': None, 'count': 0}, f)

    def _read_data(self):
        """读取存储数据"""
        with open(self.storage_file, 'r') as f:
            return json.load(f)

    def _write_data(self, date, count):
        """写入新数据"""
        with open(self.storage_file, 'w') as f:
            json.dump({'date': date, 'count': count}, f)

    def get_count(self):
        """获取并自增计数"""
        data = self._read_data()
        today = datetime.now().strftime('%Y-%m-%d')

        if data['date'] != today:
            # 新的一天重置计数
            new_count = 1
        else:
            # 同一天递增计数
            new_count = data['count'] + 1

        self._write_data(today, new_count)
        return new_count


    def format_number(self):
        """补齐两位数"""
        num = self.get_count()
        return str(num).zfill(2)


# 使用示例
if __name__ == "__main__":
    counter = DailyCounter()
    # 当天第一次调用
    print(counter.format_number())  # 输出：01

    # 当天第二次调用
    print(counter.format_number())  # 输出：02

    # 第二天调用（修改系统日期测试）
    # print(counter.get_count())  # 输出：1