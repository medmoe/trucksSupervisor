from agent.models import Entry
from agent.serializers import EntrySerializer
from rest_framework import mixins
from rest_framework import generics


# Create your views here.

class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
