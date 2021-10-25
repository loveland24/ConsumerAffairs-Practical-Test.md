# ConsumerAffairs-Practical-Test.md

## Application will be provided an API Key in order to be authenticated (trusted)<br>
- can be created via POST: /user/ by an authenticated user
- or via `python manage.py createsuperuser`
- if created via console, a token will need to be generated via <br> 
```
from rest_framework.authtoken.models import Token
token = Token.objects.create(user=...)
print(token.key)
```

### Application should pass the token key in the Authorization HTTP header, for example:
`Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

### Application can either submit a new session id with an event, or create one via:
- POST: /session/

#Endpoints
- /event/ (list all events)
- /event/[INT]/ (list event by ID)
- /session/ (list all sessions)
- /session/[STR]/ (list session by ID)

##Filtering
## Event:
- session (ie. /event/?session=e2085be5-9137-4e4e-80b5-f1ffddc25423)
- category (ie. /event/?category=page%20interaction)
- timestamp (ie. /event/?timestamp_gte=2021-10-01%2000:00:00.000000&timestamp_lte=2021-10-31%2000:00:00.000000)