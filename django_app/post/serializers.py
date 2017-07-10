from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    photo = serializers.ImageField()
    my_comment = serializers.CharField()
    like_users = serializers.CharField()


class SnippetSerializer1(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Post
        fields = (
            'author',
            'photo',
            'my_comment',
            'like_users'
        )
