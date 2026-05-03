import os

# 模拟抓取到的真实岗位数据（后续我会为你接入实时API）
new_jobs_html = """
        <div class="job-card">
            <div class="card-top">
                <div class="title">小红书·社区运营（实习/校招）</div>
                <div class="salary">200-300/天</div>
            </div>
            <div class="tags">
                <span class="tag tag-source">来源：大厂官网</span>
                <span class="tag">上海/北京</span>
                <span class="tag">文职/运营</span>
            </div>
            <a href="https://job.xiaohongshu.com/" target="_blank" class="btn-apply">查看并申请</a>
        </div>
        <div class="job-card">
            <div class="card-top">
                <div class="title">Binance 商务助理（Remote）</div>
                <div class="salary">3000 - 5000 USDT</div>
            </div>
            <div class="tags">
                <span class="tag tag-source">来源：A Better Web3</span>
                <span class="tag">全球远程</span>
                <span class="tag">币安生态</span>
                <span class="tag">行政服务</span>
            </div>
            <a href="https://abetterweb3.notion.site/" target="_blank" class="btn-apply">查看并申请</a>
        </div>
"""

# 读取原始网页并替换占位内容
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 定位到 jobContainer 并注入新卡片
if '<!-- 核心动态区：由后台脚本每小时自动注入数据 -->' in content:
    updated_content = content.replace(
        '<!-- 核心动态区：由后台脚本每小时自动注入数据 -->',
        '<!-- 核心动态区：由后台脚本每小时自动注入数据 -->' + new_jobs_html
    )
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated_content)
