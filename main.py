import os
from anthropic import Anthropic

# هنا نطلب من السكربت أن يبحث عن المفتاح السري في إعدادات السحابة المخفية
# ولذلك لن نكتب المفتاح السري هنا أبداً لحمايته
my_secret_key = os.getenv("CLAUDE_API_KEY")

# إعداد الاتصال بكلود
client = Anthropic(api_key=my_secret_key)

def test_cloud_connection():
    print("جاري إرسال أول رسالة إلى كلود من السحابة...")
    
    # إرسال رسالة بسيطة للتجربة
    response = client.messages.create(
        model="claude-3-haiku-20240307", 
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": "مرحباً كلود، أنا المهندس إبراهيم وهذه أول رسالة تجريبية أرسلها لك من الخادم السحابي. أجبني بترحيب قصير جداً."
            }
        ]
    )
    
    # طباعة الرد
    print("\n✅ الرد وصل بنجاح:")
    print(response.content[0].text)

# تشغيل التجربة
if __name__ == "__main__":
    test_cloud_connection()