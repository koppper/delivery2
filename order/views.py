from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from order.forms import UserEditForm, ProfileEditForm, UserRegisterForm
from order.models import Profile


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                   data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'order/edit.html',
                      {'user_form': user_form, 'profile_form': profile_form})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'order/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'order/create_profile.html'
    fields = ['image', 'bio', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('main')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            Profile.objects.create(user=user)
            user.save()
            return redirect('product_list')
    else:
        form = UserRegisterForm()
        messages.error(request, 'Ошибка регистрации')
    return render(request, 'order/register.html', {'form': form})


def log_in(request):
    title = 'Вход'
    context = {
        'title': title
    }
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context['error'] = "Entered username or password are invalid!"
        else:
            return redirect("product_list")
    return render(request, "order/login.html", context=context)


def user_logout(request):
    logout(request)
    return redirect('login')

