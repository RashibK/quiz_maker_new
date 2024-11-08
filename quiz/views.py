from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from quiz_maker.story_generator import generate_story
from quiz.utils.pdf_utils import extract_text_from_pdf

 
def generate_story_from_words(request):
        file_path = "/home/chips/coding/python/quiz_maker_new/deliverable 2.pdf"
        pdf_text = extract_text_from_pdf(file_path)
        story = generate_story(pdf_text)

        return HttpResponse(f"Generated text: {story}")



def home(request):
    return render(request, 'quiz/home.html')

