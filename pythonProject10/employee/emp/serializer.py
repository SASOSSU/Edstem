from rest_framework import serializers
from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmyloyeeSerializer(serializers.Serializer):
    empy_id = serializers.IntegerField()
    empy_name = serializers.CharField(max_length=30)
    empy_age = serializers.IntegerField()
    empy_salary = serializers.FloatField()
    empy_dep = serializers.CharField(max_length=30)

    def add_profile(self, validated_data):
        user_obj = Department.objects.filter(dep=validated_data.get("empy_dep")).first()
        if user_obj:
            obj, created = Employee.objects.update_or_create(
                id=validated_data.get("empy_id"),
                name=validated_data.get("empy_name"),
                age=validated_data.get("empy_age"),
                salary=validated_data.get("empy_salary"),
                dep=user_obj,

            )
