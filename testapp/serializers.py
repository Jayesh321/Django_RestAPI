from rest_framework import serializers
from testapp.models import Article

# (REST Framework Modal Serializer):
#------------------------------------------------------
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ['id', 'title', 'auther', 'email']
        fields = '__all__'

# (Django REST Framework  Serializer):This form is used to create data from django shell and get data from the shell only
#------------------------------------------------------------------------------------------

# class ArticleSerializer(serializers.Serializer):
#     #id = serializers.ImageField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     auther = serializers.CharField(max_length=50)
#     email = serializers.EmailField()
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.

#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.auther = validated_data.get('auther', instance.auther)
#         instance.email = validated_data.get('email',instance.email)
#         instance.data = validated_data.get('date', instance.data)
#         instance.save()
#         return instance


