from rest_framework import serializers
from .models import SystemAnalyst
from .models import SoftwareTester
from .models import BackEnd
from .models import FrontEnd
from .models import UiUx

#Json for SA
class SystemAnalystSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAnalyst
        fields = ['id', 'Name', 'EmployeeID',  'MonthlySalary']

#Json for ST
class SoftwareTesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareTester
        fields = ['id', 'Name', 'EmployeeID',  'MonthlySalary']

#Json for BE
class BackEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackEnd
        fields = ['id', 'Name', 'EmployeeID', 'MonthlySalary']

#Json for FE
class FrontEndSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontEnd
        fields = ['id', 'Name', 'EmployeeID', 'MonthlySalary']

#Json for UiUx
class UiUxSerializer(serializers.ModelSerializer):
    class Meta:
        model = UiUx
        fields = ['id', 'Name', 'EmployeeID',  'MonthlySalary']
