import traceback
from theeye.celery import app
from event.serializers import EventSerializer

@app.task(queue='theEye')
def eventCreate(data, application_id):
    try:
        serializer = EventSerializer(data=data, context={'application_id': application_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return True
    except:
        print(traceback.format_exc())
