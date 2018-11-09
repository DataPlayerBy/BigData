from pyhive import hive
from TCLIService.ttypes import TOperationState


# # synchronize
# cursor = hive.connect(host='192.168.1.190', port='10000', database='ods_crawler').cursor()
# cursor.execute('select * from crawler_weibo_account_info limit 10')
# print(cursor.fetchall())

# asynchronous
cursor = hive.connect(host='192.168.1.190', port='10000', database='ods_crawler').cursor()
cursor.execute('select * from crawler_weibo_account_info limit 10000', async_=True)
status = cursor.poll().operationState
while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
    logs = cursor.fetch_logs()
    for message in logs:
        print(message)
    status = cursor.poll().operationState
for result in cursor.fetchall():
    print(result)
