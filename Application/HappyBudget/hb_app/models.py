# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Goals(models.Model):
    goal_id = models.IntegerField(db_column='Goal_ID', primary_key=True)  # Field name made lowercase.
    goal_name = models.CharField(db_column='Goal_name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    goal_target = models.TextField(db_column='Goal_target', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    goal_current = models.TextField(db_column='Goal_current', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Goals'


class Transactions(models.Model):
    transaction_id = models.IntegerField(db_column='transaction_ID', primary_key=True)  # Field name made lowercase.
    transaction_date = models.DateTimeField(blank=True, null=True)
    transaction_amt = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Transactions'


class Users(models.Model):
    user_id = models.IntegerField(db_column='user_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(max_length=40, blank=True, null=True)
    user_password = models.CharField(max_length=40, blank=True, null=True)
    user_email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'

'''
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FirstAppAccessrecord(models.Model):
    date = models.DateField()
    name = models.ForeignKey('FirstAppWebpage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'first_app_accessrecord'


class FirstAppTopic(models.Model):
    top_name = models.CharField(max_length=264)

    class Meta:
        managed = False
        db_table = 'first_app_topic'


class FirstAppWebpage(models.Model):
    name = models.CharField(unique=True, max_length=264)
    url = models.CharField(unique=True, max_length=200)
    topic = models.ForeignKey(FirstAppTopic, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'first_app_webpage'
'''