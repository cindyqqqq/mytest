import streamlit as st
import pandas as pd
import numpy as np
import base64

st.title("多功能Streamlit应用（选项卡版）")

# ===================== 创建6个选项卡 =====================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "学生数字档案", 
    "动物相册", 
    "南宁美食探", 
    "视频播放器", 
    "音乐播放器", 
    "个人简历生成器"
])

# ===================== 1. 选项卡1：学生数字档案 =====================
with tab1:
    st.header('学生 小满-数字档案')

    # ---------------------- 基础信息模块 ----------------------
    st.subheader('📌基础信息')
    st.caption('学生ID:NEO-2025-001')
    st.markdown('注册时间：:green[2025-12-18 15:09:10] | 精神状态:✅ 正常')
    st.markdown('当前位置：:green[实训楼710] | 安全等级：:green[绝密]')

    # ---------------------- 技能矩阵模块 ----------------------
    st.subheader("📊 技能矩阵")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption('C语言')
        st.markdown('#### 95%')
        st.write(":green[↑ 2%]")
    with col2:
        st.caption('Python')
        st.markdown('#### 87%')
        st.write(":red[↓ -1%]")
    with col3:
        st.caption('Java')
        st.markdown('#### 68%')
        st.write(":red[↓ -10%]")

    # ---------------------- 课程进度模块 ----------------------
    st.subheader("📚 Streamlit课程进度")
    st.markdown('###### Streamlit课程进度')
    st.progress(60)

    # ---------------------- 任务日志模块 ----------------------
    st.subheader("📋 任务日志")
    data = {
        '日期':["2023-10-01", "2023-10-12", "2023-10-20"],
        '任务':["学生数字档案", "课程管理系统", "数据可视化"],
        '状态':["✅ 完成", "● 进行中", "✕ 未完成"],
        '难度':["★★★☆☆", "★★☆☆☆", "★★★★☆"],
    }
    index = pd.Series(['0', '1', '2'], name='')
    df = pd.DataFrame(data, index=index)
    st.table(df)

    # ---------------------- 最新代码成果模块 ----------------------
    st.subheader("💻 最新代码成果")
    code = '''def detect_villain(avatar):
    if avatar == "black":
        detect_villain(1)
        return "ACCESS DENIED"
    else:
        allow_login()'''
    st.code(code, language="python")

    # ---------------------- 底部系统信息模块 ----------------------
    st.markdown('***')
    st.write("""
    - :green[SYSTEM MESSAGE:] 下一个任务目标已解锁。
    - :green[SYSTEM: ]课程管理系统
    - :green[CONTROL:] 2023-06-01 12:42:48
    - 系统状态：在线 排班表 已更新
    """)

# ===================== 2. 选项卡2：动物相册 =====================
with tab2:
    st.title("动物相册 🐒")

    # 定义图片数据列表
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

    # 初始化会话状态（添加tab2前缀避免冲突）
    if 'tab2_ind' not in st.session_state:
        st.session_state['tab2_ind'] = 0

    # 显示图片
    st.image(image_ua[st.session_state['tab2_ind']]['url'], caption=image_ua[st.session_state['tab2_ind']]['text'])

    # 按钮布局
    c1, c2 = st.columns(2)
    def tab2_nextImg():
        st.session_state['tab2_ind'] = (st.session_state['tab2_ind'] + 1) % len(image_ua)
    def tab2_prevImg():
        st.session_state['tab2_ind'] = (st.session_state['tab2_ind'] - 1) % len(image_ua)

    with c1:
        st.button('上一张', use_container_width=True, on_click=tab2_prevImg, key='tab2_prev')
    with c2:
        st.button('下一张', use_container_width=True, on_click=tab2_nextImg, key='tab2_next')

