import streamlit as st
import g4f

# إعدادات الصفحة
st.set_page_config(page_title="Content Falcon", page_icon="🦅")

st.title("🦅 Content Falcon")
st.subheader("ذكاء اصطناعي لصناعة المحتوى الاحترافي")

# خانة إدخال النص
user_input = st.text_area("أدخل موضوع المقال أو النص هنا:", placeholder="...اكتب موضوعك هنا ليتم تحويله لبوستات")

if st.button("توليد المحتوى الآن 🚀"):
    if user_input:
        with st.spinner("جاري تحليق الصقر لتوليد محتواك..."):
            try:
                # التعديل هنا: اخترنا مزودين مستقرين وتجاوزنا الأخطاء
                response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_35_turbo,
                    messages=[{"role": "user", "content": f"اكتب لي محتوى احترافي ومنظم عن: {user_input}"}],
                    provider=g4f.Provider.Blackbox, # استخدمنا Blackbox لأنه مستقر جداً ولا يطلب API Key
                    stream=False,
                )
                
                st.success("تم توليد المحتوى بنجاح!")
                st.markdown("### المحتوى المقترح:")
                st.write(response)
                
            except Exception as e:
                st.error("حدث خطأ في الاتصال، جاري المحاولة بمزود آخر...")
                # محاولة ثانية بمزود احتياطي في حال فشل الأول
                try:
                    response = g4f.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": user_input}],
                        provider=g4f.Provider.DuckDuckGo,
                    )
                    st.write(response)
                except:
                    st.error("عذراً، جميع المصادر مزدحمة حالياً. حاول مرة أخرى بعد قليل.")
    else:
        st.warning("الرجاء كتابة موضوع أولاً!")

st.divider()
st.caption("Content Falcon AI v1.1 - 2026 | Prepared by Fadl Fouad Raheem")
