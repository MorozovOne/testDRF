from django.shortcuts import render

# Create your views here.
class AnimeAPIView(generics.ListAPIView):
    queryset = Anime.objects.all()