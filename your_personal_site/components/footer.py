import streamlit as st

def display_footer():
    st.markdown("---")
    footer_text = """
    <div style="text-align: center; padding: 10px;">
        <p>&copy; {current_year} 江浩然. 保留所有权利.</p>
        <p>
            <a href="mailto:jhr0124@foxmail.com">邮箱</a> | 
            <a href="https://www.linkedin.com/in/yourprofile/" target="_blank">领英</a> | 
            <a href="https://github.com/yourprofile" target="_blank">GitHub</a> (请替换链接)
        </p>
        <p>由 Streamlit 构建 🚀</p>
    </div>
    """.format(current_year="2025") # 您可以动态获取年份 import datetime; datetime.date.today().year
    st.markdown(footer_text, unsafe_allow_html=True)