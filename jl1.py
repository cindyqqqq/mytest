import streamlit as st
import base64

# 页面基础配置
st.set_page_config(page_title="个人简历生成器", layout="wide", initial_sidebar_state="collapsed")
st.title("个人简历生成器")
st.text("使用Streamlit创建您的个性化简历")

# 分栏布局：左侧表单，右侧预览
c1, c2 = st.columns((1, 2))

# 左侧：个人信息表单区域
with c1:
    st.subheader("个人信息表单")
    # 基础信息输入（移除placeholder）
    name = st.text_input("姓名")
    zw = st.text_input("职位")
    num = st.text_input("电话")
    yx = st.text_input("邮箱")
    data = st.date_input("出生日期", value=None)
    
    # 性别单选（横向排列）
    xb = st.radio("性别", ["男", "女", "其他"], index=0, horizontal=True)
    
    # 学历下拉框
    xueli = st.selectbox("学历", ["高中", "大专", "本科", "硕士", "博士"], index=0)
    
    # 语言能力多选（移除placeholder）
    language = st.multiselect("语言能力", ["中文", "英语", "日语", "韩语"])
    
    # 技能多选（移除placeholder）
    skills = st.multiselect("技能（可多选）", ["Python", "Java", "HTML/CSS", "机器学习"])
    
    # 工作经验滑块（0-30年）
    work_exp = st.slider("工作经验（年）", 0, 30, 0)
    
    # 期望薪资滑块（0-50000元，默认区间10000-20000）
    exp_salary = st.slider("期望薪资范围（元）", 0, 50000, (10000, 20000))
    
    # 个人简介文本域（移除placeholder）
    intro = st.text_area("个人简介", height=150)
    
    # 最佳联系时间下拉
    contact_time = st.selectbox("每日最佳联系时间段", ["09:00", "20:44", "19:00-22:00"], index=1)
    
    # 图片上传组件
    st.subheader("上传个人照片")
    uploaded_file = st.file_uploader(
        "Drag and drop file here",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False,
        help="Limit:200MB per file • JPG, JPEG, PNG"
    )
    # 处理图片base64编码（用于预览）
    img_base64 = None
    if uploaded_file is not None:
        img_bytes = uploaded_file.read()
        img_base64 = base64.b64encode(img_bytes).decode()

# 右侧：简历实时预览区域
with c2:
    st.subheader("简历实时预览")
    st.markdown("---")
    
    # 照片显示在姓名上方
    if img_base64:
        st.image(f"data:image/png;base64,{img_base64}", width=120)
    else:
        # 占位头像
        st.image("https://via.placeholder.com/120", width=120)
    
    # 基础信息展示
    st.write(f"**姓名**: {name if name else '未填写'}")
    st.write(f"**职位**: {zw if zw else '未填写'}")
    st.write(f"**电话**: {num if num else '未填写'}")
    st.write(f"**邮箱**: {yx if yx else '未填写'}")
    st.write(f"**出生日期**: {data if data else '1990/01/01'}")
    
    # 右侧信息栏
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
    
    # 个性签名（右下角）
    st.markdown("<p style='text-align: right; color: #888;'>\"代码改变世界，你改变代码\"</p>", unsafe_allow_html=True)
