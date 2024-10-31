import pymysql
pymysql.version_info=(1,4,3,"final",0) # 指定了pymysql的版本：1.4.3,按照你版本修改
pymysql.install_as_MySQLdb()


from .celery import app as celery_app
__all__ = ('celery_app',)
