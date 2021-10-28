from django.shortcuts import render
from .models import Test, Message
from .forms import TestForm
import joblib
import pandas as pd

algorithm = joblib.load('./algorithm/DecisionTreeClassifier.pkl')


def index(request):
    return render(request, 'home.html', {})


def diet(request,prognosis):
    if prognosis == 'Diabetes':
        return render(request, 'Diabetes.html', {})
    elif prognosis == 'Fungal infection':
        return render(request, 'Fungal_infection.html', {})
    elif prognosis == 'Peptic ulcer disease':
        return render(request, 'Peptic_ulcer_disease.html', {})
    elif prognosis == 'Gastroenteritis':
        return render(request, 'Gastroenteritis.html', {})
    else:
        return render(request, 'Chronic_cholestasi.html', {})


def test(request):
    context = {}
    if request.POST:
        form = TestForm(request.POST)
        if form.is_valid:
            itching = request.POST.get('itching')
            skin_rash = request.POST.get('skin_rash')
            vomiting = request.POST.get('vomiting')
            fatigue = request.POST.get('fatigue')
            weight_loss = request.POST.get('weight_loss')
            irregular_sugar_level = request.POST.get('irregular_sugar_level')
            sunken_eyes = request.POST.get('sunken_eyes')
            dehydration = request.POST.get('dehydration')
            indigestion = request.POST.get('indigestion')
            yellowish_skin = request.POST.get('yellowish_skin')
            nausea = request.POST.get('nausea')
            loss_of_appetite = request.POST.get('loss_of_appetite')
            abdominal_pain = request.POST.get('abdominal_pain')
            diarrhoea = request.POST.get('diarrhoea')
            yellowing_of_eyes = request.POST.get('yellowing_of_eyes')
            blurred_and_distorted_vision = request.POST.get('blurred_and_distorted_vision')
            obesity = request.POST.get('obesity')
            excessive_hunger = request.POST.get('excessive_hunger')
            passage_of_gases = request.POST.get('passage_of_gases')
            internal_itching = request.POST.get('internal_itching')
            dischromic_patches = request.POST.get('dischromic_patches')
            increased_appetite = request.POST.get('increased_appetite')
            polyuria = request.POST.get('polyuria')
            
            
            def val2(x):
                if x == 0:
                    return 'Diabetes'
                elif x == 1:
                    return 'Fungal infection'
                elif x == 2:
                    return 'Peptic ulcer disease'
                elif x == 3:
                    return 'Gastroenteritis'
                else:
                    return 'Chronic cholestasis'
            temp = {
                'itching' : itching,
                'skin_rash' : skin_rash,
                'vomiting' : vomiting,
                'fatigue' : fatigue,
                'weight_loss' : weight_loss,
                'irregular_sugar_level' : irregular_sugar_level,
                'sunken_eyes' : sunken_eyes,
                'dehydration' : dehydration,
                'indigestion' : indigestion,
                'yellowish_skin' : yellowish_skin,
                'nausea' : nausea,
                'loss_of_appetite' : loss_of_appetite,
                'abdominal_pain' : abdominal_pain,
                'diarrhoea' : diarrhoea,
                'yellowing_of_eyes' : yellowing_of_eyes,
                'blurred_and_distorted_vision' : blurred_and_distorted_vision,
                'obesity' : obesity,
                'excessive_hunger' : excessive_hunger,
                'passage_of_gases' : passage_of_gases,
                'internal_itching' : internal_itching,
                'dischromic_patches' : dischromic_patches,
                'increased_appetite' : increased_appetite,
                'polyuria' : polyuria,
            }
            testdata = pd.DataFrame(temp, index=[0])
            print(testdata)
            status = algorithm.predict(testdata)
            prognosis = val2(status)

            test_record = Test(
                user = request.user,
                itching = itching,
                skin_rash = skin_rash,
                vomiting = vomiting,
                fatigue = fatigue,
                weight_loss = weight_loss,
                irregular_sugar_level = irregular_sugar_level,
                sunken_eyes = sunken_eyes,
                dehydration = dehydration,
                indigestion = indigestion,
                yellowish_skin = yellowish_skin,
                nausea = nausea,
                loss_of_appetite = loss_of_appetite,
                abdominal_pain = abdominal_pain,
                diarrhoea = diarrhoea,
                yellowing_of_eyes = yellowing_of_eyes,
                blurred_and_distorted_vision = blurred_and_distorted_vision,
                obesity = obesity,
                excessive_hunger = excessive_hunger,
                passage_of_gases = passage_of_gases,
                internal_itching = internal_itching,
                dischromic_patches = dischromic_patches,
                increased_appetite = increased_appetite,
                polyuria = polyuria,
                prognosis = prognosis
            )            
            test_record.save()
            context['prognosis']=prognosis
            return render(request, 'test_result.html', context)
        else:
            context['eorror':'User imput error! please ensure to correctly fill the test form']
            return render(request, 'test.html', context)
    else:
        form = TestForm()
    context['form'] = form
    return render(request, 'test.html', context)

def message(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    s = Message(name=name, email=email, subject=subject, message=message)
    s.save()