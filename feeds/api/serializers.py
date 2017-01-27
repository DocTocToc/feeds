from rest_framework import serializers
from category.models import Category

from ..models import Feed, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'url', )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'feed',
            'title',
            'link',
            'published',
        )


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = (
            'url',
            'get_absolute_url',
            'website',
            'feed_url',
            'name',
            'short_name',
            'slug',
            'is_active',
            'errors',
            'category',
            'title',
            'link',
            'tagline',
            'language',
            'copyright',
            'author',
            'webmaster',
            'pubDate',
            'last_modified',
            'ttl',
            'image_title',
            'image_link',
            'image_url',
            'etag',
            'last_checked',
            'check_interval',
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ('name', )
