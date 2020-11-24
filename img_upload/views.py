from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .models import Upload
from .import forms
import pytesseract as tess
from PIL import Image


def upload(request):
    if(request.method=="POST"):
        form=forms.image_upload(request.POST,request.FILES)
        if(form.is_valid()):
            instance=form.save(commit=False)
            img=Image.open(instance.image)
            text=tess.image_to_string(img)
            instance.ocr=text
            instance.save()
            return HttpResponseRedirect("display")
    else:
        form=forms.image_upload()
    return render(request,"forms.html",{"form":form})

def display(request):
    data=Upload.objects.all().order_by("img_name")
    return render(request,"display.html",{"data":data})

def delete(request):
    if(request.method=="POST"):
        primary_key=request.POST.get("primary_key")
        obj=get_object_or_404(Upload,pk=primary_key)
        obj.delete()
    data=Upload.objects.all().order_by("img_name")
    return render(request,"display.html",{"data":data})
        
def editText(request):
    if(request.method=="POST"):
        primary_key=request.POST.get("primary_key")
        new_text=request.POST.get("title")
        obj=get_object_or_404(Upload,pk=primary_key)
        obj.img_name=new_text
        obj.save()
    data=Upload.objects.all().order_by("img_name")
    return render(request,"display.html",{"data":data})
