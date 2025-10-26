import datetime

from django.http import HttpResponse
from django.views import View


def home(request):
    return HttpResponse("Welcome to the Home Page!")



def current_datetime(request):
    html = """
    <html>
        <head>
            <title>Live Date & Time</title>
            <style>
                body {
                    background: linear-gradient(to right, #6a11cb, #2575fc);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    color: #ffffff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    background-color: rgba(0, 0, 0, 0.3);
                    padding: 50px 80px;
                    border-radius: 20px;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
                    animation: fadeIn 2s ease-in-out;
                }
                h1 {
                    font-size: 2.5em;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 1.5em;
                    letter-spacing: 1px;
                }
                @keyframes fadeIn {
                    from { opacity: 0; transform: scale(0.8); }
                    to { opacity: 1; transform: scale(1); }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌟 Current Date & Time 🌟</h1>
                <p id="clock">Loading...</p>
            </div>
            <script>
                function updateClock() {
                    const now = new Date();
                    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
                    const dateStr = now.toLocaleDateString(undefined, options);
                    const timeStr = now.toLocaleTimeString();
                    document.getElementById('clock').innerText = dateStr + " | " + timeStr;
                }
                setInterval(updateClock, 1000); // update every second
                updateClock(); // initial call
            </script>
        </body>
    </html>
    """
    return HttpResponse(html)



class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")

from django.shortcuts import render

# Create your views here.
