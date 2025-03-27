from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from .models import Photo
from .serializers import PhotoSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PhotoForm
from django.http import HttpResponse


# List all photos or create a new photo



# Page HTML pour la liste des photos
def photo_list_page(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'list.html', {'photos': photos})

# Page HTML pour l'upload
def photo_upload_page(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})


# Vue pour afficher le détail d'une photo
def photo_detail_page(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo_detail.html', {'photo': photo})

# Vue pour supprimer une photo
def photo_delete_page(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('photo_list')
# ***********

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def photo_upload(request):
    print("\n=== DONNÉES REÇUES ===")
    print("POST Data:", request.POST)  # Vérifiez 'title'
    print("FILES Data:", request.FILES)  # Vérifiez 'image'

    if 'image' not in request.FILES:
        return Response({"error": "Aucun fichier 'image' reçu"}, status=400)

    # Test manuel (bypass serializer)
    try:
        new_photo = Photo.objects.create(
            title=request.POST.get('title'),
            image=request.FILES['image']
        )
        return Response({"success": f"Photo {new_photo.id} créée !"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
@api_view(['GET', 'POST'])
def photo_list(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve a specific photo
@api_view(['GET'])
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    serializer = PhotoSerializer(photo)
    return Response(serializer.data)


# Update an existing photo
@api_view(['PUT', 'PATCH'])
def photo_update(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    serializer = PhotoSerializer(photo, data=request.data, partial=True)  # partial=True permet un PATCH
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a photo
@api_view(['DELETE'])
def photo_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)