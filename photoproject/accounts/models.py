from django.db import models
# AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    Userモデルを継承したカスタムユーザモデル
    '''
    pass

# Create your models here.
