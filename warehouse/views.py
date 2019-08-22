from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from .models import AssemblyWarehouse,CityWarehouse,SubWarehouse,User, TotalCityWarehouse, TotalSubWarehouse
from .serializers import AssemblyWarehouseSerializer,AWPurifierTransportSerializer,AWReturnedSerializer,UserDetailsSerializer,CWPurifierUpdateSerializer,CityWarehouseSerializer,CWPurifierTransportSerializer,CWReturnedSerializer,SWPurifierUpdateSerializer,SWarehouseSerializer,SWPurifierTransportSerializer,SWReturnedSerializer,SWCustomerReceived,TotalCityWarehouseSerializer,TotalSubWarehouseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
# Create your views here.

class AssemblyWarehouseList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.all()
        serializer = AssemblyWarehouseSerializer(aw, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssemblyWarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssemblyWarehouseDetails(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, pk):
        try:
            return AssemblyWarehouse.objects.get(pk=pk)
        except AssemblyWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        aw = self.get_object(pk)
        serializer = AssemblyWarehouseSerializer(aw)
        #return Response({"message":"success","Result":serializer.data})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        aw = self.get_object(pk)
        serializer = AssemblyWarehouseSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadyForTransportCityWarehouse(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return AssemblyWarehouse.objects.get(purifierid=purifierid)
        except AssemblyWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = AWPurifierTransportSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = AWPurifierTransportSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurifierReturned(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return AssemblyWarehouse.objects.get(purifierid=purifierid)
        except AssemblyWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = AWReturnedSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = AWReturnedSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        aw = self.get_object(email)
        serializer = UserDetailsSerializer(aw)
        return Response(serializer.data)


class PurifierShiftedCityWarehouse(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return AssemblyWarehouse.objects.get(purifierid=purifierid)
        except AssemblyWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = CWPurifierUpdateSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = CWPurifierUpdateSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityWarehouseList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = CityWarehouse.objects.all()
        serializer = CityWarehouseSerializer(aw, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CityWarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReadyForTransportSubWarehouse(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return CityWarehouse.objects.get(purifierid=purifierid)
        except CityWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = CWPurifierTransportSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = CWPurifierTransportSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CWPurifierReturned(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return CityWarehouse.objects.get(purifierid=purifierid)
        except CityWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = CWReturnedSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = CWReturnedSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurifierShiftedSubWarehouse(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return CityWarehouse.objects.get(purifierid=purifierid)
        except CityWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWPurifierUpdateSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWPurifierUpdateSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubWarehouseList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = SubWarehouse.objects.all()
        serializer = SWarehouseSerializer(aw, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SWarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReadyForTransportCustomer(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return SubWarehouse.objects.get(purifierid=purifierid)
        except SubWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWPurifierTransportSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWPurifierTransportSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SWPurifierReturned(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return SubWarehouse.objects.get(purifierid=purifierid)
        except SubWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWReturnedSerializer(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWReturnedSerializer(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurifierReceivedByCustomer(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get_object(self, purifierid):
        try:
            return SubWarehouse.objects.get(purifierid=purifierid)
        except SubWarehouse.DoesNotExist:
            raise Http404

    def get(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWCustomerReceived(aw)
        return Response(serializer.data)

    def put(self, request, purifierid, format=None):
        aw = self.get_object(purifierid)
        serializer = SWCustomerReceived(aw, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TotalCityWarehouseDetails(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get(self, request, format=None):
        aw = TotalCityWarehouse.objects.all()
        serializer = TotalCityWarehouseSerializer(aw, many=True)
        return Response(serializer.data)


class TotalSubWarehouseDetails(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    authentication_classes = (TokenAuthentication,SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def get(self, request, format=None):
        aw = TotalSubWarehouse.objects.all()
        serializer = TotalSubWarehouseSerializer(aw, many=True)
        return Response(serializer.data)
