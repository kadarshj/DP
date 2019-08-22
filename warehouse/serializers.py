from warehouse.models import User
from rest_framework import serializers
from .models import AssemblyWarehouse, CityWarehouse, SubWarehouse, TotalCityWarehouse,TotalSubWarehouse
from django.contrib.auth import authenticate

class AssemblyWarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssemblyWarehouse
        fields = ('purifierid','aw_manager','aw_executive','location','address','user')
        #fields = '__all__'
        #extra_kwargs = {'user': {'required': False}}
        read_only_fields = ('user',)

class AWPurifierTransportSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssemblyWarehouse
        fields = ('purifierid','is_in_transport','transport_person_name','cw_name','start_transport')

class AWReturnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssemblyWarehouse
        fields = ('purifierid','is_returned','returned_from','is_device_ok','return_time')

class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','is_aw_manager','is_cw_manager','is_sw_manager','is_aw_executive','is_cw_executive','is_sw_executive','is_aw_transport','is_cw_transport','is_sw_transport')

class CWPurifierUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssemblyWarehouse
        fields = ('purifierid','is_in_transport','is_in_citywarehouse','end_transport')

class CityWarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityWarehouse
        fields = ('purifierid','cw_manager','cw_executive','location','address','user')
        #fields = '__all__'
        #extra_kwargs = {'user': {'required': False}}
        read_only_fields = ('user',)

class CWPurifierTransportSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityWarehouse
        fields = ('purifierid','is_in_transport','transport_person_name','sw_name','start_transport')

class CWReturnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityWarehouse
        fields = ('purifierid','is_returned','returned_from','is_device_ok','return_time')


class SWPurifierUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityWarehouse
        fields = ('purifierid','is_in_transport','is_in_subwarehouse','end_transport')

class SWarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubWarehouse
        fields = ('purifierid','sw_manager','sw_executive','location','address','user')
        #fields = '__all__'
        #extra_kwargs = {'user': {'required': False}}
        read_only_fields = ('user',)

class SWPurifierTransportSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubWarehouse
        fields = ('purifierid','is_in_transport','transport_person_name','start_transport')

class SWReturnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubWarehouse
        fields = ('purifierid','is_returned','returned_from','is_device_ok','return_time')

class SWCustomerReceived(serializers.ModelSerializer):

    class Meta:
        model = SubWarehouse
        fields = ('purifierid','is_in_transport','cust_name','cust_phoneno','end_transport','customer_transport')

class TotalCityWarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalCityWarehouse
        fields = '__all__'
        read_only_fields = ('user',)


class TotalSubWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalSubWarehouse
        fields = '__all__'
        read_only_fields = ('user',)


#Admin panel serializers

class AssemblyWarehouseStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssemblyWarehouse
        fields = ('purifierid','aw_manager','aw_executive','location','address','user','is_in_transport','timestamp','start_transport','end_transport')
        #fields = '__all__'
        #extra_kwargs = {'user': {'required': False}}
        read_only_fields = ('user',)

class CityWarehouseStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityWarehouse
        fields = ('purifierid','cw_manager','cw_executive','location','address','user','is_in_transport','timestamp','start_transport','end_transport')
        #fields = '__all__'
        #extra_kwargs = {'user': {'required': False}}
        read_only_fields = ('user',)

class SubWarehouseStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubWarehouse
        fields = ('purifierid','sw_manager','sw_executive','location','address','user','is_in_transport','timestamp','start_transport','end_transport')
        #fields = '__all__'
        #extra_kwargs = {'user': {'required': False}}
        read_only_fields = ('user',)

class SubWarehouseCustSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubWarehouse
        fields = ('purifierid','customer_transport','cust_name','cust_phoneno')
        #fields = '__all__'
        #extra_kwargs = {'user': {'required': False}}
        read_only_fields = ('user',)
