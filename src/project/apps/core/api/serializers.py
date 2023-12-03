from rest_framework.serializers import ModelSerializer
from apps.core.models import (
    Contact,
    WebsiteInformation)



class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )


class WebsiteInformationSerializer(ModelSerializer):
    class Meta:
        model = WebsiteInformation
        fields = (
            'website_logo',
            'location', 
            'email',
            'tel_number',
            'twitter_link',
            'facebook_link', 
            'instagram_link', 
            'linkedin_link', 
            'youtube_link'
        )