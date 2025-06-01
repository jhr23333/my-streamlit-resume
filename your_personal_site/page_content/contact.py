import streamlit as st

def contact_page():
    st.header("📞 联系方式 (Contact Me)")
    
    st.subheader("欢迎与我联系！")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # st.image("path_to_your_contact_image_or_icon.png", width=150) # 可选：添加一个图标或图片
        st.markdown("### 江浩然")

    with col2:
        st.markdown("""
        <i class="fas fa-envelope"></i> **邮箱 (Email):** <a href="mailto:jhr0124@foxmail.com">jhr0124@foxmail.com</a><br>
        <i class="fas fa-phone"></i> **电话 (Phone):** +86 188-5189-7395<br>
        
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("留言给我 (Leave a Message)")
    
    # 简单的联系表单示例 (数据不会实际发送，仅为前端展示)
    with st.form(key="contact_form"):
        name = st.text_input("您的姓名 (Your Name)")
        email = st.text_input("您的邮箱 (Your Email)")
        message = st.text_area("留言内容 (Message)")
        submit_button = st.form_submit_button(label="发送 (Send)")
        
        if submit_button:
            if name and email and message:
                st.success(f"感谢您的留言，{name}！我会尽快回复您。 (模拟发送)")
                # 实际应用中，这里可以接邮件发送服务或后端API
            else:
                st.error("请填写所有必填项。")
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        """, unsafe_allow_html=True) # 添加 Font Awesome 图标库