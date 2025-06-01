import streamlit as st
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

# 必须是第一个 Streamlit 命令
st.set_page_config(page_title="江浩然 - 个人主页", layout="wide", page_icon="👨‍💻")

# 从新目录导入页面
# 注意：我们将 resume_page 的内容拆分到 skills_activities.py 和 contact.py 中
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.skills_activities import skills_activities_page # 替换之前的 resume_page
from page_content.contact import contact_page

# 导入组件
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # 加载自定义 CSS
        load_css() # 您提供的示例中包含这个

        st.sidebar.image("https://www.cuhk.edu.cn/sites/cuhk.edu.cn/files/logo_whole_スクリーン%20ショット%202023-01-16%2011.24.19_0.png", width=200) # 示例图片，您可以替换成自己的头像或校徽
        st.sidebar.markdown("## 导航菜单")
        app_selection = st.sidebar.radio(
            "选择页面", self.apps, format_func=lambda app_item: app_item["title"]
        )
        st.sidebar.markdown("---")
        st.sidebar.info("""
        **江浩然**
        \n[jhr0124@foxmail.com](mailto:jhr0124@foxmail.com)
        \n求职意向：投研/咨询
        """)


        # 运行选中的应用函数
        for app_item in self.apps:
            if app_item["title"] == app_selection["title"]:
                app_item["function"]()
                break
        
        # 在每个页面底部显示页脚
        display_footer()

# 初始化应用
main_app = MultiApp()

# 添加页面到应用中
# 顺序会影响侧边栏的显示顺序
main_app.add_app("🏠 首页", home_page)
main_app.add_app("🎓 教育背景", education_page)
main_app.add_app("💼 实习经历", experience_page)
main_app.add_app("🛠️ 技能与活动", skills_activities_page) # 使用新的页面
main_app.add_app("📞 联系方式", contact_page)


# 运行应用
main_app.run()