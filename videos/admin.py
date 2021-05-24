from django.contrib import admin
from .models import videoAllProxy, VideoPublishedProxy

# Register your models here.

class VideoAllAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'video_id', 'state', 'is_published', 
    ]
    list_filter = ['video_id', 'active']
    readonly_fields = ['id', 'is_published', 'publish_timestamp', ]
    search_fields = ['title']
    class Meta:
        model = videoAllProxy
    
    # def published(self, obj, *args, **kwargs):
    #     return obj.active


admin.site.register(videoAllProxy, VideoAllAdmin)


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    list_filter = ['video_id']
    search_fields = ['title']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoProxy.objects.filter(active=True)


admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
