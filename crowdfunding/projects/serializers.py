# All of the below has been created by me
from rest_framework import serializers
from .models import Project, Pledge, Comment #, Pledge added from DRF doc 2

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id') #added from user doc
# pledges = PledgeSerializer(many=True, read_only=True) #added from DRF doc 2
    def update(self, instance, validated_data): #this below section added from permissions doc
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def create(self, validated_data):
        return Project.objects.create(**validated_data)



class CommentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    project = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()
    author = serializers.ReadOnlyField(source='owner.id') 


    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

#new addition from DRF doc 2
class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter'] #added from User doc

#Added from DRF doc 2
class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    