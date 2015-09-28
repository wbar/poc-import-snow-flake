from django.conf import settings


# noinspection PyMethodMayBeStatic,PyProtectedMember,PyUnusedLocal
class EtlRouter(object):
    """
    A router to ETL process
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'import_etl':
            return settings.ETL_DATABASE_ID
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'import_etl':
            return settings.ETL_DATABASE_ID
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'import_etl' and \
           obj2._meta.app_label == 'import_etl':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'import_etl':
            return db == settings.ETL_DATABASE_ID
        return None
