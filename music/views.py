from django.http import FileResponse
import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Booking, Artist
from .forms import SongForm,SignupForm, BookingForm, ArtistForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
def is_admin(user):
    return user.is_staff
@login_required
@user_passes_test(is_admin)
def upload_song(request):
    if request.method=='POST':
        form=SongForm(request.POST, request.FILES)
        if form.is_valid():
            song=form.save(commit=False)
            song.save()
            return redirect('song_list')
    else:
        form=SongForm()
    return render(request, 'music/upload.html', {'form':form})
def song_list(request):
    query=request.GET.get('q')
    if query:
        songs=Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))
    else:
        songs=Song.objects.all()
    return render(request, 'music/list.html', {'songs':songs, 'query':query})
def song_detail(request,pk):
    song=song.objects.get(pk=pk)
    return render(request, 'music/detail.html', {'song':song})
'''def songlist(request):
    query=request.GET.get('q')
    if query:
        songs=Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))
    else:
        songs=Song.objects.all()
        return render(request, 'music/list.html', {'songs':songs, 'query':query})'''
def download(request,pk):
    song=Song.objects.get(pk=pk)
    file_path=song.audio_file.path
    return FileResponse(open(file_path, 'rb'),as_attachment=True)
def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('song_list')
    else:
        form=SignupForm()
    return render(request, 'music/signup.html',{'form':form})
@login_required
def book_artist(request, artist_id):
    artist=get_object_or_404(Artist, id=artist_id)
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            booking=form.save(commit=False)
            booking.customer=request.user
            booking.artist_name=artist.stage_name
            booking.save()
        return redirect('artist_detail',artist_id )
    else:
        form=BookingForm()
    return render(request, 'music/book_artist.html', {'artist':artist, 'form':form})
@login_required
def artist_bookings(request):
    bookings=Booking.objects.all().order_by('-created_at')
    return render(request, 'music/artist_bookings.html', {"bookings":bookings})
def artist_list(request):
    artists=Artist.objects.all()
    return render(request, 'music/artists.html', {'artists':artists})
def artist_detail(request, pk):
    artist=get_object_or_404(Artist,pk=pk)
    return render(request, 'music/artist_detail.html',{'artist':artist})
@login_required
def create_artist(request):
    if request.method=="POST":
        form=ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist=form.save(commit=False)
            artist.user=request.user
            artist.save()
            return redirect('artist_detail', artist.id)
    else:
        form=ArtistForm()
        return render(request, 'music/create_artist.html', {'form':form})
@login_required
def update_artist(request, pk):
    artist=get_object_or_404(Artist, pk=pk)
    if request.method=='POST':
        form=ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_detail',artist.id)
        if artist.user!=request.user:
             return redirect('artist_list')
    else:
        form=ArtistForm()
        instance=artist
        return render(request,'music/update_artist.html', {'form':form})
@login_required
def delete_artist(request, pk):
    artist=get_object_or_404(Artist, pk=pk)
    if request.method=='POST':
        artist.delete()
        if artist.user!=request.user:
         return redirect('artist_list')
    return render(request, 'music/delete_artist.html',{'artist':artist})

@login_required
def accept_booking(request, pk):
    booking=get_object_or_404(Booking, pk=pk)
    booking.status='accepted'
    booking.save()
    return redirect('artist_bookings')
@login_required
def reject_booking(request, pk):
    booking=get_object_or_404(Booking,pk=pk)
    booking.status='rejected'
    booking.save()
    return redirect('artist_bookings')
@login_required
def notifications(request):
    notifications=request.user.notification_se.order_by('-created_at')
    return render(request, 'music/notification.html', {'notifications':notifications})