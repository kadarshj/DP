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
from .serializers import AssemblyWarehouseSerializer,SubWarehouseCustSerializer,AssemblyWarehouseStatusSerializer,CityWarehouseStatusSerializer,SubWarehouseStatusSerializer,AWPurifierTransportSerializer,AWReturnedSerializer,UserDetailsSerializer,CWPurifierUpdateSerializer,CityWarehouseSerializer,CWPurifierTransportSerializer,CWReturnedSerializer,SWPurifierUpdateSerializer,SWarehouseSerializer,SWPurifierTransportSerializer,SWReturnedSerializer,SWCustomerReceived,TotalCityWarehouseSerializer,TotalSubWarehouseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication, BasicAuthentication
from django.db.models import Count
from rest_framework.renderers import JSONRenderer

class AssemblyWarehousePurifierCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'aw_purifier_count': aw}
        return Response(content)

class AssemblyWarehousePurifierHoldCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.filter(is_in_transport = 'Hold').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'aw_purifier_count_Hold': aw}
        return Response(content)

class AssemblyWarehousePurifierTransitCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.filter(is_in_transport = 'Transit').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'aw_purifier_count_Transit': aw}
        return Response(content)


class AssemblyWarehousePurifierShiftedCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.filter(is_in_transport = 'Shifted').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'aw_purifier_count_Shifted': aw}
        return Response(content)


class AssemblyWarehousePurifierHold(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.filter(is_in_transport = 'Hold')
        serializer = AssemblyWarehouseStatusSerializer(aw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)

class AssemblyWarehousePurifierTransit(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.filter(is_in_transport = 'Transit')
        serializer = AssemblyWarehouseStatusSerializer(aw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)

class AssemblyWarehousePurifierShifted(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = AssemblyWarehouse.objects.filter(is_in_transport = 'Shifted')
        serializer = AssemblyWarehouseStatusSerializer(aw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)


class CityWarehousePurifierCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = CityWarehouse.objects.count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'cw_purifier_count': cw}
        return Response(content)

class CityWarehouseWisePurifierCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = AssemblyWarehouse.objects.values('cw_name').order_by('cw_name').annotate(the_count=Count('cw_name'))
       # serializer = AssemblyWarehouseSerializer(aw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(cw)

class CityWarehousePurifierHoldCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = CityWarehouse.objects.filter(is_in_transport = 'Hold').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'cw_purifier_count_Hold': cw}
        return Response(content)

class CityWarehousePurifierTransitCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = CityWarehouse.objects.filter(is_in_transport = 'Transit').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'cw_purifier_count_Transit': cw}
        return Response(content)


class CityWarehousePurifierShiftedCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = CityWarehouse.objects.filter(is_in_transport = 'Shifted').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'cw_purifier_count_Shifted': cw}
        return Response(content)


class CityWarehousePurifierHold(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = CityWarehouse.objects.filter(is_in_transport = 'Hold')
        serializer = CityWarehouseStatusSerializer(cw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)

class CityWarehousePurifierTransit(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = CityWarehouse.objects.filter(is_in_transport = 'Transit')
        serializer = CityWarehouseStatusSerializer(cw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)

class CityWarehousePurifierShifted(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        cw = CityWarehouse.objects.filter(is_in_transport = 'Shifted')
        serializer = CityWarehouseStatusSerializer(cw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)

#SubWarehouse


class SubWarehousePurifierCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'sw_purifier_count': sw}
        return Response(content)

class SubWarehouseWisePurifierCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = CityWarehouse.objects.values('sw_name').order_by('sw_name').annotate(the_count=Count('sw_name'))
       # serializer = AssemblyWarehouseSerializer(aw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(sw)

class SubWarehousePurifierHoldCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.filter(is_in_transport = 'Hold').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'sw_purifier_count_Hold': sw}
        return Response(content)

class SubWarehousePurifierTransitCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.filter(is_in_transport = 'Transit').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'sw_purifier_count_Transit': sw}
        return Response(content)


class SubWarehousePurifierShiftedCount(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.filter(is_in_transport = 'Shifted').count()
        #serializer = AssemblyWarehouseSerializer(aw, many=True)
        content = {'sw_purifier_count_Shifted': sw}
        return Response(content)


class SubWarehousePurifierHold(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.filter(is_in_transport = 'Hold')
        serializer = SubWarehouseStatusSerializer(sw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)

class SubWarehousePurifierTransit(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.filter(is_in_transport = 'Transit')
        serializer = SubWarehouseStatusSerializer(sw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)

class SubWarehousePurifierShifted(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.filter(is_in_transport = 'Shifted')
        serializer = SubWarehouseStatusSerializer(sw, many=True)
        #content = {'aw_purifier_count_Shifted': aw}
        return Response(serializer.data)


class CustomerDetails(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        sw = SubWarehouse.objects.all()
        serializer = SubWarehouseCustSerializer(sw, many=True)
        return Response(serializer.data)
