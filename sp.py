import streamlit as st

# 初始化会话状态
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 视频数据列表（可根据需要扩展集数）
video_arr = [
    {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "还珠格格第一部-第1集"},
    {"url": "https://www.w3schools.com/html/movie.mp4", "title": "还珠格格第一部-第2集"},
    {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4", "title": "还珠格格第一部-第3集"},
    {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4", "title": "还珠格格第一部-第4集"},
    {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "还珠格格第一部-第5集"},
    {"url": "https://www.w3schools.com/html/movie.mp4", "title": "还珠格格第一部-第6集"}
    ]

# 播放视频的函数
def playVideo(e):
    st.session_state['ind'] = int(e)

# 设置页面标题
st.title(video_arr[st.session_state['ind']]['title'])

# 显示当前选中的视频
st.video(video_arr[st.session_state['ind']]['url'])

# 每3集分一行的核心逻辑
batch_size = 3
# 按每3个元素分组
for start in range(0, len(video_arr), batch_size):
    # 截取当前批次的视频索引
    batch_indices = range(start, min(start + batch_size, len(video_arr)))
    # 创建对应数量的列
    cols = st.columns(len(batch_indices))
    # 循环将按钮放入列中
    for col, idx in zip(cols, batch_indices):
        with col:
            st.button(f'第{idx+1}集', on_click=playVideo, args=[idx])
