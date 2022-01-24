from enum import auto
from django.db import models
from django.db.models.fields import CharField, IntegerField,DateField,TextField

class FundingBoard(models.Model):

    board_id = IntegerField(primary_key=True)
    user_id = CharField(max_length=30)

    title = CharField(max_length=255, null=True)
    category = CharField(max_length=30, null=True)
    language_text = CharField(max_length=30, null=True)
    target = CharField(max_length=30, null=True)
    intro = TextField(null=True)
    file_name = CharField(max_length=30, null=True)
    background_text = CharField(max_length=200, null=True)
    object_text = CharField(max_length = 200, null=True)
    develop_content = CharField(max_length=200, null=True)

    fund_goal_price = IntegerField()
    fund_total_price = IntegerField()
    regi_date = DateField(null=True)

    
    class Meta:
        db_table = 'FundingBoard'
        app_label = 'fundingapp'
        managed = False


class User1(models.Model):

    user_id = CharField(max_length=30, primary_key=True)
    user_pw = CharField(max_length=30)
    user_name = CharField(max_length = 30)
    user_email = CharField(max_length=30)


    
    class Meta:
        db_table = 'User'
        app_label = 'fundingapp'
        managed = False


class JoinFund(models.Model):
    id = IntegerField(primary_key=True, auto_created=True)
    user_id = CharField(max_length=30)
    board_id = IntegerField()
    fund_price = IntegerField()


    
    class Meta:
        db_table = 'JoinFund'
        app_label = 'fundingapp'
        managed = False

class FundingFunc(models.Model):

    board_id = IntegerField(primary_key=True)
    func_a_price = IntegerField()
    func_b_price = IntegerField()
    func_c_price = IntegerField()

    class Meta:
        db_table = 'FundingFunc'
        app_label = 'fundingapp'
        managed = False

class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()