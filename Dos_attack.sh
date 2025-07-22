#### 本スクリプトは自己検証用で、外部攻撃は厳禁 ####

#!/bin/bash

# 送信する回数
TOTAL_REQUESTS=10000

# 並列で動かすプロセス数（高いほど負荷）
CONCURRENCY=10000

# 実際に送る関数
send_request() {
  curl -s -X POST -F "candidate_ids=1" http://localhost:8000/vote > /dev/null
}

# 並列に送信
for ((i=0; i<$TOTAL_REQUESTS; i++)); do
  send_request &  # バックグラウンドで並列実行
  if (( i % CONCURRENCY == 0 )); then
    wait  # 一定数ごとに待つ（リソース食いすぎ防止）
  fi
done

wait  # 残りを待つ
echo "Finished sending $TOTAL_REQUESTS requests with $CONCURRENCY concurrency."
