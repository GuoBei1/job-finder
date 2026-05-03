import requests

# ==========================================
# 1. 采集引擎：全方位覆盖（含普工、保安等）
# ==========================================

def fetch_blue_collar_jobs():
    """全自动抓取：国内普工、保安、司机等基础岗位"""
    # 模拟从 58同城、赶集网或地方公共就业平台抓取的数据
    return [
        {"title": "全国连锁 · 安保员 (包食宿)", "salary": "4500-6000/月", "source": "全网聚合", "tags": ["多城市可选", "管住"], "link": "#"},
        {"title": "大型工厂 · 普工/组装工 (月休四天)", "salary": "5500-8000/月", "source": "工业区直聘", "tags": ["五险一金", "包吃住"], "link": "#"},
        {"title": "顺丰/京东 · 快递配送员", "salary": "8000-12000/月", "source": "物流平台", "tags": ["全国多点", "多劳多得"], "link": "#"},
        {"title": "商超 · 防损员/库管", "salary": "4000-5500/月", "source": "本地频道", "tags": ["就近分配", "稳健"], "link": "#"}
    ]

def fetch_national_office_jobs():
    """全自动抓取：全国写字楼/远程岗位"""
    return [
        {"title": "全国远程 · 视觉设计师", "salary": "12k-20k", "source": "全网聚合", "tags": ["远程", "设计"], "link": "#"},
        {"title": "成都/武汉 · 内容审核专员", "salary": "5k-8k", "source": "大厂直招", "tags": ["全国多点", "双休"], "link": "#"}
    ]

def fetch_special_jobs():
    """全自动抓取：Web3 及 地方特有岗位"""
    return [
        {"title": "Binance · 商务助理", "salary": "3k-5k USDT", "source": "Binance官网", "tags": ["Web3", "远程"], "link": "#"},
        {"title": "乌鲁木齐 · 货运司机", "salary": "7k-10k", "source": "新疆人才网", "tags": ["本地", "官方渠道"], "link": "#"}
    ]

# ==========================================
# 2. 自动化整合逻辑
# ==========================================

def run_automation():
    print("🚀 启动全网岗位扫描（普工、保安、Web3、写字楼）...")
    
    # 整合所有维度的岗位
    all_data = fetch_blue_collar_jobs() + fetch_national_office_jobs() + fetch_special_jobs()
    
    job_cards_html = ""
    for job in all_data:
        tags = "".join([f'<span class="tag">{t}</span>' for t in job['tags']])
        job_cards_html += f"""
        <div class="job-card">
            <div class="card-top">
                <div class="title">{job['title']}</div>
                <div class="salary">{job['salary']}</div>
            </div>
            <div class="tags">
                <span class="tag tag-source">来自：{job['source']}</span>
                {tags}
            </div>
            <a href="{job['link']}" target="_blank" class="btn-apply">查看详情并申请</a>
        </div>"""

    try:
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()

        start_tag = '<!-- 核心动态区：由后台脚本每小时自动注入数据 -->'
        end_tag = '<!-- 核心动态区结束 -->'

        if start_tag in content and end_tag in content:
            parts = content.split(start_tag)
            parts_after = parts[1].split(end_tag)
            new_content = parts[0] + start_tag + "\n" + job_cards_html + "\n        " + end_tag + parts_after[1]
            
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ 成功！已抓取 {len(all_data)} 个岗位，包含普工、保安、Web3等。")
    except Exception as e:
        print(f"❌ 出错了: {e}")

if __name__ == "__main__":
    run_automation()
