import streamlit as st

def skills_activities_page():
    st.header("🛠️ 技能总结 (Skills)")
    
    col_skill1, col_skill2 = st.columns(2)
    with col_skill1:
        st.subheader("💻 技术与分析技能")
        st.markdown("""
        - **数据分析 & 编程:** Python (Pandas, NumPy, Scikit-learn), SQL, R
        - **金融建模与估值:** DCF, LBO, Comps, Financial Statement Analysis
        - **商业软件:** MS Office Suite (Excel, PowerPoint, Word), Tableau (初级)
        - **AI 工具:** ChatGPT, DeepSeek, Midjourney
        - **数据库:** MySQL (基础)
        """)
    with col_skill2:
        st.subheader("🗣️ 语言与软技能")
        st.markdown("""
        - **语言:**
            - 普通话 (母语)
            - 英语 (雅思 7.0, GMAT 700, 流利听说读写)
            - 粤语 (日常交流)
        - **软技能:**
            - 逻辑思维与问题解决
            - 沟通表达与团队协作
            - 快速学习与适应能力
            - 信息搜集与研究能力
            - 组织协调与项目管理
        """)
    st.markdown("---")

    st.header("🌳 校园经历与荣誉 (Campus Experience & Honors)")
    st.subheader("东南大学校辩论队 (Southeast University Debate Team)")
    st.markdown("**职位 (Role):** 副队长 (Vice Captain)")
    st.markdown("**时间 (Duration):** 2020年9月 - 2023年6月")
    st.markdown("""
    - **能力塑造 (Skills Developed):**
        - 培养了细致的信息检索和各类数据、材料搜集能力。
        - 训练了优秀的公开演讲、临场应变和缜密的逻辑思维能力。
        - 展现了优秀的沟通、组织和团队协作能力。
    - **成绩荣誉 (Achievements/Honors):**
        - 2022年东南大学“至善杯”辩论赛冠军
        - 多次获得“最佳辩手”称号
    """)
    st.markdown("""
    - **其他荣誉与活动:**
        - 东南大学优秀学生干部
        - 多次获得校级奖学金
        - 参与组织多项校园文化活动
    """) # 您可以根据实际情况补充