# views.py
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import cv2
import os
from django.conf import settings
from .models import Certificate

# Load the template certificate image (save it in the static folder)
template_image = cv2.imread(os.path.join(settings.STATIC_ROOT, 'template.png'))

# Function to update the image with text
def update_certificate_template(template_image, user_name):
    # Make a copy of the template to work on
    template = template_image.copy()
    coords = (x,y) # Replace with coordinate of where to update

    # Define the font, color, and size for the text to be added
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    font_color = (0, 0, 0)  # Black color (BGR format)
    font_scale = 1
    thickness = 1
    line_type = cv2.LINE_AA

    # Put the user's name at the specified coordinates
    cv2.putText(template, user_name, coords, font, font_scale, font_color, thickness, lineType=line_type)

    return template

# View for generating and updating certificates
def generate_certificate(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']

        updated_template = update_certificate_template(template_image, user_name)

        # Convert the updated image to a format suitable for saving
        ret, buf = cv2.imencode('.png', updated_template)
        image = ContentFile(buf.tobytes())

        certificate = Certificate(user_name=user_name)
        certificate.certificate_image.save(f"{user_name}.png", image)
        certificate.save()

        return redirect('certificate_display', id=certificate.id)
    else:
        return render(request, 'certificate-form.html')

# View for displaying the updated certificate
def certificate_display(request, id):
    certificate = Certificate.objects.get(id=id)
    return render(request, 'certificate-display.html', {'certificate': certificate})
