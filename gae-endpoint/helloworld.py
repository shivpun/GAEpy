
from google.appengine.ext import ndb, endpoints
from protorpc import messages, remote

class Task(messages.Message):
    name = messages.StringField(1, required=True)
    owner = messages.StringField(2)
    
    
class TaskList(messages.Message):
    items = messages.MessageField(Task, 1, repeated=True)

@endpoints.api(name='tasks', version='v1', description="Task Api Management")
class TaskApi(remote.Service):
    
    @endpoints.method(Task, Task, name='task.insert', path='task',  http_method='POST')
    def insert_task(self, request):
        print request
        return request
    
    
application=endpoints.api_server([TaskApi])