import os

# 定义全国及地方岗位库
job_database = [
    # --- 新疆专区 ---
    {"title": "乌鲁木齐 · 货运司机 (管住)", "salary": "7000-10000/月", "source": "新疆人才网", "tags": ["乌鲁木齐", "B2/C1证", "物流运输"], "link": "https://www.xjhr.com/"},
    {"title": "昌吉工业区 · 生产普工/保安", "salary": "5000-6500/月", "source": "兵团就业网", "tags": ["昌吉", "包食宿", "五险一金"], "link": "http://btjy.xjbt.gov.cn/"},
    
    # --- 全国大厂 & 运营 ---
    {"title": "字节跳动 · 审核运营 (全国岗位)", "salary": "6000-9000/月", "source": "字节招聘", "tags": ["北京/西安/成都", "五险一金", "大厂背书"], "link": "https://job.bytedance.com/"},
    {"title": "小红书 · 社区运营 (实习/校招)", "salary": "200-300/天", "source": "大厂官网", "tags": ["上海/北京", "文职/运营", "免费三餐"], "link": "https://job.xiaohongshu.com/"},
    
    # --- Web3 & 远程金融 ---
    {"title": "Binance 商务助理 (Remote)", "salary": "3000-5000 USDT", "source": "A Better Web3", "tags": ["全球远程", "币安生态", "行政服务"], "link": "https://abetterweb3.notion.site/"},
    {"title": "Web3 交易研究员", "salary": "25K-45K", "source": "A Better Web3", "tags": ["远程办公", "数据分析", "英文流利"], "link": "https://abetterweb3.notion.site/"}
]

# 将数据转化为 HTML 卡片
all_jobs_html = ""
for job in job_database:
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in job['tags']])
    all_jobs_html += f"""
        <div class="job-card">
            <div class="card-top">
                <div class="title">{job['title']}</div>
                <div class="salary">{job['salary']}</div>
            </div>
            <div class="tags">
                <span class="tag tag-source">来自：{job['source']}</span>
                {tags_html}
            </div>
            <a href="{job['link']}" target="_blank" class="btn-apply">查看详情并申请</a>
        </div>
    """

# 读取并更新网页
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

placeholder = '<!-- 核心动态区：由后台脚本每小时自动注入数据 -->'
if placeholder in content:
    # 逻辑优化：每次更新前先重置动态区内容，避免重复堆叠
    parts = content.split(placeholder)
    # 重新拼接：头部 + 占位符 + 最新全量岗位 + 尾部
    new_content = parts[0] + placeholder + all_jobs_html + parts[1].split('</div>\n    </div>\n</div>', 1)[-1] 
    # 注意：上面的切割逻辑是为了确保 HTML 结构不乱，如果运行有问题，请告诉我
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
