import streamlit as st

def load_css():
    # 您可以从一个外部 CSS 文件加载样式
    # with open("path/to/your/style.css") as f:
    #     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # 或者直接在这里定义 CSS 样式
    custom_css = """
    <style>
        /* 全局字体 */
        body {
            font-family: 'Arial', sans-serif; /* 您可以选择更现代的字体 */
        }

        /* 侧边栏样式 */
        .css-1d391kg { /* Streamlit 侧边栏的特定类名，可能会随版本变化 */
            background-color: #f0f2f6; /* 淡灰色背景 */
        }
        
        /* 标题样式 */
        h1, h2, h3 {
            color: #2c3e50; /* 深蓝灰色 */
        }

        /* 链接样式 */
        a {
            color: #3498db; /* 蓝色链接 */
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
            color: #2980b9;
        }
        
        /* 按钮样式 - 示例 */
        .stButton>button {
            border-radius: 20px;
            border: 1px solid #3498db;
            background-color: white;
            color: #3498db;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #3498db;
            color: white;
        }
        
        /* 页脚样式 */
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #7f8c8d;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # 引入 Font Awesome 以便在联系页面使用图标
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        """, unsafe_allow_html=True)