# ===================== 3. 选项卡3：南宁美食探 =====================
with tab3:
    st.title("南宁美食探")
    st.markdown('探索南宁地道美食店铺，让你的味蕾体验广西风味')

    # ---------------------- 数据准备模块 ----------------------
    shops = pd.DataFrame({
        "店铺名称": ["桂小厨(万象城店)", "南宁肥仔饭店(朝阳店)", "甘家界柠檬鸭(大学路店)", "复记老友粉(中山路店)", "粉之都(星光店)"],
        "评分": [4.8, 4.6, 4.7, 4.5, 4.4],
        "地址": ["青秀区民族大道136号", "兴宁区朝阳路65号", "西乡塘区大学东路100号", "青秀区中山路22号", "江南区星光大道34号"],
        "坐标": [(22.8170, 108.3668), (22.8285, 108.3428), (22.8060, 108.2745), (22.8150, 108.3400), (22.8020, 108.3450)]
    })

    score_data = shops[["店铺名称", "评分"]].set_index("店铺名称")
    price_type_data = pd.DataFrame({
        "类型": ["老友粉店", "柠檬鸭店", "广西菜餐厅", "粉面馆", "大排档"],
        "人均价格(元)": [18, 85, 68, 15, 55]
    }).set_index("类型")
    time_data = pd.DataFrame({
        "时段": ["08:00", "10:00", "12:00", "14:00", "18:00", "20:00", "22:00"],
        "本地食客": [60, 90, 220, 70, 260, 190, 110],
        "外地游客": [40, 70, 180, 50, 220, 160, 90]
    }).set_index("时段")
    months = [f"{m}月" for m in range(1, 13)]
    price_trend_data = pd.DataFrame({
        "月份": months,
        shops["店铺名称"][0]: np.linspace(65, 72, 12) + np.random.randn(12)*0.8,
        shops["店铺名称"][1]: np.linspace(58, 65, 12) + np.random.randn(12)*0.8,
        shops["店铺名称"][2]: np.linspace(75, 82, 12) + np.random.randn(12)*0.8,
        shops["店铺名称"][3]: np.linspace(15, 18, 12) + np.random.randn(12)*0.3,
        shops["店铺名称"][4]: np.linspace(12, 15, 12) + np.random.randn(12)*0.3
    }).set_index("月份")

    # ---------------------- 可视化展示 ----------------------
    st.subheader("📍 南宁美食地图")
    map_data = pd.DataFrame(
        [list(coord) for coord in shops["坐标"]],
        columns=["lat", "lon"],
        index=shops["店铺名称"]
    )
    st.map(map_data, zoom=12)

    st.subheader("⭐ 餐厅评分")
    st.bar_chart(score_data, color="#1E88E5")

    st.subheader("💰 不同类型餐厅价格")
    st.line_chart(price_type_data, color="#2196F3")

    st.subheader("⏰ 用餐高峰时段")
    st.area_chart(time_data, color=["#1E88E5", "#E53935"])

    st.subheader("📈 餐厅12个月价格走势")
    st.line_chart(price_trend_data)

