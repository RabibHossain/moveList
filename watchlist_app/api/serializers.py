from watchlist_app.models import WatchList, StreamPlatform
from rest_framework import serializers



"""
Model Serializer Functionalities
"""



class WatchListSerializer(serializers.ModelSerializer):

    # Adding custom fields
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name']


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name = 'stream-detail'
    # )
 
    class Meta:
        model = StreamPlatform
        fields = "__all__"        
 
    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title & Description should be different!")
    #     else:
    #         return data


"""
Serializer Functionalities
"""

# def description_length(value):
#     if len(value) < 5:
#         raise serializers.ValidationError("Description is too short!!!")
#     else:
#         return value 

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Movie` instance, given the validated data.
#         """
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Movie` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()

#         return instance

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title & Description should be different!")
#         else:
#             return data
