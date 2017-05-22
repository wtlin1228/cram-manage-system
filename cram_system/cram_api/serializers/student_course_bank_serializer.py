from rest_framework import serializers

from cram_api.models.student_model import StudentCourseBank


class StudentCourseBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourseBank
        fields = (
            'id',
            'owner',
            'course',
            'balance',
            'updated_at',
            'created_at'
        )
