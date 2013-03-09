from django.shortcuts import render


def profile(request):
    context = {
        'values':
            [
                [10, 40, 50],
                [80, 50, 30],
                [75, 80, 40],
            ]
    }

    return render(request, 'user_profile/profile.html', context)


def send_message(request):
    from messages.views import compose

    return compose(request, recipient="admin", template_name="user_profile/message/compose.html", )

def messages(request):

    from messages.views import inbox

    return inbox(request, 'user_profile/message/list.html')


