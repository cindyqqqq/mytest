import streamlit as st

# 页面基础配置
st.set_page_config(page_title="简易音乐播放器", page_icon="", layout="centered")

# 音乐库数据（可自行替换成自己的歌曲信息）
music_library = [
    {
        "title": "花",
        "artist": "海洋Bo / 黄绮珊",
        "duration": "4：21",
        "audio_url": "https://music.163.com/song/media/outer/url?id=2756055504.mp3",  
        "cover_url": "http://p1.music.126.net/tOcMu6ZsnQ7BTKiiMm74Og==/109951172244995907.jpg?param=130y130" 
    },
    {
        "title": "给未来的自己",
        "artist": "余翊",
        "duration": "4:04",
        "audio_url": "https://music.163.com/song/media/outer/url?id=3327521028.mp3",
        "cover_url": "http://p2.music.126.net/Ke8Pljuxyshpx55cMIuWNA==/109951172459509491.jpg?param=130y130"
    },
    {
        "title": "苦海无涯",
        "artist": "法老 / Yoken_Official",
        "duration": "3：55",
        "audio_url": "https://music.163.com/song/media/outer/url?id=1465082816.mp3",
        "cover_url": "http://p2.music.126.net/HqEkuaWZfqnpci4EtxF41w==/109951165163056041.jpg?param=130y130"
    }
]

# 初始化会话状态，记录当前播放歌曲索引
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0

# 标题与简介
st.title(" 简易音乐播放器")
st.write("支持歌曲切换，展示专辑封面/歌手/歌名")

# 获取当前歌曲信息
current_music = music_library[st.session_state.current_idx]
total_musics = len(music_library)

# 布局：封面 + 歌曲标题
col1, col2 = st.columns([1, 2])
with col1:
    st.image(current_music["cover_url"], caption="专辑封面", width=200)
with col2:
    st.header(current_music["title"])
    st.write(f"歌手: {current_music['artist']}")
    st.write(f"时长: {current_music['duration']}")

# 音频播放组件
st.audio(current_music["audio_url"], format="audio/mp3")

# 切歌按钮
col_prev, col_next = st.columns(2)
with col_prev:
    if st.button("上一首"):
        st.session_state.current_idx = (st.session_state.current_idx - 1) % total_musics
        st.rerun()
with col_next:
    if st.button("下一首"):
        st.session_state.current_idx = (st.session_state.current_idx + 1) % total_musics
        st.rerun()
