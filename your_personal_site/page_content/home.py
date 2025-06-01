import streamlit as st

def home_page():
    st.title("江浩然")
    st.subheader("求职方向：投资研究 / 战略咨询 / 市场分析") # 您可以根据实际情况修改
    
    st.markdown("---")
    st.markdown("""
    欢迎来到我的个人主页。我是一名对金融市场、企业战略和数据分析充满热情的应届毕业生。
    拥有在香港中文大学（深圳）市场营销硕士和东南大学工商管理学士的教育背景，
    以及在多家知名机构的投研和咨询实习经历。
    
    我致力于运用我的分析能力、行业洞察和学习热情，为企业创造价值。
    请通过导航栏浏览我的详细教育背景、实习经历、技能和联系方式。
    """)
    st.markdown("---")

    # 您可以在这里添加更多首页内容，例如个人简介的亮点或照片
    # col1, col2 = st.columns([1,2])
    # with col1:
        # st.image("path_to_your_profile_picture.jpg", width=200) # 替换为您的照片路径
    # with col2:
        # st.write("更多关于我的介绍...")