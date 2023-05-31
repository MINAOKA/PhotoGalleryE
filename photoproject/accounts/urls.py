from django.urls import path
# viewsモジュールをインポート
from.import views
# URLパターンを逆引きできるように名前をつける
app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # viewモジュールをインスタンス化する
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),
]



