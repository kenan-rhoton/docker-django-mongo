from django.test.simple import DiscoverRunner
from django.test import TestCase

class NoSQLTestRunner(DiscoverRunner):

    mongodb_name = 'test_django'

    def setup_databases(self, **kwargs):
        from mongoengine.connection import connect, disconnect
        disconnect()
        connect(self.mongodb_name, host='mongodb://mongo/' + self.mongodb_name )
        print('Creating mongo test database ' + self.mongodb_name)
        # return super(MongoTestRunner, self).setup_databases(**kwargs)

    def teardown_databases(self, old_config, **kwargs):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database(self.mongodb_name)
        print('Dropping mongo test database: ' + self.mongodb_name)
        disconnect()
        # super(MongoTestRunner, self).teardown_databases(old_config, **kwargs)


class NoSQLTestCase(TestCase):
    def _fixture_setup(self):
        pass
    def _fixture_teardown(self):
        from mongoengine.connection import get_connection, disconnect
        connection = get_connection()
        connection.drop_database('test_django')
