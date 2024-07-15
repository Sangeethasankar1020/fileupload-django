# views.py

from django.shortcuts import render, redirect
from django.conf import settings
from firebase_admin import storage, firestore
from pymongo import MongoClient
from firebase_admin import credentials, storage as firebase_storage
from google.cloud import storage as gcs_storage
from google.auth import compute_engine
# def upload_to_firebase(request):
#     if request.method == 'POST' and request.FILES.get('file'):
#         # Get the file object from the POST request
#         file_obj = request.FILES['file']

#         # Initialize Firebase Storage
#         try:
#             bucket = storage.bucket()

#             # Define the destination path in Firebase Storage
#             blob = bucket.blob(file_obj.name)

#             # Upload file to Firebase Storage
#             blob.upload_from_file(file_obj)

#             # Get the download URL of the uploaded file
#             firebase_url = blob.public_url

#             # Optionally, store Firebase URL in MongoDB or perform other actions

#             # Store Firebase URL in MongoDB using PyMongo
#             client = MongoClient('mongodb://localhost:27017')
#             db = client['fileupload']
#             collection = db['image']
        
#          # Create a document with Firebase URL
#             document = {
#             'file_name': file_obj.name,
#             'firebase_url': firebase_url,
#             }
        
#          # Insert document into MongoDB collection
#             result = collection.insert_one(document)



#             # Render a success response
#             return render(request, 'upload_success.html', {'firebase_url': firebase_url})
        
#         except Exception as e:
#             # Handle exceptions, log errors, etc.
#             print(f"Error uploading file to Firebase Storage: {str(e)}")
#             return render(request, 'upload_error.html', {'error_message': 'Failed to upload file'})

#     # Render the upload form if not a POST request or no file selected
#     return render(request, 'upload.html')

def upload_to_firebase(request):
    if request.method == 'POST' and request.FILES.get('file'):
        # Get the file object from the POST request
        file_obj = request.FILES['file']

        # Initialize Firebase Admin SDK
        # cred = credentials.Certificate('path/to/serviceAccountKey.json')
        # firebase_admin.initialize_app(cred, {
        #     'storageBucket': 'your-firebase-storage-bucket-url'
        # })

        # Initialize Firebase Storage
        firebase_client = firebase_storage.bucket()

        # Define the destination path in Firebase Storage
        blob = firebase_client.blob(file_obj.name)

        # Upload file to Firebase Storage
        blob.upload_from_file(file_obj)

        # Generate a signed URL for the uploaded file
        # Note: Adjust the expiration time (e.g., 3600 seconds = 1 hour) as needed
        signed_url = blob.generate_signed_url(
            version='v4',
            expiration=3600,
            method='GET'
        )

        # Optionally, store the signed URL in MongoDB or perform other actions

        # Store signed URL in MongoDB using PyMongo
        # Example MongoDB code here...

        # Render a success response
        return render(request, 'upload_success.html', {'signed_url': signed_url})

    # Render the upload form if not a POST request or no file selected
    return render(request, 'upload.html')