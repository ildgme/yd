
from django.shortcuts import render
from pytube import YouTube

def index(request):

	try:
		
		# check request.method is post or not
		if request.method == 'POST':
			try:
				# get link from the html form
				link = request.POST['link']
				down_link = request.POST['down_link']
				video = YouTube(link)

				# set video resolution
				stream = video.streams.get_highest_resolution()

				# DOWNLOAD_FOLDER = "d:/youtube_download/"
				
				# download the video 
				stream.download(down_link)

				# render HTML page
				return render(request, 'index.html', {'msg':'Video downloaded'})
			except:
				return render(request, 'index.html', {'msg':'Video not downloaded'})
		return render(request, 'index.html', {'msg':''})
	except:
		return render(request, "index.html", {"msg":"Sorry something went wrong!"})