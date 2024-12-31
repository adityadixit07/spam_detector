from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models import Case, When
from .models import Contact
from .serializers import ContactSerializer

class SpamView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        contact, _ = Contact.objects.get_or_create(phone_number=phone_number)
        contact.is_spam = True
        contact.save()
        return Response({'message': 'Number marked as spam'}, status=status.HTTP_200_OK)

class SearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query')
        if query.isdigit():
            contacts = Contact.objects.filter(phone_number__icontains=query)
        else:
            contacts = Contact.objects.annotate(
                starts_with=Case(
                    When(name__istartswith=query, then=True),
                    default=False,
                    output_field=models.BooleanField()
                )
            ).order_by('-starts_with', 'name')
        
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
