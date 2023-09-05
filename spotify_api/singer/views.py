from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from spotify_api.singer.permissions import IsSinger, IsSingerOrAdminUser, IsSingerOwner

from spotify_api.singer.serializers import PlaylistSerializer, SingerReadUpdateSerializer, SingerCreateSerializer, SongSerializer
from spotify_api.singer.models import Playlist, Singer, Song

# Create your views here.

class SingerAPIViewSet(ModelViewSet):
    """Singer API View"""

    queryset = Singer.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in frozenset(['POST']):
            return SingerCreateSerializer
        return SingerReadUpdateSerializer

    def get_permissions(self):
        if self.action in {"me"}:
            return [IsSinger()]
        elif self.action in {"list", "retrieve", "create"}:
            return [AllowAny()]
        elif self.action in {"update", "partial_update", "destroy"}:
            return [IsSingerOwner()]
        else:
            return [IsAdminUser()]

    @action(detail=False, methods=["GET", "PUT", "PATCH"])
    def me(self, request: Request) -> Response:
        """Get or update the current singer."""
        singer = request.user.singer
        if request.method == "GET":
            serializer = SingerReadUpdateSerializer(singer, context={"request": request})
            return Response(serializer.data)
        elif request.method in frozenset(["PUT", "PATCH"]):
            serializer = SingerReadUpdateSerializer(singer, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class SongAPIViewSet(ModelViewSet):
    """Song API View"""

    queryset = Song.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SongSerializer
    pagination_class = None

    def get_permissions(self):
        if self.action in {"list", "retrieve"}:
            return [AllowAny()]
        else:
            return [IsSingerOrAdminUser()]

class PlaylistAPIViewSet(ModelViewSet):
    """Playlist API View"""

    queryset = Playlist.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PlaylistSerializer
    pagination_class = None

    def get_permissions(self):
        if self.action in {"list", "retrieve"}:
            return [AllowAny()]
        else:
            return [IsSingerOrAdminUser()]
