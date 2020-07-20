from rest_framework.authtoken.models import Token

from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, BaseParser, FileUploadParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authentification.serializers import PatientRegistrationSerializer
from authentification.models import Subscriber
from .models import Traitement
from .permissions import IsOwnerOrReadOnly
from .serializers import TraitementSerializer
from rest_framework import viewsets, status


class TraitementView(CreateAPIView):
    serializer_class = TraitementSerializer
    permission_classes = (IsAuthenticated,)
    #parser_classes = (FileUploadParser)

    def get_queryset(self):
        traitement = Traitement.objects.all()
        return traitement

    def get(self, request):
        traitement = self.get_queryset()
        paginate_queryset = self.paginate_queryset(traitement)
        serializer = self.serializer_class(traitement, many=True)
        return Response(serializer.data)

    def post(self, request, *args,**kwargs):
        serializer = TraitementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_delete_update(RetrieveUpdateDestroyAPIView):
    serializer_class = TraitementSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            traitement = Traitement.objects.get(pk=pk)
        except Traitement.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return traitement

    def get(self, request, pk):

        traitement = self.get_queryset(pk)
        serializer = TraitementSerializer(traitement)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        traitement = self.get_queryset(pk)

        if (request.user.id == traitement.patient_id):  # If creator is who makes request
            serializer = TraitementSerializer(traitement, data=request.data)
            # if serializer.is_valid():
            serializer.save(patient_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):

        traitement = self.get_queryset(pk)

        if (request.user == traitement.doctor):  # If creator is who makes request
            traitement.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

class  UserTraitementViewSet(APIView):
    def get(self,request):
        usertraitement = Traitement.objects.filter(patient_id=request.user.id)
        return Response(TraitementSerializer(usertraitement,many=True).data)


class DoctorsViewSet(APIView):
    def get(self, request):
        doc_obj = Subscriber.objects.filter(role_subscriber=2)
        return Response(PatientRegistrationSerializer(doc_obj, many=True).data)


class PatientViewSet(APIView):
    def get(self, request):
        doc_obj = Subscriber.objects.filter(role_subscriber=1,patient_id=request.user.id)
        return Response(PatientRegistrationSerializer(doc_obj, many=True).data)






























# def post(self, request, format=None):
#     try:
#
#         serializer = TraitementSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     except Traitement.DoesNotExist:
#         raise Http404

# class TraitementAPIView(CreateAPIView):
#         serializer_class = PostSerializer
#         permission_classes = [IsAuthenticatedOrReadOnly, ]
#
#         serializer_class = TraitementSerializer
#
#         def create(self, request, *args, **kwargs):
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#
#             user = serializer.instance
#             token, created = Token.objects.get_or_create(user=user)
#             data = serializer.data
#             data["token"] = token.key
#
#             headers = self.get_success_headers(serializer.data)
#             return Response(data, status=status.HTTP_201_CREATED, headers=headers)
