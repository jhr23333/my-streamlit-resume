import streamlit as st

# --- 页面配置 (Page Config) ---
st.set_page_config(
    page_title="肖泽华 - 个人简历",
    page_icon="👨‍💻",  # Icon changed to be more tech-oriented
    layout="wide"
)

# --- 个人信息 (Personal Information) ---
st.title("肖泽华")
st.subheader("求职方向：产品经理")

st.markdown("---")

# --- 联系方式 (Contact Information) ---
# Source [1]
col1, col2 = st.columns(2)
with col1:
    st.subheader("📧 联系方式 (Contact)")
    st.markdown("**电话 (Phone/WeChat):** +86-15813700624") # 
    st.markdown("**邮箱 (Email):** szuxiaozehua@foxmail.com") # 
with col2:
    st.subheader("🗣️ 语言能力 (Languages)")
    # Source [3]
    st.markdown("- **中文 (Chinese):** 母语 (Native)")
    st.markdown("- **英语 (English):** IELTS 6.5, CET-6")
    st.markdown("- **粤语 (Cantonese):** 掌握 (Proficient)")


st.markdown("---")

# --- 教育背景 (Education) ---
st.header("🎓 教育背景 (Education)")

# Source [2]
st.subheader("香港中文大学 (The Chinese University of Hong Kong)")
st.markdown("**理学硕士 (M.Sc.):** 大数据营销 (Marketing Analytics), 商学院 (Business School)") # 
st.markdown("**时间 (Duration):** 2024.07 - 2025.08") # 

st.subheader("深圳大学 (Shenzhen University)")
st.markdown("**经济学学士 (Bachelor of Economics):** 国际经济与贸易 (International Economics and Trade), 经济学院 (College of Economics)") # 
st.markdown("**时间 (Duration):** 2020.09 - 2024.07") # 


st.markdown("---")

# --- 实习经历 (Internship Experience) ---
st.header("💼 实习经历 (Internship Experience)")

# Source [3]
# 实习 1: 腾讯音乐
st.subheader("腾讯音乐娱乐科技有限公司 (Tencent Music Entertainment)")
st.markdown("**职位 (Position):** 商业广告部—产品实习生 (Product Intern, Commercial Advertising Dept.)") # 
st.markdown("**时间 (Duration):** 2024.06 - 至今 (Present)") # 
st.markdown("""
- **核心职责 (Core Responsibility):** 拓展广告库存并提升转化效率，使QQ音乐网赚中心商业化广告收入提升超过50%。 
- **激励广告优化 (Incentive Ad Optimization):**
    - 针对电商与网服行业外，回退激励广告样式以调控过高的CTR，维护广告生态。 
    - 新增落地页二次激励功能，显著提升CVR约20%。 
- **新增广告玩法 (New Ad Features):**
    - 设计并上线“多条广告盲盒”玩法，日均提升广告收入2万元。 
    - 推出“看广告翻卡得金币”玩法，日均提升广告收入1.5万元。 
""")

# 实习 2: 百度
st.subheader("百度在线网络技术有限公司 (Baidu, Inc.)")
st.markdown("**职位 (Position):** 通用搜索组—产品实习生 (Product Intern, General Search Group)") # 
st.markdown("**时间 (Duration):** 2024.02 - 2024.05") # 
st.markdown("""
- **核心职责 (Core Responsibility):** 优化百度搜索阿拉丁及搜索策略，旨在提升人均停留时长、满意消费率和DAU。 
- **学术资源展现优化 (Academic Resource Display Optimization):** 优化了学术期刊官网在搜索结果中的展现样式与结构，实验数据显示核心指标均为正向。 
- **重复搜索体验优化 (Repeat Search Experience Optimization):**
    - 针对重复搜索场景，设计“常点内容前置”与“不点击内容折叠”功能。 
    - 策略上线后，用户换query率相对降低50%，满意消费率相对提升40%。 
- **搜索结果页推荐优化 (SERP Recommendation Optimization):**
    - 针对用户需求已在首位满足的场景，设计新的内容推荐策略与卡片样式。 
    - url点击量相对提升25%，人均停留时长相对增加35秒。 
""")

# 实习 3: 携程
st.subheader("上海携程国际旅行社有限公司 (Trip.com Group Ltd.)")
st.markdown("**职位 (Position):** 用车业务部—产品实习生 (Product Intern, Car Rental Business Dept.)") # 
st.markdown("**时间 (Duration):** 2023.09 - 2024.01") # 
st.markdown("""
- **核心职责 (Core Responsibility):** 完善用车后台产品功能，调整评分策略，以提升用户满意度与体验。 
- **司机好评机制优化 (Driver Rating System Optimization):**
    - 通过在司机端、乘客端和平台端的多项举措，限制和监测司机索要好评的行为。 
    - 最终实现司机索要好评相关的负面反馈相对下降80%。 
- **客服系统优化 (Customer Service System Optimization):**
    - 在包车售前环节增加FAQ自助问答和兜底功能，并优化服务商电话披露。 
    - 使得商家及时回复率相对提升34%，改善了客服响应效率。 
""")

st.markdown("---")

# --- 创业经历 (Entrepreneurial Experience) ---
st.header("🚀 创业经历 (Entrepreneurial Experience)")
# Source [3]
st.subheader("校园猎头平台创始人 (Founder of a Campus Headhunting Platform)")
st.markdown("**时间 (Duration):** 2023.09 - 至今 (Present)") # 
st.markdown("""
- **平台定位 (Platform Positioning):** 对接数百家知名企业的招聘需求，协助完成校园招聘。 
- **商业变现 (Monetization):** 通过推荐简历和候选人入职来支持企业招聘，个人累计实现40万+净收入，月均5万。 
""")

st.markdown("---")

# --- 技能总结 (Skills Summary) ---
st.header("🛠️ 个人技能 (Skills)")
# Source [3]
st.markdown("""
- **专业技能 (Professional Skills):**
    - **数据分析 (Data Analysis):** SQL, SPSS
    - **原型设计 (Prototyping):** 熟练使用相关工具进行产品原型设计。
    - **办公软件 (Office Suite):** 计算机二级MS Office良好证书 (National Computer Rank Examination Level 2 - MS Office Good)
- **证书及其他 (Certifications & Others):**
    - **财会 (Accounting):** 国际注册会计师考试已通过5门 (Passed 5 exams for ACCA)
""")

st.markdown("---")
st.caption("本简历由 Streamlit 生成 | Powered by Streamlit")

# To run this app:
# 1. Save this code as a Python file (e.g., resume_app.py).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: streamlit run resume_app.py