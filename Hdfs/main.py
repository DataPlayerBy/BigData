import requests

# webhdfs
# stream_response = requests.get("http://192.168.1.193:50070/webhdfs/v1/tech/azkaban/data_processing/feature_generator/wechat_oa/snbt/data/wechat_oa_account_rank_score_and_snbt_v1.0_20180901?op=OPEN", stream=True)
# httpfs
stream_response = requests.get("http://192.168.1.192:14000/webhdfs/v1/tech/azkaban/data_processing/feature_generator/wechat_oa/snbt/data/wechat_oa_account_rank_score_and_snbt_v1.0_20180901?op=OPEN&user.name=gaojingbin", stream=True)
i = 0
for line in stream_response.iter_lines():
    print(line)
    print(bytes.decode(line))
    print(str(line, encoding="utf-8"))
    i += 1
    print(i)
