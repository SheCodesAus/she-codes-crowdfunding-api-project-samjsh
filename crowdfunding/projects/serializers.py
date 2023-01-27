# All of the below has been created by me
from rest_framework import serializers
from .models import Project, Pledge #, Pledge added from DRF doc 2


class ProjectSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	title = serializers.CharField(max_length=200)
	description = serializers.CharField(max_length=None)
	goal = serializers.IntegerField()
	image = serializers.URLField()
	is_open = serializers.BooleanField()
	date_created = serializers.DateTimeField()
	owner = serializers.CharField(max_length=200)
	
	def create(self, validated_data):
		return Project.objects.create(**validated_data)

#new addition from DRF doc 2
class PledgeSerializer(serializers.ModelSerializer):
	class Meta:
            model = Pledge
            fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']