# ===================== 4. 选项卡4：视频播放器 =====================
with tab4:
    st.title("视频播放器 🎬")

    # ---------- 会话状态初始化（添加tab4前缀） ----------
    if 'tab4_ind' not in st.session_state:
        st.session_state['tab4_ind'] = 0

    # ---------- 视频数据 ----------
    video_arr = [
        {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "还珠格格第一部-第1集"},
        {"url": "https://www.w3schools.com/html/movie.mp4", "title": "还珠格格第一部-第2集"},
        {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4", "title": "还珠格格第一部-第3集"},
        {"url": "https://media.w3.org/2010/05/sintel/trailer.mp4", "title": "还珠格格第一部-第4集"},
        {"url": "https://www.w3school.com.cn/example/html5/mov_bbb.mp4", "title": "还珠格格第一部-第5集"},
        {"url": "https://www.w3schools.com/html/movie.mp4", "title": "还珠格格第一部-第6集"}
    ]

    # ---------- 回调函数 ----------
    def tab4_playVideo(e):
        st.session_state['tab4_ind'] = int(e)

    # ---------- 视频播放区域 ----------
    st.title(video_arr[st.session_state['tab4_ind']]['title'])
    st.video(video_arr[st.session_state['tab4_ind']]['url'])

    # ---------- 选集按钮区域 ----------
    batch_size = 3
    for start in range(0, len(video_arr), batch_size):
        batch_indices = range(start, min(start + batch_size, len(video_arr)))
        cols = st.columns(len(batch_indices))
        for col, idx in zip(cols, batch_indices):
            with col:
                st.button(f'第{idx+1}集', on_click=tab4_playVideo, args=[idx], key=f'tab4_btn_{idx}')

# ===================== 5. 选项卡5：音乐播放器 =====================
with tab5:
    st.title("简易音乐播放器 🎵")
    st.write("支持歌曲切换，展示专辑封面/歌手/歌名")

    # 音乐库数据
    music_library = [
        {
            "title": "花",
            "artist": "海洋Bo / 黄绮珊",
            "duration": "4:21",
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
            "duration": "3:55",
            "audio_url": "https://music.163.com/song/media/outer/url?id=1465082816.mp3",
            "cover_url": "http://p2.music.126.net/HqEkuaWZfqnpci4EtxF41w==/109951165163056041.jpg?param=130y130"
        }
    ]

    # 初始化会话状态（添加tab5前缀）
    if "tab5_music_idx" not in st.session_state:
        st.session_state.tab5_music_idx = 0

    # 获取当前歌曲信息
    current_music = music_library[st.session_state.tab5_music_idx]
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

    # 切歌按钮（添加唯一key）
    col_prev, col_next = st.columns(2)
    with col_prev:
        if st.button("上一首", key='tab5_prev'):
            st.session_state.tab5_music_idx = (st.session_state.tab5_music_idx - 1) % total_musics
            st.rerun()
    with col_next:
        if st.button("下一首", key='tab5_next'):
            st.session_state.tab5_music_idx = (st.session_state.tab5_music_idx + 1) % total_musics
            st.rerun()

# ===================== 6. 选项卡6：个人简历生成器 =====================
with tab6:
    st.title("个人简历生成器 📄")
    st.text("使用Streamlit创建您的个性化简历")

    # 分栏布局：左侧表单，右侧预览
    c1, c2 = st.columns((1, 2))

    # 左侧：个人信息表单区域
    with c1:
        st.subheader("个人信息表单")
        # 基础信息输入
        name = st.text_input("姓名", key='tab6_name')
        zw = st.text_input("职位", key='tab6_zw')
        num = st.text_input("电话", key='tab6_num')
        yx = st.text_input("邮箱", key='tab6_yx')
        data = st.date_input("出生日期", value=None, key='tab6_birth')
        
        # 性别单选（横向排列）
        xb = st.radio("性别", ["男", "女", "其他"], index=0, horizontal=True, key='tab6_gender')
        
        # 学历下拉框
        xueli = st.selectbox("学历", ["高中", "大专", "本科", "硕士", "博士"], index=0, key='tab6_edu')
        
        # 语言能力多选
        language = st.multiselect("语言能力", ["中文", "英语", "日语", "韩语"], key='tab6_lang')
        
        # 技能多选
        skills = st.multiselect("技能（可多选）", ["Python", "Java", "HTML/CSS", "机器学习"], key='tab6_skills')
        
        # 工作经验滑块（0-30年）
        work_exp = st.slider("工作经验（年）", 0, 30, 0, key='tab6_exp')
        
        # 期望薪资滑块（0-50000元）
        exp_salary = st.slider("期望薪资范围（元）", 0, 50000, (10000, 20000), key='tab6_salary')
        
        # 个人简介文本域
        intro = st.text_area("个人简介", height=150, key='tab6_intro')
        
        # 最佳联系时间下拉
        contact_time = st.selectbox("每日最佳联系时间段", ["09:00", "20:44", "19:00-22:00"], index=1, key='tab6_time')
        
        # 图片上传组件
        st.subheader("上传个人照片")
        uploaded_file = st.file_uploader(
            "Drag and drop file here",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=False,
            help="Limit:200MB per file • JPG, JPEG, PNG",
            key='tab6_upload'
        )
        # 处理图片base64编码
        img_base64 = None
        if uploaded_file is not None:
            img_bytes = uploaded_file.read()
            img_base64 = base64.b64encode(img_bytes).decode()

    # 右侧：简历实时预览区域
    with c2:
        st.subheader("简历实时预览")
        st.markdown("---")
        
        # 照片显示
        if img_base64:
            st.image(f"data:image/png;base64,{img_base64}", width=120)
        else:
            st.image("https://via.placeholder.com/120", width=120)
        
        # 基础信息展示
        st.write(f"**姓名**: {name if name else '未填写'}")
        st.write(f"**职位**: {zw if zw else '未填写'}")
        st.write(f"**电话**: {num if num else '未填写'}")
        st.write(f"**邮箱**: {yx if yx else '未填写'}")
        st.write(f"**出生日期**: {data if data else '1990/01/01'}")
        
        # 基本信息栏
        st.markdown("### 基本信息")
        st.write(f"性别: {xb}")
        st.write(f"学历: {xueli}")
        st.write(f"工作经验: {work_exp}年")
        st.write(f"期望薪资: {exp_salary[0]}-{exp_salary[1]}元")
        st.write(f"最佳联系时间: {contact_time}")
        st.write(f"语言能力: {', '.join(language) if language else '未填写'}")
        
        # 个人简介
        st.markdown("### 个人简介")
        st.write(intro if intro else "这个人很神秘，没有留下任何介绍。")
        
        # 专业技能
        st.markdown("### 专业技能")
        st.write(', '.join(skills) if skills else "未填写")
        
        # 个性签名
        st.markdown("<p style='text-align: right; color: #888;'>\"代码改变世界，你改变代码\"</p>", unsafe_allow_html=True)
