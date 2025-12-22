import streamlit as st

st.set_page_config(page_title='动物相册', page_icon='🐒')

# 定义图片数据列表，包含图片URL和描述文本
image_ua = [
    {
        'url': 'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
        'text': '鸟'
    },
    {
        'url': 'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg',
        'text': '狗'
    },
    {
        'url': 'https://www.baltana.com/files/wallpapers-2/Cute-Cat-Images-07756.jpg',
        'text': '猫'
    },
]

# 初始化会话状态，用于保存当前显示的图片索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前索引对应的图片和标题
st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# 创建两列布局，分别放置“上一张”和“下一张”按钮
c1, c2 = st.columns(2)

# 定义“下一张”按钮的点击事件处理函数
def nextImg():
    # 取模运算实现循环切换（到最后一张后回到第一张）
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

# 定义“上一张”按钮的点击事件处理函数
def prevImg():
    # 取模运算实现循环切换（到第一张后回到最后一张）
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)

# 左列放置“上一张”按钮，并绑定点击事件
with c1:
    st.button('上一张', use_container_width=True, on_click=prevImg)

# 右列放置“下一张”按钮，并绑定点击事件
with c2:
    st.button('下一张', use_container_width=True, on_click=nextImg)
