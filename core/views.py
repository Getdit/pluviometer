from django.shortcuts import get_object_or_404, Http404
from django.http.response import FileResponse
from core.models import TempURL


def download_temporary_file(request, uuid):
    temp_url = get_object_or_404(TempURL, slug=uuid)

    if temp_url.is_valid():
        response = FileResponse(open(temp_url.path, 'rb'))
        temp_url.valid = False
        temp_url.save()
        return response
    raise Http404

from django.http import HttpResponse

def showFirebaseJS(request):
    data='''importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");
     importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js");

     // Initialize the Firebase app in the service worker by passing the generated config
     const firebaseConfig = {
     apiKey: "AIzaSyCMWnMUxwERltoyIipBiffguQqkCOiHtl0",

     authDomain: "petshop-3871e.firebaseapp.com",

     projectId: "petshop-3871e",

     storageBucket: "petshop-3871e.appspot.com",

     messagingSenderId: "701092389886",

     appId: "1:701092389886:web:888346904c0b399a7216af",

     measurementId: "G-8NGF95RR5C",
     };

     firebase.initializeApp(firebaseConfig);

     // Retrieve firebase messaging
     const messaging = firebase.messaging();

     messaging.onBackgroundMessage(function (payload) {
     console.log("Received background message ", payload);

     const notificationTitle = payload.notification.title;
     const notificationOptions = {
     body: payload.notification.body,
     };

     self.registration.showNotification(notificationTitle, notificationOptions);
     });'''

    return HttpResponse(data,content_type="text/javascript")