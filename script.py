import streamlit as st
from g4f.client import Client

# إعدادات الصفحة
st.set_page_config(page_title="Content Falcon AI", page_icon="🦅", layout="wide")

# العنوان الرئيسي
st.title("🦅 Content Falcon")
st.markdown("### ذكاء اصطناعي لصناعة المحتوى الاحترافي")

# القائمة الجانبية للإعدادات
with st.sidebar:
    st.header("⚙️ الإعدادات")
    platform = st.selectbox("المنصة المستهدفة:", ["فيسبوك", "لينكد إن", "تويتر (X)", "إنستغرام"])
    tone = st.selectbox("نبرة الصوت:", ["احترافية", "إبداعية", "حماسية", "ودودة"])
    num_posts = st.sidebar.slider("عدد المنشورات المطلوبة:", 1, 5, 3)
    st.markdown("---")
    st.write("تم التطوير بواسطة Content Falcon AI")

# واجهة إدخال البيانات
col1, col2 = st.columns([1, 1])

with col1:
    user_article = st.text_area("📄 الصق المقال أو النص هنا:", height=300,
                                placeholder="اكتب موضوعك هنا ليتم تحويله لبوستات...")
    generate_btn = st.button("🚀 توليد المحتوى الآن")

with col2:
    if generate_btn:
        if user_article.strip():
            with st.spinner("🧠 الصقر يحلل النص ويولد الأفكار..."):
                try:
                    client = Client()
                    # بناء الأوامر للذكاء الاصطناعي
                    prompt = f"أنت خبير تسويق رقمي. قم بتحويل النص التالي إلى {num_posts} منشورات لمنصة {platform}. " \
                             f"يجب أن تكون نبرة الصوت {tone}. أضف إيموجيات جذابة وهاشتاقات ترند:\n\n{user_article}"

                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    # عرض النتيجة
                    st.success("✨ تم صيد الأفكار بنجاح!")
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)

                except Exception as e:
                    st.error(f"حدث خطأ فني: {e}")
        else:
            st.warning("الرجاء إدخال نص المقال أولاً لتتم المعالجة!")

# تذييل الصفحة
st.markdown("---")
st.caption("Content Falcon AI v1.0 - 2026")