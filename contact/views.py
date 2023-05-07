from django.shortcuts import render


class ContactMe(View):

    def get(self, request, *args, **kwargs):
        return render(request, "./contact-me.html")