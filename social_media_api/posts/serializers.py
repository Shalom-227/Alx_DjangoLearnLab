from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    ''' *source* attribute in a serializer field is used to specify the attribute from which to retrieve the value during serialization or deserialization. This is helpful when the field you want to serialize is not a direct field of the model associated with the serializer '''
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at']
        #fields that cannot be edited
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        """Ensure the logged-in user is set as the author"""
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
            return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Read-only author field and displays username instead of ID
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        """Ensure the logged-in user is set as the comment author"""
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
            return super().create(validated_data)



