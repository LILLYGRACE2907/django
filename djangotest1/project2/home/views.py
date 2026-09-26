from django.http import HttpResponse

def home(request):
    return HttpResponse("""""
                        <h1>Welcome to my Django Project!</h1>
                        <p>This is the home page of my Django Project.</p>
                        """)
def about(request):
    return HttpResponse("""
    <h1>About Us</h1>
    <p>This is the about page of my Django Project.</p>
    """)
def contact(request):
    return HttpResponse("""
    <h1>Contact Us</h1>
    <p>This is the contact page of my Django Project.</p>
    """)
def services(request):
    return HttpResponse("""
    <h1>Our Services</h1>
    <p>This is the services page of my Django Project.</p>
    """)