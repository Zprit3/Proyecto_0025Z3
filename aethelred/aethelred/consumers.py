from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import AnonymousUser
import json

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Obtener el token JWT de los parámetros de la conexión
        token = self.scope['query_string'].decode('utf-8').split('=')[1]

        try:
            # Validar el token
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            self.scope['user'] = await self.get_user(user_id)
            await self.accept()
        except Exception as e:
            print("Error de autenticación:", e)
            await self.close()

    async def get_user(self, user_id):
        # Obtener el usuario desde la base de datos
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return await User.objects.get(id=user_id)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': f"Usuario {self.scope['user'].username} dice: {message}"
        }))